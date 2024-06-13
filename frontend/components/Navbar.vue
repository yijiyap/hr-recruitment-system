<template>
  <nav :class="[
    'navbar sticky-top navbar-expand-lg bg-body-tertiary p-4',
    { 'scrolled': !view.atTopOfPage },
  ]">
    <div class="container-fluid">
      <NuxtLink to="/">
        <img src="/ivl_logo.png" alt="IVL Logo" width="80%" />
      </NuxtLink>
      <h1 class="tw-text-2xl tw-font-bold tw-text-center mt-2">
        Internship Recruitment System
      </h1>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown"
        aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page">
              <NuxtLink to="/demand" style="text-decoration: none; color: inherit">Hire an intern</NuxtLink>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link">
              <NuxtLink to="/parents" style="text-decoration: none; color: inherit">Hire a child</NuxtLink>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Donation</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { onBeforeMount, onUnmounted } from 'vue';

// Define reactive property for tracking scroll state
const view = reactive({
  atTopOfPage: true,
});

// Function to handle scroll event
const handleScroll = () => {
  view.atTopOfPage = window.pageYOffset === 0;
};

// Add scroll event listener on mount and remove it on unmount
onBeforeMount(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style>
/* Custom styles for the navbar */
nav.scrolled {
  @apply tw-shadow-xl;
  border-bottom: 0px;
  transition: background-color 3s ease-out;
}
</style>