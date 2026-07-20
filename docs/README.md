# QA Agent Hub - Quality Engineering Dashboard

A web-based dashboard with AI-powered agents for QA/SDET teams in the banking domain.

## Features

- **12 Specialized AI Agents** for different QA tasks
- **Role-based Organization**: Junior QA, Senior QA, Team Lead
- **Banking Domain** focused prompts and outputs
- **Real-time Chat** interface with each agent

### Available Agents

| Category | Agents |
|----------|--------|
| Junior QA | Gherkin Converter, Test Case Writer, Bug Reporter, Test Data Generator |
| Senior QA | API Test Generator, Automation Script Builder, SQL Query Helper, Performance Test Creator |
| Team Lead | Sprint Test Planner, Defect Triage Assistant, Coverage Analyzer, Release Readiness Checker |

## Tech Stack

- **Frontend**: Vue.js 3 + Vite + Vuetify
- **Backend**: Python FastAPI
- **AI**: OpenAI GPT-4o-mini

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.10+
- OpenAI API Key

### 1. Clone Repository

```bash
git clone https://github.com/thisiskanhaiya/qa-agent-hub.git
cd qa-agent-hub
```

### 2. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp ../.env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run backend
uvicorn main:app --reload --port 8000
```

### 3. Setup Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run frontend
npm run dev
```

### 4. Open Application

Visit `http://localhost:5173` in your browser.

## Deployment

### Frontend (Vercel)

1. Connect your GitHub repo to Vercel
2. Set root directory to `frontend`
3. Deploy

### Backend (Render)

1. Connect your GitHub repo to Render
2. Set root directory to `backend`
3. Add environment variable: `OPENAI_API_KEY`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Project Structure

```
qa-agent-hub/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── stores/
│   │   └── router/
│   └── package.json
├── backend/
│   ├── main.py
│   └── requirements.txt
├── .env.example
└── README.md
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | Your OpenAI API key |
| `VITE_API_BASE_URL` | Backend API URL (for frontend) |

## License

MIT

---

Built for QA teams in Banking domain
