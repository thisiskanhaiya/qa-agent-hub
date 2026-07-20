import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useApiKeyStore = defineStore('apiKey', () => {
  const apiKey = ref(localStorage.getItem('openai_api_key') || '')

  const hasApiKey = computed(() => !!apiKey.value && apiKey.value.startsWith('sk-'))

  const setApiKey = (key) => {
    apiKey.value = key
    localStorage.setItem('openai_api_key', key)
  }

  const clearApiKey = () => {
    apiKey.value = ''
    localStorage.removeItem('openai_api_key')
  }

  return {
    apiKey,
    hasApiKey,
    setApiKey,
    clearApiKey
  }
})
