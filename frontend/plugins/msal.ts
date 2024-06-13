import {useMSAuth} from "~/composables/useMSAuth";

export default defineNuxtPlugin(async ({ $config }) => {
  const msAuth = useMSAuth();

  try {
    await msAuth.initialize();
    // Logging for debugging
    console.log('MSAL instance initialized in plugin')
  } catch (error) {
    console.error(error);
  }

  return {};
});