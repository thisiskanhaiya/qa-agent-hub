import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import AgentChat from '../views/AgentChat.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/agent/:id',
    name: 'AgentChat',
    component: AgentChat,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
