<template>
    <div class="tw-font-noto">
        <h2 class="tw-text-xl tw-bg-clip-text tw-text-center tw-mt-4">
            Please log in to continue
        </h2>

        <div class="tw-relative tw-px-6 tw-lg-px-8">
            <div class="tw-mt-10 tw-flex tw-items-center tw-justify-center tw-gap-x-6">

                <button type="submit" class="btn btn-secondary" @click="login">
                    <span>Login with Indorama Ventures email</span>
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useMSAuth } from "~/composables/useMSAuth";
const config = useRuntimeConfig();

const msAuth = useMSAuth();

async function login() {
    await msAuth.signIn()
}
</script>
