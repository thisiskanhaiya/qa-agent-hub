import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const customTheme = {
  dark: false,
  colors: {
    primary: '#1E3A5F',
    secondary: '#3498DB',
    accent: '#27AE60',
    background: '#F5F7FA',
    surface: '#FFFFFF',
    error: '#E74C3C',
    warning: '#F39C12',
    info: '#3498DB',
    success: '#27AE60'
  }
}

export default createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: 'customTheme',
    themes: {
      customTheme
    }
  }
})
