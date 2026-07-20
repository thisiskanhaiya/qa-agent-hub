<template>
  <v-dialog v-model="dialog" max-width="500">
    <template #activator="{ props }">
      <v-btn 
        v-bind="props" 
        icon 
        variant="text" 
        color="white"
        :title="hasApiKey ? 'API Key Connected' : 'Add API Key'"
      >
        <v-icon :color="hasApiKey ? 'success' : 'white'">
          {{ hasApiKey ? 'mdi-key-check' : 'mdi-key-plus' }}
        </v-icon>
      </v-btn>
    </template>

    <v-card>
      <v-card-title class="d-flex align-center">
        <v-icon class="mr-2">mdi-key</v-icon>
        OpenAI API Key
      </v-card-title>

      <v-card-text>
        <v-alert 
          v-if="!hasApiKey" 
          type="info" 
          variant="tonal" 
          class="mb-4"
        >
          Add your OpenAI API key to get real AI responses. Without it, you'll see demo responses.
        </v-alert>

        <v-alert 
          v-else 
          type="success" 
          variant="tonal" 
          class="mb-4"
        >
          API Key is configured. Agents will use real AI responses.
        </v-alert>

        <v-text-field
          v-model="apiKey"
          :type="showKey ? 'text' : 'password'"
          label="OpenAI API Key"
          placeholder="sk-..."
          variant="outlined"
          :append-inner-icon="showKey ? 'mdi-eye-off' : 'mdi-eye'"
          @click:append-inner="showKey = !showKey"
          hint="Get your key from platform.openai.com"
          persistent-hint
        />

        <v-expand-transition>
          <div v-if="!hasApiKey" class="mt-4">
            <p class="text-body-2 text-grey-darken-1 mb-2">
              <strong>How to get an API key:</strong>
            </p>
            <ol class="text-body-2 text-grey-darken-1">
              <li>Go to <a href="https://platform.openai.com" target="_blank">platform.openai.com</a></li>
              <li>Sign up or log in</li>
              <li>Navigate to API Keys section</li>
              <li>Create a new secret key</li>
              <li>Copy and paste it here</li>
            </ol>
          </div>
        </v-expand-transition>
      </v-card-text>

      <v-card-actions>
        <v-btn 
          v-if="hasApiKey" 
          color="error" 
          variant="text"
          @click="removeKey"
        >
          Remove Key
        </v-btn>
        <v-spacer />
        <v-btn variant="text" @click="dialog = false">Cancel</v-btn>
        <v-btn 
          color="primary" 
          variant="flat"
          :disabled="!apiKey.trim()"
          @click="saveKey"
        >
          Save Key
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useApiKeyStore } from '../stores/apiKey'

const apiKeyStore = useApiKeyStore()

const dialog = ref(false)
const apiKey = ref('')
const showKey = ref(false)

const hasApiKey = computed(() => apiKeyStore.hasApiKey)

onMounted(() => {
  apiKey.value = apiKeyStore.apiKey || ''
})

const saveKey = () => {
  apiKeyStore.setApiKey(apiKey.value.trim())
  dialog.value = false
}

const removeKey = () => {
  apiKeyStore.clearApiKey()
  apiKey.value = ''
}
</script>
