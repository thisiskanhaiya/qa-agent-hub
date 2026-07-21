<template>
  <v-container fluid class="chat-container pa-0">
    <v-card class="chat-card" elevation="0">
      <!-- Agent Header -->
      <v-card-title class="chat-header bg-primary">
        <v-btn icon variant="text" color="white" @click="goBack" class="mr-2">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        
        <v-avatar :color="getCategoryColor" size="40" class="mr-3">
          <v-icon color="white">{{ agent?.icon }}</v-icon>
        </v-avatar>
        
        <div>
          <div class="text-h6 text-white">{{ agent?.name }}</div>
          <div class="text-caption text-white-50">{{ agent?.category }}</div>
        </div>
        
        <v-spacer />
        
        <v-btn 
          icon 
          variant="text" 
          color="white" 
          @click="clearChat"
          title="Clear chat"
        >
          <v-icon>mdi-delete-outline</v-icon>
        </v-btn>
      </v-card-title>

      <!-- Chat Messages -->
      <v-card-text class="chat-messages" ref="messagesContainer">
        <div v-if="messages.length === 0" class="welcome-message text-center py-8">
          <v-icon size="64" color="primary" class="mb-4">{{ agent?.icon }}</v-icon>
          <h3 class="text-h6 mb-2">{{ agent?.name }}</h3>
          <p class="text-body-2 text-grey-darken-1 mb-4">
            {{ agent?.description }}
          </p>
          <v-chip color="primary" variant="tonal">
            Type your message below to get started
          </v-chip>
        </div>

        <ChatMessage
          v-for="(message, index) in messages"
          :key="index"
          :message="message"
        />

        <div v-if="isLoading" class="loading-indicator">
          <v-progress-circular indeterminate color="primary" size="24" />
          <span class="ml-2 text-grey">Agent is thinking...</span>
        </div>
      </v-card-text>

      <!-- Input Area -->
      <v-card-actions class="chat-input-area">
        <v-textarea
          v-model="userInput"
          placeholder="Type your message..."
          rows="2"
          auto-grow
          max-rows="5"
          variant="outlined"
          density="comfortable"
          hide-details
          @keydown.enter.exact.prevent="sendMessage"
          class="chat-input"
        />
        <v-btn
          color="primary"
          icon
          size="large"
          class="ml-2"
          :disabled="!userInput.trim() || isLoading"
          @click="sendMessage"
        >
          <v-icon>mdi-send</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, computed, watch, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAgentStore } from '../stores/agents'
import { useApiKeyStore } from '../stores/apiKey'
import ChatMessage from '../components/ChatMessage.vue'
import apiClient from '../api/client'

const route = useRoute()
const router = useRouter()
const agentStore = useAgentStore()
const apiKeyStore = useApiKeyStore()

const userInput = ref('')
const isLoading = ref(false)
const messagesContainer = ref(null)

const agent = computed(() => agentStore.getAgentById(route.params.id))
const messages = computed(() => agentStore.getChatHistory(route.params.id))

const getCategoryColor = computed(() => {
  const colors = {
    'Junior QA': 'success',
    'Senior QA': 'info',
    'Team Lead': 'warning'
  }
  return colors[agent.value?.category] || 'primary'
})

const goBack = () => {
  router.push('/')
}

const clearChat = () => {
  agentStore.clearChat(route.params.id)
}

const scrollToBottom = async () => {
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

watch(messages, scrollToBottom, { deep: true })

const sendMessage = async () => {
  if (!userInput.value.trim() || isLoading.value) return

  const userMessage = userInput.value.trim()
  userInput.value = ''

  agentStore.addMessage(route.params.id, {
    role: 'user',
    content: userMessage
  })

  isLoading.value = true

  try {
    const historyPayload = messages.value
      .slice(-10)
      .map(({ role, content }) => ({ role, content }))

    const response = await apiClient.post(`/api/chat/${route.params.id}`, {
      message: userMessage,
      history: historyPayload,
      api_key: apiKeyStore.apiKey || null
    }, {
      timeout: 30000
    })

    agentStore.addMessage(route.params.id, {
      role: 'assistant',
      content: response.data?.response || 'No response received from the agent.'
    })
  } catch (error) {
    console.error('Error:', error)
    const errorMessage = error?.response?.data?.detail
      ? `The agent request failed: ${error.response.data.detail}`
      : 'Sorry, I encountered an error. Please try again.'

    agentStore.addMessage(route.params.id, {
      role: 'assistant',
      content: errorMessage
    })
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.chat-container {
  height: calc(100vh - 64px);
  display: flex;
  flex-direction: column;
}

.chat-card {
  height: 100%;
  display: flex;
  flex-direction: column;
  border-radius: 0;
}

.chat-header {
  flex-shrink: 0;
  display: flex;
  align-items: center;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
  background: #f5f7fa;
}

.welcome-message {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.loading-indicator {
  display: flex;
  align-items: center;
  padding: 16px;
}

.chat-input-area {
  flex-shrink: 0;
  padding: 16px;
  background: white;
  border-top: 1px solid #e0e0e0;
}

.chat-input {
  flex: 1;
}
</style>
