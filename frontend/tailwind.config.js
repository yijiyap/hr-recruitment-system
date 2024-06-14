/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');

export default {
  prefix: "tw-",
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    fontFamily: {
      'sans': ['Noto Sans', ...defaultTheme.fontFamily.sans],
      'noto': ['Noto Sans', ...defaultTheme.fontFamily.sans],
      'test': ['Tilt Prism', 'sans-serif'],
    },
  },
  corePlugins: {
    preflight: false,
  },
  plugins: [],
}

