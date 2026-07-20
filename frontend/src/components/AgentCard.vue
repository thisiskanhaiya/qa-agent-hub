<template>
  <v-card
    class="agent-card"
    elevation="3"
    hover
    @click="openAgent"
  >
    <v-card-item>
      <template #prepend>
        <v-avatar :color="getCategoryColor" size="48">
          <v-icon size="28" color="white">{{ agent.icon }}</v-icon>
        </v-avatar>
      </template>
      
      <v-card-title class="text-h6">{{ agent.name }}</v-card-title>
      <v-card-subtitle>{{ agent.category }}</v-card-subtitle>
    </v-card-item>
    
    <v-card-text class="text-body-2 text-grey-darken-1">
      {{ agent.description }}
    </v-card-text>
    
    <v-card-actions>
      <v-chip size="small" :color="getCategoryColor" variant="tonal">
        {{ agent.category }}
      </v-chip>
      <v-spacer />
      <v-btn
        color="primary"
        variant="text"
        append-icon="mdi-arrow-right"
        @click.stop="openAgent"
      >
        Open
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  agent: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const getCategoryColor = computed(() => {
  const colors = {
    'Junior QA': 'success',
    'Senior QA': 'info',
    'Team Lead': 'warning'
  }
  return colors[props.agent.category] || 'primary'
})

const openAgent = () => {
  router.push(`/agent/${props.agent.id}`)
}
</script>

<style scoped>
.agent-card {
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.agent-card:hover {
  transform: translateY(-4px);
}
</style>
