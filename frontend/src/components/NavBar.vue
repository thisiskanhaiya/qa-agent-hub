<template>
  <v-app-bar color="primary" elevation="2">
    <v-app-bar-nav-icon @click="goHome">
      <v-icon>mdi-shield-check</v-icon>
    </v-app-bar-nav-icon>
    
    <v-app-bar-title class="text-h5 font-weight-bold">
      Quality Engineering Dashboard
    </v-app-bar-title>
    
    <v-spacer />

    <v-chip 
      :color="hasApiKey ? 'success' : 'warning'" 
      variant="flat"
      class="mr-2"
      size="small"
    >
      <v-icon start size="small">{{ hasApiKey ? 'mdi-check-circle' : 'mdi-alert-circle' }}</v-icon>
      {{ hasApiKey ? 'AI Connected' : 'Demo Mode' }}
    </v-chip>
    
    <v-chip color="secondary" class="mr-2">
      <v-icon start>mdi-robot</v-icon>
      {{ agentCount }} Agents
    </v-chip>

    <ApiKeyDialog />
    
    <v-btn icon>
      <v-avatar color="secondary" size="36">
        <v-icon>mdi-account</v-icon>
      </v-avatar>
    </v-btn>
  </v-app-bar>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAgentStore } from '../stores/agents'
import { useApiKeyStore } from '../stores/apiKey'
import ApiKeyDialog from './ApiKeyDialog.vue'

const router = useRouter()
const agentStore = useAgentStore()
const apiKeyStore = useApiKeyStore()

const agentCount = computed(() => agentStore.agents.length)
const hasApiKey = computed(() => apiKeyStore.hasApiKey)

const goHome = () => {
  router.push('/')
}
</script>
