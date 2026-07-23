<template>
  <v-container class="about-page py-8">
    <!-- Hero Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <v-card class="hero-card" elevation="4" rounded="xl">
          <v-card-text class="pa-8 text-center">
            <v-icon size="80" color="primary" class="mb-4">mdi-robot-outline</v-icon>
            <h1 class="text-h3 font-weight-bold mb-4">QA Agent Hub</h1>
            <p class="text-h6 text-grey-darken-1 mb-6">
              AI-Powered Quality Engineering Assistant
            </p>
            <v-chip-group class="justify-center">
              <v-chip color="primary" variant="flat">12 Specialized Agents</v-chip>
              <v-chip color="success" variant="flat">Banking Domain</v-chip>
              <v-chip color="info" variant="flat">OpenAI Powered</v-chip>
            </v-chip-group>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Overview Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-information-outline</v-icon>
          What is QA Agent Hub?
        </h2>
        <v-card elevation="2" rounded="lg">
          <v-card-text class="pa-6">
            <p class="text-body-1 mb-4">
              QA Agent Hub is an intelligent quality engineering platform that leverages AI to assist QA professionals 
              in their daily tasks. Built specifically for the banking and financial services domain, it provides 
              specialized agents for Junior QA, Senior QA, and Team Lead roles.
            </p>
            <p class="text-body-1">
              Each agent is trained with domain-specific knowledge to help with test case writing, automation script 
              generation, bug reporting, test planning, and much more—making your QA workflow faster and more efficient.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Key Features Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-star-outline</v-icon>
          Key Features
        </h2>
      </v-col>
      <v-col cols="12" md="4" v-for="feature in features" :key="feature.title">
        <v-card class="feature-card h-100" elevation="2" rounded="lg" hover>
          <v-card-text class="pa-6 text-center">
            <v-avatar :color="feature.color" size="60" class="mb-4">
              <v-icon size="30" color="white">{{ feature.icon }}</v-icon>
            </v-avatar>
            <h3 class="text-h6 font-weight-bold mb-3">{{ feature.title }}</h3>
            <p class="text-body-2 text-grey-darken-1">{{ feature.description }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Architecture Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-layers-outline</v-icon>
          System Architecture
        </h2>
        <v-card elevation="2" rounded="lg">
          <v-card-text class="pa-6">
            <v-row>
              <v-col cols="12" md="6">
                <div class="architecture-box mb-4">
                  <h4 class="text-h6 font-weight-bold mb-3">
                    <v-icon color="success" class="mr-2">mdi-view-dashboard-outline</v-icon>
                    Frontend
                  </h4>
                  <v-list density="compact">
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-vuejs</v-icon>
                        Vue 3 with Composition API
                      </v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-material-design</v-icon>
                        Vuetify 3 Material Design
                      </v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-state-machine</v-icon>
                        Pinia State Management
                      </v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-lightning-bolt</v-icon>
                        Vite Build Tool
                      </v-list-item-title>
                    </v-list-item>
                  </v-list>
                </div>
              </v-col>
              <v-col cols="12" md="6">
                <div class="architecture-box mb-4">
                  <h4 class="text-h6 font-weight-bold mb-3">
                    <v-icon color="warning" class="mr-2">mdi-server</v-icon>
                    Backend
                  </h4>
                  <v-list density="compact">
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-language-python</v-icon>
                        FastAPI (Python 3.11+)
                      </v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-robot</v-icon>
                        OpenAI GPT-4o-mini
                      </v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-swap-horizontal</v-icon>
                        CORS & ASGI Support
                      </v-list-item-title>
                    </v-list-item>
                    <v-list-item>
                      <v-list-item-title>
                        <v-icon size="small" class="mr-2">mdi-cloud-outline</v-icon>
                        Deployed on Render
                      </v-list-item-title>
                    </v-list-item>
                  </v-list>
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- How It Works Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-cog-outline</v-icon>
          How It Works
        </h2>
      </v-col>
      <v-col cols="12" md="3" v-for="(step, index) in workflowSteps" :key="index">
        <v-card class="workflow-card h-100" elevation="2" rounded="lg">
          <v-card-text class="pa-6 text-center">
            <v-avatar :color="step.color" size="50" class="mb-4">
              <span class="text-h5 font-weight-bold">{{ index + 1 }}</span>
            </v-avatar>
            <v-icon :color="step.color" size="40" class="mb-3">{{ step.icon }}</v-icon>
            <h4 class="text-h6 font-weight-bold mb-3">{{ step.title }}</h4>
            <p class="text-body-2 text-grey-darken-1">{{ step.description }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Agent Categories Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-account-group-outline</v-icon>
          Agent Categories
        </h2>
      </v-col>
      <v-col cols="12" md="4" v-for="category in categories" :key="category.name">
        <v-card :color="category.color" class="category-card h-100" elevation="4" rounded="lg">
          <v-card-text class="pa-6 text-white">
            <v-icon color="white" size="50" class="mb-4">{{ category.icon }}</v-icon>
            <h3 class="text-h5 font-weight-bold mb-3">{{ category.name }}</h3>
            <p class="text-body-1 mb-4">{{ category.description }}</p>
            <v-divider class="my-4 border-opacity-50"></v-divider>
            <p class="text-caption font-weight-bold mb-2">Agents:</p>
            <v-chip-group column>
              <v-chip 
                v-for="agent in category.agents" 
                :key="agent"
                size="small"
                color="white"
                variant="flat"
              >
                {{ agent }}
              </v-chip>
            </v-chip-group>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Tech Stack Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-code-tags</v-icon>
          Tech Stack
        </h2>
        <v-card elevation="2" rounded="lg">
          <v-card-text class="pa-6">
            <v-row>
              <v-col cols="6" md="3" v-for="tech in techStack" :key="tech.name">
                <div class="tech-item text-center pa-4">
                  <v-icon :color="tech.color" size="40" class="mb-2">{{ tech.icon }}</v-icon>
                  <p class="text-body-2 font-weight-bold">{{ tech.name }}</p>
                  <p class="text-caption text-grey">{{ tech.version }}</p>
                </div>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Use Cases Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-lightbulb-outline</v-icon>
          Use Cases
        </h2>
        <v-expansion-panels>
          <v-expansion-panel v-for="useCase in useCases" :key="useCase.title">
            <v-expansion-panel-title>
              <v-icon :color="useCase.color" class="mr-3">{{ useCase.icon }}</v-icon>
              <span class="font-weight-bold">{{ useCase.title }}</span>
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              <p class="text-body-1 mb-3">{{ useCase.description }}</p>
              <v-chip-group>
                <v-chip 
                  v-for="example in useCase.examples" 
                  :key="example"
                  size="small"
                  color="primary"
                  variant="outlined"
                >
                  {{ example }}
                </v-chip>
              </v-chip-group>
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>

    <!-- Getting Started Section -->
    <v-row class="mb-8">
      <v-col cols="12">
        <h2 class="text-h4 font-weight-bold mb-4">
          <v-icon color="primary" class="mr-2">mdi-rocket-launch-outline</v-icon>
          Getting Started
        </h2>
        <v-card class="getting-started-card" elevation="4" rounded="lg" color="primary">
          <v-card-text class="pa-8 text-white">
            <v-row align="center">
              <v-col cols="12" md="8">
                <h3 class="text-h5 font-weight-bold mb-4">Ready to boost your QA workflow?</h3>
                <v-list class="bg-transparent text-white">
                  <v-list-item>
                    <template v-slot:prepend>
                      <v-icon color="white">mdi-numeric-1-circle</v-icon>
                    </template>
                    <v-list-item-title class="font-weight-bold">Select an Agent</v-list-item-title>
                    <v-list-item-subtitle class="text-white text-opacity-90">
                      Choose from 12 specialized AI agents
                    </v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                    <template v-slot:prepend>
                      <v-icon color="white">mdi-numeric-2-circle</v-icon>
                    </template>
                    <v-list-item-title class="font-weight-bold">Add API Key (Optional)</v-list-item-title>
                    <v-list-item-subtitle class="text-white text-opacity-90">
                      Use demo mode or add your OpenAI key for live AI responses
                    </v-list-item-subtitle>
                  </v-list-item>
                  <v-list-item>
                    <template v-slot:prepend>
                      <v-icon color="white">mdi-numeric-3-circle</v-icon>
                    </template>
                    <v-list-item-title class="font-weight-bold">Start Chatting</v-list-item-title>
                    <v-list-item-subtitle class="text-white text-opacity-90">
                      Ask questions and get instant QA assistance
                    </v-list-item-subtitle>
                  </v-list-item>
                </v-list>
              </v-col>
              <v-col cols="12" md="4" class="text-center">
                <v-btn 
                  size="x-large" 
                  color="white" 
                  variant="flat"
                  @click="$router.push('/')"
                  rounded="lg"
                >
                  <v-icon class="mr-2">mdi-play</v-icon>
                  Try It Now
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Footer Info -->
    <v-row>
      <v-col cols="12">
        <v-card elevation="1" rounded="lg">
          <v-card-text class="pa-6 text-center">
            <v-icon color="primary" size="40" class="mb-3">mdi-github</v-icon>
            <p class="text-body-1 mb-3">
              This project is open source and built with modern web technologies.
            </p>
            <v-chip-group class="justify-center">
              <v-chip prepend-icon="mdi-license">MIT License</v-chip>
              <v-chip prepend-icon="mdi-cloud">Cloud Deployed</v-chip>
              <v-chip prepend-icon="mdi-security">Secure API Key Handling</v-chip>
            </v-chip-group>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const features = [
  {
    icon: 'mdi-robot-outline',
    color: 'primary',
    title: '12 Specialized Agents',
    description: 'AI agents trained for specific QA tasks from junior to team lead level'
  },
  {
    icon: 'mdi-bank',
    color: 'success',
    title: 'Banking Domain Focus',
    description: 'Specialized knowledge for financial services and banking QA scenarios'
  },
  {
    icon: 'mdi-lightning-bolt',
    color: 'warning',
    title: 'Real-time Responses',
    description: 'Instant AI-powered answers using OpenAI GPT-4o-mini model'
  },
  {
    icon: 'mdi-cloud-outline',
    color: 'info',
    title: 'Cloud Deployed',
    description: 'Backend on Render, Frontend on Vercel for reliable 24/7 availability'
  },
  {
    icon: 'mdi-key-variant',
    color: 'purple',
    title: 'Flexible API Key',
    description: 'Use demo mode or bring your own OpenAI API key for unlimited usage'
  },
  {
    icon: 'mdi-responsive',
    color: 'teal',
    title: 'Responsive Design',
    description: 'Beautiful Material Design UI that works on all devices'
  }
]

const workflowSteps = [
  {
    icon: 'mdi-account-circle',
    color: 'primary',
    title: 'Choose Agent',
    description: 'Select from Junior QA, Senior QA, or Team Lead agents'
  },
  {
    icon: 'mdi-message-text',
    color: 'success',
    title: 'Ask Question',
    description: 'Type your QA-related question or requirement'
  },
  {
    icon: 'mdi-brain',
    color: 'warning',
    title: 'AI Processing',
    description: 'Agent processes with domain-specific knowledge'
  },
  {
    icon: 'mdi-check-circle',
    color: 'info',
    title: 'Get Result',
    description: 'Receive detailed, actionable QA deliverables'
  }
]

const categories = [
  {
    name: 'Junior QA',
    icon: 'mdi-school',
    color: 'success',
    description: 'Essential QA tasks for beginners and test execution',
    agents: ['Gherkin Converter', 'Test Case Writer', 'Bug Reporter', 'Test Data Generator']
  },
  {
    name: 'Senior QA',
    icon: 'mdi-shield-check',
    color: 'info',
    description: 'Advanced automation and performance testing',
    agents: ['API Test Generator', 'Automation Builder', 'SQL Helper', 'Performance Tester']
  },
  {
    name: 'Team Lead',
    icon: 'mdi-account-tie',
    color: 'warning',
    description: 'Strategic planning and quality governance',
    agents: ['Sprint Planner', 'Defect Triage', 'Coverage Analyzer', 'Release Checker']
  }
]

const techStack = [
  { name: 'Vue 3', version: '3.4+', icon: 'mdi-vuejs', color: 'success' },
  { name: 'Vuetify', version: '3.5+', icon: 'mdi-material-design', color: 'info' },
  { name: 'Vite', version: '5.1+', icon: 'mdi-lightning-bolt', color: 'warning' },
  { name: 'Pinia', version: '2.1+', icon: 'mdi-state-machine', color: 'purple' },
  { name: 'FastAPI', version: 'Latest', icon: 'mdi-api', color: 'teal' },
  { name: 'Python', version: '3.11+', icon: 'mdi-language-python', color: 'primary' },
  { name: 'OpenAI', version: 'GPT-4o', icon: 'mdi-robot', color: 'deep-purple' },
  { name: 'Axios', version: 'Latest', icon: 'mdi-axios', color: 'blue-grey' }
]

const useCases = [
  {
    title: 'Test Documentation',
    icon: 'mdi-file-document',
    color: 'primary',
    description: 'Generate comprehensive test cases, Gherkin scenarios, and bug reports with proper formatting',
    examples: ['BDD Scenarios', 'Test Case Templates', 'Bug Report Format', 'Test Data Sets']
  },
  {
    title: 'Test Automation',
    icon: 'mdi-robot',
    color: 'success',
    description: 'Create automation scripts for web, API, and performance testing',
    examples: ['Selenium Scripts', 'API Tests', 'JMeter Scripts', 'Playwright Code']
  },
  {
    title: 'Test Planning',
    icon: 'mdi-calendar-check',
    color: 'warning',
    description: 'Plan sprints, analyze coverage, and assess release readiness',
    examples: ['Sprint Test Plans', 'Coverage Reports', 'Risk Assessment', 'Release Checklists']
  },
  {
    title: 'Database Testing',
    icon: 'mdi-database',
    color: 'info',
    description: 'Generate SQL queries for test data setup and validation',
    examples: ['INSERT Queries', 'SELECT Validations', 'UPDATE Scripts', 'JOIN Operations']
  }
]
</script>

<style scoped>
.about-page {
  max-width: 1400px;
  margin: 0 auto;
}

.hero-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.hero-card .v-icon {
  color: white !important;
}

.feature-card {
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
}

.workflow-card {
  border-top: 4px solid;
}

.category-card {
  transition: transform 0.3s ease;
}

.category-card:hover {
  transform: scale(1.02);
}

.tech-item {
  transition: all 0.3s ease;
  border-radius: 8px;
}

.tech-item:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.getting-started-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.architecture-box {
  padding: 16px;
  border-radius: 8px;
  background-color: rgba(0, 0, 0, 0.02);
}
</style>
