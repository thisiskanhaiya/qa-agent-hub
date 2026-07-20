<template>
  <v-container fluid class="pa-6 bg-background">
    <v-row>
      <v-col cols="12">
        <div class="text-center mb-8">
          <h1 class="text-h4 font-weight-bold text-primary mb-2">
            Welcome to Quality Engineering Dashboard
          </h1>
          <p class="text-subtitle-1 text-grey-darken-1">
            Select an AI agent to assist with your QA tasks
          </p>
        </div>
      </v-col>
    </v-row>

    <div v-for="category in categories" :key="category" class="mb-8">
      <v-row>
        <v-col cols="12">
          <div class="d-flex align-center mb-4">
            <v-icon :color="getCategoryColor(category)" class="mr-2">
              {{ getCategoryIcon(category) }}
            </v-icon>
            <h2 class="text-h5 font-weight-medium">{{ category }}</h2>
            <v-chip 
              :color="getCategoryColor(category)" 
              size="small" 
              class="ml-3"
              variant="tonal"
            >
              {{ getAgentsByCategory(category).length }} agents
            </v-chip>
          </div>
        </v-col>
      </v-row>
      
      <v-row>
        <v-col
          v-for="agent in getAgentsByCategory(category)"
          :key="agent.id"
          cols="12"
          sm="6"
          md="4"
          lg="3"
        >
          <AgentCard :agent="agent" />
        </v-col>
      </v-row>
      
      <v-divider v-if="category !== categories[categories.length - 1]" class="mt-6" />
    </div>
  </v-container>
</template>

<script setup>
import { computed } from 'vue'
import { useAgentStore } from '../stores/agents'
import AgentCard from '../components/AgentCard.vue'

const agentStore = useAgentStore()

const categories = computed(() => agentStore.categories)
const getAgentsByCategory = (category) => agentStore.getAgentsByCategory(category)

const getCategoryColor = (category) => {
  const colors = {
    'Junior QA': 'success',
    'Senior QA': 'info',
    'Team Lead': 'warning'
  }
  return colors[category] || 'primary'
}

const getCategoryIcon = (category) => {
  const icons = {
    'Junior QA': 'mdi-school',
    'Senior QA': 'mdi-code-braces',
    'Team Lead': 'mdi-account-tie'
  }
  return icons[category] || 'mdi-robot'
}
</script>
