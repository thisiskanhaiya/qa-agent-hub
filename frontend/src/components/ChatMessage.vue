<template>
  <div :class="['message', message.role]">
    <v-avatar
      :color="message.role === 'user' ? 'secondary' : 'primary'"
      size="36"
      class="message-avatar"
    >
      <v-icon color="white">
        {{ message.role === 'user' ? 'mdi-account' : 'mdi-robot' }}
      </v-icon>
    </v-avatar>
    
    <div class="message-content">
      <div class="message-header">
        <span class="message-sender">
          {{ message.role === 'user' ? 'You' : 'Agent' }}
        </span>
        <span class="message-time">{{ formatTime(message.timestamp) }}</span>
      </div>
      
      <div class="message-body" v-html="renderMarkdown(message.content)"></div>
      
      <v-btn
        v-if="message.role === 'assistant' && hasCodeBlock"
        size="small"
        variant="text"
        color="primary"
        prepend-icon="mdi-content-copy"
        @click="copyContent"
        class="copy-btn"
      >
        Copy
      </v-btn>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { marked } from 'marked'

const props = defineProps({
  message: {
    type: Object,
    required: true
  }
})

const hasCodeBlock = computed(() => {
  return props.message.content.includes('```')
})

const renderMarkdown = (content) => {
  return marked(content)
}

const formatTime = (timestamp) => {
  if (!timestamp) return ''
  return new Date(timestamp).toLocaleTimeString([], { 
    hour: '2-digit', 
    minute: '2-digit' 
  })
}

const copyContent = () => {
  const codeMatch = props.message.content.match(/```[\s\S]*?\n([\s\S]*?)```/)
  const textToCopy = codeMatch ? codeMatch[1] : props.message.content
  navigator.clipboard.writeText(textToCopy)
}
</script>

<style scoped>
.message {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
  max-width: 85%;
}

.message.user {
  margin-left: auto;
  flex-direction: row-reverse;
}

.message-avatar {
  flex-shrink: 0;
}

.message-content {
  background: #f5f5f5;
  border-radius: 12px;
  padding: 12px 16px;
}

.message.user .message-content {
  background: #e3f2fd;
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.message-sender {
  font-weight: 600;
  font-size: 0.875rem;
}

.message-time {
  font-size: 0.75rem;
  color: #666;
}

.message-body {
  font-size: 0.9375rem;
  line-height: 1.5;
}

.message-body :deep(pre) {
  background: #1e1e1e;
  color: #d4d4d4;
  padding: 12px;
  border-radius: 8px;
  overflow-x: auto;
  margin: 8px 0;
}

.message-body :deep(code) {
  font-family: 'Monaco', 'Menlo', monospace;
  font-size: 0.875rem;
}

.copy-btn {
  margin-top: 8px;
}
</style>
