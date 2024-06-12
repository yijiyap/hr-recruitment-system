import {useMSAuth} from "~/auth/useMSAuth";

export default defineNuxtPlugin(async ({ $config }) => {
  const msAuth = useMSAuth();
  await msAuth.initialize();

  return {};
});