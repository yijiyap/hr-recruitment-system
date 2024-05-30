<template>
  <div>
    <h1 class="tw-text-3xl tw-font-bold tw-underline tw-text-center">
      Indorama Ventures HR Internship Recruitment System
    </h1>

    <h2 class="tw-text-2xl tw-font-bold tw-text-center tw-mt-5">
      2. Confirm the role information
    </h2>

    <div class="container-fluid m-3">
      <div class="row bg-light p-3 m-3">
        <div class="col text-center">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">General details</h3>
          Department: HRHO <br />
          Supervisor: Uklit <br />
          Supervisor email: uklit.t@indorama.net <br />
        </div>
        <div class="col text-center">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">Internship Role Details</h3>
          Role 1: HR Intern<br />
          Internship Period: May 2025 - Aug 2025 <br />
        </div>
      </div>

      <div class="row bg-light p-3 m-3">
        <div class="col">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">Role Description</h3>

          <h4 class="tw-text-lg tw-font-bold">Primary Responsibilities</h4>
          <p>Assist with recruitment processes, including posting job ads, screening resumes and scheduling interviews.</p>

          <h4 class="tw-text-lg tw-font-bold">Project Description</h4>
          <p>Work on updating employee handbook and assist in organizing the annual employee engagement survey.</p>
        </div>
      </div>

      <div class="row bg-light p-3 m-3">
        <div class="col">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">Skills and Qualifications</h3>

          <h4 class="tw-text-lg tw-font-bold">Required skills:</h4>
          <p>Strong communication skills, attention to detail, proficiency in Microsoft Office Suite.</p>

          <h4 class="tw-text-lg tw-font-bold">Preferred skills:</h4>
          <p>Familiarity with HR software (JobsDB, LinkedIn, SAP SuccessFactors), basic knowledge of labour laws.</p>

          <h4 class="tw-text-lg tw-font-bold">Education level:</h4>
          <p>Currently pursuing a degree in Human Resources, Business Administration, or a related field.</p>
        </div>
      </div>

      <div class="row bg-light p-3 m-3">
        <div class="col">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">Additional Information</h3>

          <h4 class="tw-text-lg tw-font-bold">Others:</h4>
          <p>Previous internship experience in a Human Resources Internship is preferred.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, useAttrs } from 'vue';
const route = useRoute();

onMounted(() => {
    console.log(route.query.roleId);

    // Fetch role info from API

});


</script>