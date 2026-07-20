from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI(
    title="QA Agent Hub API",
    description="Backend API for Quality Engineering Dashboard",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    history: Optional[List[Message]] = []


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
    
    messages = [{"role": "system", "content": agent["system_prompt"]}]
    
    for msg in request.history[-10:]:
        messages.append({"role": msg.role, "content": msg.content})
    
    messages.append({"role": "user", "content": request.message})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=2000,
            temperature=0.7
        )
        
        assistant_message = response.choices[0].message.content
        
        return ChatResponse(response=assistant_message, agent_id=agent_id)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
