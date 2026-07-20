<template>
  <v-app-bar color="primary" elevation="2">
    <v-app-bar-nav-icon @click="goHome">
      <v-icon>mdi-shield-check</v-icon>
    </v-app-bar-nav-icon>
    
    <v-app-bar-title class="text-h5 font-weight-bold">
      Quality Engineering Dashboard
    </v-app-bar-title>
    
    <v-spacer />
    
    <v-chip color="secondary" class="mr-4">
      <v-icon start>mdi-robot</v-icon>
      {{ agentCount }} Agents
    </v-chip>
    
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

const router = useRouter()
const agentStore = useAgentStore()

const agentCount = computed(() => agentStore.agents.length)

const goHome = () => {
  router.push('/')
}
</script>
