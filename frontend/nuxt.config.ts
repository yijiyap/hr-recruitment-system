// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      clientId: process.env.CLIENT_ID,
      authority: process.env.AUTHORITY,
      redirectUri: process.env.REDIRECT_URI,
      postLogoutRedirectUri: process.env.POST_LOGOUT_REDIRECT_URI
    }
  },
  css: [
    '~/assets/css/main.css',
    'bootstrap/dist/css/bootstrap.css',
    'primevue/resources/themes/aura-light-green/theme.css'
  ],
  modules: [
    'nuxt-primevue'
  ],
  primevue: {
    /* Options */
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
})