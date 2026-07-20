#!/usr/bin/env python3
"""Simple HTTP server for QA Agent Hub - No external dependencies"""

import json
import urllib.request
import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

AGENTS = {
    "gherkin-converter": {"name": "Gherkin Converter", "category": "Junior QA"},
    "test-case-writer": {"name": "Test Case Writer", "category": "Junior QA"},
    "bug-reporter": {"name": "Bug Reporter", "category": "Junior QA"},
    "test-data-generator": {"name": "Test Data Generator", "category": "Junior QA"},
    "api-test-generator": {"name": "API Test Generator", "category": "Senior QA"},
    "automation-builder": {"name": "Automation Script Builder", "category": "Senior QA"},
    "sql-helper": {"name": "SQL Query Helper", "category": "Senior QA"},
    "performance-tester": {"name": "Performance Test Creator", "category": "Senior QA"},
    "sprint-planner": {"name": "Sprint Test Planner", "category": "Team Lead"},
    "defect-triage": {"name": "Defect Triage Assistant", "category": "Team Lead"},
    "coverage-analyzer": {"name": "Coverage Analyzer", "category": "Team Lead"},
    "release-readiness": {"name": "Release Readiness Checker", "category": "Team Lead"},
}

MOCK_RESPONSES = {
    "gherkin-converter": """Here's your Gherkin conversion:

```gherkin
Feature: Fund Transfer
  As a bank customer
  I want to transfer funds between accounts
  So that I can manage my money

  Background:
    Given user is logged into the banking portal
    And user has a valid source account

  @smoke @banking @transfer
  Scenario: Successful fund transfer between own accounts
    Given the source account has balance of "5000" INR
    When user initiates transfer of "1000" INR to savings account
    Then transfer should be completed successfully
    And source account balance should be "4000" INR

  @negative @banking
  Scenario: Fund transfer with insufficient balance
    Given the source account has balance of "500" INR
    When user initiates transfer of "1000" INR
    Then transfer should fail with message "Insufficient funds"
```""",
    "test-case-writer": """## Test Cases Generated

| TC ID | Title | Priority |
|-------|-------|----------|
| TC_001 | Verify successful login with valid credentials | High |
| TC_002 | Verify login fails with invalid password | High |
| TC_003 | Verify account lockout after 3 failed attempts | High |
| TC_004 | Verify password field is masked | Medium |

### TC_001: Verify successful login with valid credentials

**Preconditions:**
- User has valid banking credentials
- Application is accessible

**Test Steps:**
1. Navigate to login page
2. Enter valid username
3. Enter valid password
4. Click Login button

**Expected Result:**
- User is redirected to dashboard
- Welcome message displays user name""",
    "bug-reporter": """## Bug Report

**Bug ID:** BUG-2024-001  
**Title:** Fund transfer fails silently when session expires

**Environment:** UAT | Chrome 120 | Windows 11

**Severity:** High  
**Priority:** P1

**Steps to Reproduce:**
1. Login to banking portal
2. Wait for 15 minutes (session timeout)
3. Initiate fund transfer
4. Click Submit

**Expected Result:** Error message about session expiry

**Actual Result:** No error shown, transfer appears to complete but money not transferred

**Attachments:** [Screenshot placeholder]""",
    "test-data-generator": """## Generated Test Data

### Customer Data
| Field | Value |
|-------|-------|
| Name | John Smith (FAKE) |
| Account No | 1234567890 |
| IBAN | GB82WEST12345698765432 |
| Sort Code | 12-34-56 |

### Transaction Data
| Type | Amount | Currency |
|------|--------|----------|
| Credit | 5000.00 | INR |
| Debit | 1500.50 | INR |
| Transfer | 2000.00 | INR |

### Card Data (TEST ONLY)
| Card Number | Expiry | CVV |
|-------------|--------|-----|
| 4111111111111111 | 12/25 | 123 |

*All data is FAKE and for testing purposes only*""",
    "api-test-generator": """## API Test Script (Python + pytest)

```python
import pytest
import requests

BASE_URL = "https://api.bank.com/v1"

class TestFundTransfer:
    
    @pytest.fixture
    def auth_headers(self):
        return {"Authorization": "Bearer test_token"}
    
    def test_successful_transfer(self, auth_headers):
        payload = {
            "from_account": "1234567890",
            "to_account": "0987654321",
            "amount": 1000.00,
            "currency": "INR"
        }
        
        response = requests.post(
            f"{BASE_URL}/transfer",
            json=payload,
            headers=auth_headers
        )
        
        assert response.status_code == 200
        assert response.json()["status"] == "success"
        assert response.json()["transaction_id"] is not None
    
    def test_insufficient_funds(self, auth_headers):
        payload = {
            "from_account": "1234567890",
            "to_account": "0987654321",
            "amount": 999999.00,
            "currency": "INR"
        }
        
        response = requests.post(
            f"{BASE_URL}/transfer",
            json=payload,
            headers=auth_headers
        )
        
        assert response.status_code == 400
        assert "insufficient" in response.json()["error"].lower()
```""",
    "automation-builder": """## Selenium Automation Script (Python)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-msg")
    
    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text


# Test
def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://banking.example.com/login")
    
    login_page = LoginPage(driver)
    login_page.login("testuser", "password123")
    
    assert "dashboard" in driver.current_url
    driver.quit()
```""",
}


class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == '/':
            self._set_headers()
            self.wfile.write(json.dumps({"message": "QA Agent Hub API", "status": "running"}).encode())
        
        elif parsed.path == '/api/agents':
            self._set_headers()
            agents_list = [{"id": k, "name": v["name"]} for k, v in AGENTS.items()]
            self.wfile.write(json.dumps(agents_list).encode())
        
        elif parsed.path.startswith('/api/agents/'):
            agent_id = parsed.path.split('/')[-1]
            if agent_id in AGENTS:
                self._set_headers()
                self.wfile.write(json.dumps({"id": agent_id, **AGENTS[agent_id]}).encode())
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Agent not found"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_POST(self):
        parsed = urlparse(self.path)
        
        if parsed.path.startswith('/api/chat/'):
            agent_id = parsed.path.split('/')[-1]
            
            if agent_id not in AGENTS:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Agent not found"}).encode())
                return
            
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            try:
                data = json.loads(body) if body else {}
                user_message = data.get('message', '')
                api_key = data.get('api_key', None)
            except:
                user_message = ''
                api_key = None
            
            # If API key provided, use OpenAI
            if api_key and api_key.startswith('sk-'):
                response_text = self.call_openai(api_key, agent_id, user_message, data.get('history', []))
            else:
                # Use mock response
                response_text = MOCK_RESPONSES.get(
                    agent_id,
                    f"I'm the **{AGENTS[agent_id]['name']}** agent.\n\nYou said: \"{user_message}\"\n\n*Demo Mode: Add your OpenAI API key (click the key icon in navbar) to get real AI responses.*"
                )
            
            self._set_headers()
            self.wfile.write(json.dumps({
                "response": response_text,
                "agent_id": agent_id
            }).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def call_openai(self, api_key, agent_id, user_message, history):
        """Call OpenAI API with the provided key"""
        system_prompts = {
            "gherkin-converter": "You are a Gherkin Converter Agent for a banking QA team. Convert requirements into proper Gherkin syntax with Feature, Scenario, Given, When, Then. Add tags like @smoke, @regression, @banking.",
            "test-case-writer": "You are a Test Case Writer Agent for banking QA. Generate detailed test cases with ID, Title, Preconditions, Steps, Expected Results, Priority.",
            "bug-reporter": "You are a Bug Reporter Agent. Format professional bug reports with Bug ID, Title, Environment, Severity, Priority, Steps to Reproduce, Expected/Actual Results.",
            "test-data-generator": "You are a Test Data Generator for banking. Generate realistic FAKE test data: account numbers, IBANs, transaction amounts, customer names. Never use real data.",
            "api-test-generator": "You are an API Test Generator for banking QA. Generate REST API test scripts in Python/Java with assertions and error handling.",
            "automation-builder": "You are an Automation Script Builder. Generate Selenium/Playwright/Cypress scripts following Page Object Model with proper waits and locators.",
            "sql-helper": "You are a SQL Query Helper for banking QA. Help build SELECT, INSERT, UPDATE queries for banking schema (accounts, customers, transactions).",
            "performance-tester": "You are a Performance Test Creator. Generate JMeter/Gatling/k6 scripts with thread groups, HTTP requests, assertions, and response time thresholds.",
            "sprint-planner": "You are a Sprint Test Planner. Create test plans with scope, approach, resources, timeline, risks, entry/exit criteria.",
            "defect-triage": "You are a Defect Triage Assistant. Analyze bugs and suggest severity, priority, category, root cause, and assignment.",
            "coverage-analyzer": "You are a Coverage Analyzer. Help with requirements-to-test mapping, gap identification, and traceability matrices.",
            "release-readiness": "You are a Release Readiness Checker. Evaluate test status, defects, coverage, and provide Go/No-Go recommendations.",
        }
        
        system_prompt = system_prompts.get(agent_id, f"You are the {AGENTS[agent_id]['name']} agent for banking QA.")
        
        messages = [{"role": "system", "content": system_prompt}]
        for msg in history[-10:]:
            messages.append({"role": msg.get("role", "user"), "content": msg.get("content", "")})
        messages.append({"role": "user", "content": user_message})
        
        try:
            payload = json.dumps({
                "model": "gpt-4o-mini",
                "messages": messages,
                "max_tokens": 2000,
                "temperature": 0.7
            }).encode('utf-8')
            
            req = urllib.request.Request(
                "https://api.openai.com/v1/chat/completions",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                }
            )
            
            # Create SSL context
            ctx = ssl.create_default_context()
            
            with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result['choices'][0]['message']['content']
        
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            return f"**API Error:** {e.code}\n\nPlease check your API key is valid and has credits.\n\nDetails: {error_body}"
        except Exception as e:
            return f"**Error calling OpenAI:** {str(e)}\n\nFalling back to demo mode. Check your network connection."

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]}")


def run(port=8000):
    server = HTTPServer(('', port), RequestHandler)
    print(f"🚀 QA Agent Hub API running at http://localhost:{port}")
    print("Press Ctrl+C to stop")
    server.serve_forever()


if __name__ == '__main__':
    run()
