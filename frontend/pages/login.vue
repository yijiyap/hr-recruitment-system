<template>
    <div class="">
        <h2
            class="tw-text-xl tw-bg-clip-text tw-text-center tw-mt-4">
            Please log in to continue
        </h2>

        <div class="tw-relative tw-px-6 tw-lg-px-8">
            <div class="tw-isolate">
                <div class="tw-relative tw-px-6 tw-lg-px-8">
                    <div class="tw-mx-auto tw-max-w-2xl tw-py-16 tw-sm-py-40 tw-lg-py-41">
                        <div class="tw-text-center tw-flex tw-flex-col tw-justify-center tw-items-center">
                            <img src="https://i.ibb.co/y6ZvhjC/Microsoft-logo-svg.png"
                                class="tw-h-24 tw-w-24 tw-ring-4 tw-ring-blue-200 tw-sm-h-32 tw-sm-w-32 tw-object-cover tw-hover-opacity-75 tw-transition-all tw-duration-300" />
                            <h1 class="tw-text-4xl tw-font-bold tw-tracking-tight tw-text-gray-900 tw-sm-text-6xl" />
                            <div class="tw-mt-10 tw-flex tw-items-center tw-justify-center tw-gap-x-6">

                                <button type="submit"
                                    class="btn btn-secondary"
                                    @click="login">
                                    <span>Login with Microsoft 365</span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import {useMSAuth} from "~/composables/useMSAuth";

const msAuth = useMSAuth();

async function login() {
    await msAuth.signIn()
}
</script>
