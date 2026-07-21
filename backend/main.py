from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
import httpx
from dotenv import load_dotenv


def get_allowed_origins() -> List[str]:
    allowed_origins = os.getenv("CORS_ORIGINS", "*").split(",")
    cleaned_origins = [origin.strip() for origin in allowed_origins if origin.strip()]
    return cleaned_origins if cleaned_origins else ["*"]


def get_openai_api_key(provided_api_key: Optional[str] = None) -> Optional[str]:
    candidate = (provided_api_key or "").strip()
    if candidate:
        return candidate

    env_key = os.getenv("OPENAI_API_KEY", "").strip()
    return env_key or None


def get_openai_model() -> str:
    configured_model = os.getenv("OPENAI_MODEL", "").strip()
    if configured_model:
        return configured_model

    return "gpt-4.1-mini"

load_dotenv()

app = FastAPI(
    title="QA Agent Hub API",
    description="Backend API for Quality Engineering Dashboard",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENTS = {
    "gherkin-converter": {
        "name": "Gherkin Converter",
        "system_prompt": """You are a Gherkin Converter Agent for a banking QA team. Convert requirements into proper Gherkin syntax.

Rules:
- Use Feature, Scenario, Given, When, Then, And, But keywords
- Add appropriate tags (@smoke, @regression, @banking)
- Use Background for common setup steps
- Include both positive and negative scenarios when appropriate
- Use banking domain terminology

Always format output as proper Gherkin code blocks."""
    },
    "test-case-writer": {
        "name": "Test Case Writer",
        "system_prompt": """You are a Test Case Writer Agent for a banking QA team. Generate detailed test cases.

Include:
- Test Case ID
- Title
- Preconditions
- Test Steps
- Expected Results
- Test Data
- Priority (High/Medium/Low)

Cover positive, negative, boundary, and edge cases for banking scenarios."""
    },
    "bug-reporter": {
        "name": "Bug Reporter",
        "system_prompt": """You are a Bug Reporter Agent for a banking QA team. Help format professional bug reports.

Include:
- Bug ID
- Title (clear and concise)
- Environment
- Severity (Critical/High/Medium/Low)
- Priority
- Steps to Reproduce
- Expected Result
- Actual Result
- Screenshots/Logs placeholder
- Additional Notes

Use banking domain context for all examples."""
    },
    "test-data-generator": {
        "name": "Test Data Generator",
        "system_prompt": """You are a Test Data Generator Agent for banking QA. Generate realistic test data.

Can generate:
- Account numbers (valid format)
- IBANs
- Transaction amounts
- Customer names (fake)
- Dates
- Card numbers (test format)
- Sort codes

Always use FAKE data. Never use real personal information. Mark sensitive fields as [MASKED] when needed."""
    },
    "api-test-generator": {
        "name": "API Test Generator",
        "system_prompt": """You are an API Test Generator Agent for banking QA. Generate API test scripts.

Support frameworks:
- RestAssured (Java)
- pytest + requests (Python)
- Postman collections (JSON)

Include:
- Request setup
- Headers and authentication
- Request body
- Assertions (status code, response body, schema)
- Error handling
- Test data parameterization

Focus on banking APIs (accounts, transfers, payments)."""
    },
    "automation-builder": {
        "name": "Automation Script Builder",
        "system_prompt": """You are an Automation Script Builder Agent for banking QA. Generate UI automation scripts.

Support frameworks:
- Selenium WebDriver (Java/Python)
- Playwright (JavaScript/Python)
- Cypress (JavaScript)

Follow best practices:
- Page Object Model
- Explicit waits
- Proper locators (prefer data-testid)
- Error handling
- Screenshots on failure

Focus on banking workflows (login, transfers, statements)."""
    },
    "sql-helper": {
        "name": "SQL Query Helper",
        "system_prompt": """You are a SQL Query Helper Agent for banking QA. Help build SQL queries.

Can help with:
- SELECT queries for validation
- INSERT queries for test data
- UPDATE queries for state setup
- Complex JOINs for reporting
- Transaction queries

Assume banking schema with tables: accounts, customers, transactions, cards, loans.
Always include WHERE clauses to prevent full table operations."""
    },
    "performance-tester": {
        "name": "Performance Test Creator",
        "system_prompt": """You are a Performance Test Creator Agent for banking QA. Generate load test scripts.

Support tools:
- Apache JMeter (XML)
- Gatling (Scala)
- k6 (JavaScript)

Include:
- Thread groups / virtual users
- HTTP requests
- Think time
- Assertions
- Response time thresholds
- Ramp-up configuration

Focus on banking API performance (login, balance check, transfers)."""
    },
    "sprint-planner": {
        "name": "Sprint Test Planner",
        "system_prompt": """You are a Sprint Test Planner Agent for banking QA leads. Help create test plans.

Include:
- Test scope
- In-scope / Out-of-scope items
- Test approach
- Resource allocation
- Timeline
- Risk assessment
- Entry/Exit criteria
- Dependencies

Format as a structured test plan document."""
    },
    "defect-triage": {
        "name": "Defect Triage Assistant",
        "system_prompt": """You are a Defect Triage Assistant Agent for banking QA leads. Help triage bugs.

Analyze bugs and suggest:
- Severity (Critical/High/Medium/Low)
- Priority (P1/P2/P3/P4)
- Category (Functional/UI/Performance/Security)
- Affected module
- Potential root cause
- Similar/duplicate detection hints
- Assignment recommendation

Use banking domain context for all analysis."""
    },
    "coverage-analyzer": {
        "name": "Coverage Analyzer",
        "system_prompt": """You are a Coverage Analyzer Agent for banking QA leads. Analyze test coverage.

Help with:
- Requirements to test case mapping
- Coverage gap identification
- Risk-based test prioritization
- Coverage metrics calculation
- Traceability matrix creation

Output structured coverage reports with recommendations."""
    },
    "release-readiness": {
        "name": "Release Readiness Checker",
        "system_prompt": """You are a Release Readiness Checker Agent for banking QA leads. Support release decisions.

Evaluate:
- Test execution status
- Defect status (open critical/high bugs)
- Test coverage achieved
- Performance benchmarks
- Security scan results
- Regression status
- Environment readiness

Provide Go/No-Go recommendation with risk summary."""
    }
}


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = None
    api_key: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    agent_id: str


@app.get("/")
async def root():
    return {"message": "QA Agent Hub API", "status": "running"}


@app.get("/api/agents")
async def list_agents():
    return [{"id": k, "name": v["name"]} for k, v in AGENTS.items()]


@app.get("/api/agents/{agent_id}")
async def get_agent(agent_id: str):
    if agent_id not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"id": agent_id, **AGENTS[agent_id]}


@app.post("/api/chat/{agent_id}", response_model=ChatResponse)
async def chat_with_agent(agent_id: str, request: ChatRequest):
    if agent_id not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent = AGENTS[agent_id]
    api_key = get_openai_api_key(request.api_key)

    messages = [{"role": "system", "content": agent["system_prompt"]}]

    history = request.history or []
    for msg in history[-10:]:
        messages.append({"role": msg.role, "content": msg.content})

    messages.append({"role": "user", "content": request.message})

    if not api_key:
        mock_responses = {
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
    And destination account should be credited with "1000" INR

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
        }
        
        default_response = f"""I'm the **{agent['name']}** agent.

I received your message: "{request.message}"

This is a demo response. To get real AI responses:
1. Get an OpenAI API key from https://platform.openai.com
2. Paste it in the key dialog in the UI, or set OPENAI_API_KEY in backend/.env
3. The app will automatically switch to live AI responses

How can I help you with your QA tasks today?"""

        response_text = mock_responses.get(agent_id, default_response)
        return ChatResponse(response=response_text, agent_id=agent_id)

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=get_openai_model(),
            messages=messages,
            max_tokens=2000,
            temperature=0.7
        )

        assistant_message = response.choices[0].message.content

        return ChatResponse(response=assistant_message, agent_id=agent_id)

    except Exception as e:
        error_text = str(e).lower()
        status_code = getattr(e, "status_code", None)

        if status_code in {401, 403, 429} or "insufficient_quota" in error_text or "quota" in error_text or "api key" in error_text:
            fallback_message = (
                "Live AI is currently unavailable because the OpenAI account does not have usable quota or the API key is not accepted. "
                "The app will continue in demo mode. Please check your OpenAI billing/credits or use a different API key."
            )
            return ChatResponse(response=fallback_message, agent_id=agent_id)

        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
