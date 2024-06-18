<template>
  <div class="tw-font-noto">
    <div class="text-center">
        Hi!
    </div>
    <div
        class="col-span-1 tw-justify-center container tw-mx-auto tw-flex tw-flex-col tw-text-center tw-bg-white tw-rounded-lg tw-shadow tw-divide-y tw-divide-gray-200 tw-max-w-sm tw-mt-5">
        <div class="tw-flex-1 tw-flex tw-flex-col tw-p-8 tw-relative">

            <div v-if="profileImage">
                <img class="tw-w-32 tw-h-32 tw-flex-shrink-0 tw-mx-auto tw-rounded-full tw-ring-4 tw-ring-green-300" :src="profileImage" alt="">
            </div>
            <div
v-else
                class="tw-justify-center tw-items-center tw-flex tw-mx-auto tw-text-gray-600 tw-font-semibold tw-w-32 tw-h-32 tw-rounded-full tw-bg-blue-200 tw-uppercase :hover:tw-bg-gray-300">
                {{ userStore.user.name?.match(/[A-Z]/g).join("") }}
            </div>

            <h3 class="tw-mt-6 tw-text-gray-900 tw-text-sm tw-font-medium">{{ userStore.user.name }}</h3>
            <dl class="tw-mt-1 tw-flex-grow tw-flex tw-flex-col tw-justify-between">
                <dt class="tw-sr-only">Name</dt>
                <dd class="tw-text-gray-500 tw-text-sm">{{ userStore.user.username }}</dd>
                <dt class="tw-sr-only">Email</dt>
            </dl>
            <button class="btn btn-secondary"
                @click="logout(userStore.user.homeAccountId)" type="submit">Logout
            </button>
        </div>

    </div>
  </div>
</template>

<script setup>
import { useMSAuth } from "~/composables/useMSAuth";
import { useAppUser } from "~/composables/useAppUser";

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
