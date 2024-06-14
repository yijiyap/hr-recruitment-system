<template>
<div
    class="tw-col-span-1 tw-justify-center tw-container tw-mx-auto tw-flex tw-flex-col tw-text-center tw-bg-white tw-rounded-lg tw-shadow tw-divide-y tw-divide-gray-200 tw-max-w-sm tw-mt-5">
    <div class="tw-flex-1 tw-flex tw-flex-col tw-p-8 tw-relative">

        <div v-if="profileImage">
            <img class="tw-w-32 tw-h-32 tw-flex-shrink-0 tw-mx-auto tw-rounded-full tw-ring-4 tw-ring-green-300" :src="profileImage" alt="">
        </div>
        <div class="tw-justify-center tw-items-center tw-flex tw-mx-auto tw-text-gray-600 tw-font-semibold tw-w-32 tw-h-32 tw-rounded-full tw-bg-blue-200 tw-uppercase :hover:tw-bg-gray-300"
            v-else>
            {{ userStore.user.name?.match(/[A-Z]/g).join("") }}
        </div>

        <h3 class="tw-mt-6 tw-text-gray-900 tw-text-sm tw-font-medium">{{ userStore.user.name }}</h3>
        <dl class="tw-mt-1 tw-flex-grow tw-flex tw-flex-col tw-justify-between">
            <dt class="sr-only">Name</dt>
            <dd class="tw-text-gray-500 tw-text-sm">{{ userStore.user.username }}</dd>
            <dt class="sr-only">Email</dt>
        </dl>
        <button @click="logout(userStore.user.homeAccountId)"
            class="tw-absolute tw-bottom-0 tw-right-0 tw-mr-2 tw-mb-2 tw-bg-gray-100 tw-p-2 tw-rounded-lg tw-shadow hover:tw-bg-red-500 tw-text-gray-500 hover:tw-text-white hover:tw-opacity-60 tw-transition-all tw-duration-500 tw-font-extrabold tw-font-mono">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="tw-w-6 tw-h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5.636 5.636a9 9 0 1012.728 0M12 3v9" />
            </svg>
        </button>
    </div>
    <div class="tw-absolute tw-inset-x-0 tw-top-[-10rem] -z-10 tw-transform-gpu tw-overflow-hidden tw-blur-3xl sm:tw-top-[-20rem]">
        <svg class="tw-relative tw-left-[calc(50%-11rem)] -z-10 tw-h-[21.1875rem] tw-max-w-none tw--translate-x-1/2 tw-rotate-[30deg] sm:tw-left-[calc(50%-30rem)] sm:tw-h-[42.375rem] tw-animate-pulse"
            viewBox="0 0 1155 678">
            <path fill="url(#45de2b6b-92d5-4d68-a6a0-9b9b2abad533)" fill-opacity=".3"
                d="M317.219 518.975L203.852 678 0 438.341l317.219 80.634 204.172-286.402c1.307 132.337 45.083 346.658 209.733 145.248C936.936 126.058 882.053-94.234 1031.02 41.331c119.18 108.451 130.68 295.337 121.53 375.223L855 299l21.173 362.054-558.954-142.079z" />
            <defs>
                <linearGradient id="45de2b6b-92d5-4d68-a6a0-9b9b2abad533" x1="1155.49" x2="-78.208" y1=".177"
                    y2="474.645" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#38bdf8" />
                    <stop offset="1" stop-color="#f472b6" />
                </linearGradient>
            </defs>
        </svg>
    </div>
</div>

</template>

<script setup>
import {useMSAuth} from "~/composables/useMSAuth";
import {useAppUser} from "~/composables/useAppUser";

const userStore = useAppUser();
const msAuth = useMSAuth();
const isAuthenticated = msAuth.isAuthenticated();

const profileImage = ref("");

async function logout(accountId) {
    if (accountId) {
        await msAuth.signOut(accountId);
    } else {
        console.log("No account ID found")
    }
}

const getProfileImage = async () => {
    const accessToken = await msAuth.acquireTokenSilent({
        scopes: ["User.Read"],
    });
    const response = await fetch(
        "https://graph.microsoft.com/v1.0/me/photo/$value",
        {
            headers: {
                Authorization: `Bearer ${accessToken}`,
            },
        }
    );
    if (response.status != 404) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        return url;
    }
};

onMounted(async () => {
    if (isAuthenticated) {
        profileImage.value = await getProfileImage();
        userStore.value.userImage = profileImage.value;
    }
});

</script>
