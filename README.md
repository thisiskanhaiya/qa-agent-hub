# 🤖 QA Agent Hub

**AI-Powered Quality Engineering Assistant for Banking & Financial Services**

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://qa-agent-hub.vercel.app)
[![Backend](https://img.shields.io/badge/backend-render-blue)](https://qa-agent-hub.onrender.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

QA Agent Hub is an intelligent quality engineering platform that leverages OpenAI's GPT-4o-mini to assist QA professionals in their daily tasks. Built specifically for the banking and financial services domain, it provides 12 specialized AI agents for Junior QA, Senior QA, and Team Lead roles.

## ✨ Features

- 🤖 **12 Specialized AI Agents** - Trained for specific QA tasks from junior to team lead level
- 🏦 **Banking Domain Focus** - Specialized knowledge for financial services QA scenarios
- ⚡ **Real-time Responses** - Instant AI-powered answers using OpenAI GPT-4o-mini
- ☁️ **Cloud Deployed** - Backend on Render, Frontend on Vercel for 24/7 availability
- 🔑 **Flexible API Key** - Use demo mode or bring your own OpenAI API key
- 📱 **Responsive Design** - Beautiful Material Design UI that works on all devices

## 🎯 Agent Categories

### Junior QA (4 Agents)
Essential QA tasks for beginners and test execution:
- **Gherkin Converter** - Convert requirements into Gherkin format (Given/When/Then)
- **Test Case Writer** - Generate comprehensive test cases from user stories
- **Bug Reporter** - Format bug reports with standard template and severity
- **Test Data Generator** - Generate valid banking test data (accounts, transactions)

### Senior QA (4 Agents)
Advanced automation and performance testing:
- **API Test Generator** - Generate REST API test scripts from specifications
- **Automation Script Builder** - Generate Selenium/Playwright/Cypress scripts
- **SQL Query Helper** - Build SQL queries for test data setup and validation
- **Performance Test Creator** - Generate JMeter/Gatling performance test scripts

### Team Lead (4 Agents)
Strategic planning and quality governance:
- **Sprint Test Planner** - Create test plans from sprint backlog
- **Defect Triage Assistant** - Categorize and prioritize bugs efficiently
- **Coverage Analyzer** - Map test cases to requirements and identify gaps
- **Release Readiness Checker** - Go/no-go decision support and release checklists

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Frontend (Vercel)                     │
│  Vue 3 + Vuetify 3 + Pinia + Vite + Vue Router          │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ HTTPS/REST API
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   Backend (Render)                       │
│         FastAPI + Python 3.11+ + Uvicorn                │
└──────────────────────┬──────────────────────────────────┘
                       │
                       │ API Calls
                       │
┌──────────────────────▼──────────────────────────────────┐
│                    OpenAI API                            │
│                  GPT-4o-mini Model                       │
└─────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Frontend
- **Vue 3** - Progressive JavaScript framework with Composition API
- **Vuetify 3** - Material Design component framework
- **Pinia** - Intuitive state management
- **Vite** - Next generation frontend tooling
- **Vue Router** - Official routing library
- **Axios** - HTTP client for API requests

### Backend
- **FastAPI** - Modern, fast web framework for building APIs with Python
- **Python 3.11+** - Latest Python version with performance improvements
- **Uvicorn** - Lightning-fast ASGI server
- **OpenAI** - GPT-4o-mini integration
- **httpx** - Modern HTTP client with async support
- **Pydantic** - Data validation using Python type annotations

### Deployment
- **Frontend**: Vercel (Automatic deployments from main branch)
- **Backend**: Render (Web service with auto-deploy)

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- OpenAI API key (optional - demo mode available)

### Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
echo "OPENAI_API_KEY=your_openai_key_here" > .env
echo "PORT=8000" >> .env

# Run server
uvicorn main:app --reload --port 8000
```

#### Frontend Setup
```bash
cd frontend
npm install

# Create .env files
echo "VITE_API_BASE_URL=http://localhost:8000" > .env.development
echo "VITE_API_BASE_URL=https://qa-agent-hub.onrender.com" > .env.production

# Run development server
npm run dev
```

Visit `http://localhost:5173` to see the app.

## 🎨 Usage

1. **Select an Agent** - Choose from 12 specialized AI agents
2. **Add API Key (Optional)** - Use demo mode or add your OpenAI key for live AI responses
3. **Start Chatting** - Ask questions and get instant QA assistance

### Example Prompts

**For Gherkin Converter:**
```
Convert this to Gherkin: User logs into banking app, views account balance, and transfers money to another account
```

**For Test Case Writer:**
```
Generate test cases for login functionality with valid and invalid credentials
```

**For API Test Generator:**
```
Create REST Assured test for GET /api/accounts endpoint that returns list of bank accounts
```

## 📊 Use Cases

- **Test Documentation** - Generate test cases, Gherkin scenarios, and bug reports
- **Test Automation** - Create automation scripts for web, API, and performance testing
- **Test Planning** - Plan sprints, analyze coverage, and assess release readiness
- **Database Testing** - Generate SQL queries for test data setup and validation

## 🌐 Live Demo

**Frontend:** [https://qa-agent-hub.vercel.app](https://qa-agent-hub.vercel.app)

**Backend API:** [https://qa-agent-hub.onrender.com](https://qa-agent-hub.onrender.com)

Try the demo mode without an API key, or add your OpenAI key for full AI-powered responses!

## 📸 Screenshots

### Dashboard
![Dashboard](https://via.placeholder.com/800x500/667eea/ffffff?text=QA+Agent+Hub+Dashboard)

### Chat Interface
![Chat Interface](https://via.placeholder.com/800x500/764ba2/ffffff?text=Agent+Chat+Interface)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4o-mini API
- Vue.js and Vuetify teams for excellent frameworks
- FastAPI team for the amazing Python web framework

## 📧 Contact

**Project Link:** [https://github.com/thisiskanhaiya/qa-agent-hub](https://github.com/thisiskanhaiya/qa-agent-hub)

**Live Demo:** [https://qa-agent-hub.vercel.app](https://qa-agent-hub.vercel.app)

---

⭐ Star this repo if you find it helpful!

Made with ❤️ for QA Engineers
