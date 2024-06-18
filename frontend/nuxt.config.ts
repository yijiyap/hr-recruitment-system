// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      link: [
        {
          rel: 'stylesheet',
          href: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css'
        },
      ],
      script: [
        {
          src: 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js',
          tagPosition: 'bodyClose'
        }
      ]
    }
  },
  ssr: false,
  plugins: [{ src: "~/plugins/msal.ts", mode: "client" }],
  runtimeConfig: {
    public: {
      clientId: process.env.CLIENTID,
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
  modules: ['nuxt-primevue', '@nuxt/eslint', "@nuxtjs/google-fonts"],
  primevue: {
    /* Options */
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  googleFonts: {
    families: {
      'Noto+Sans': [400, 700],
    }
  }
})