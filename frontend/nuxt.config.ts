// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: [
    '~/assets/css/main.css',
    'bootstrap/dist/css/bootstrap.css',
    'primevue/resources/themes/aura-light-noir/theme.css',
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