<template>
  <div>
    <h2 class="tw-text-2xl tw-font-bold tw-text-center tw-mt-5">
      2. Confirm the role information
    </h2>

    <div class="container-fluid m-3">
      <div class="row bg-light p-3 m-3">
        <div class="col text-center">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">
            Supervisor details
          </h3>
          Department: {{ roleToHire.supervisorDetails.department }} <br />
          Supervisor: {{ roleToHire.supervisorDetails.supervisor }} <br />
          Supervisor email: {{ roleToHire.supervisorDetails.supervisorEmail }}
          <br />
        </div>
        <div class="col text-center">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">
            Internship Role Details
          </h3>
          Role {{ roleToHire.internshipRoleDetails.roleId }}:
          {{ roleToHire.internshipRoleDetails.roleName }}<br />
          Internship Period:
          {{ roleToHire.internshipRoleDetails.internshipPeriod }} <br />
        </div>
      </div>

      <div class="row bg-light p-3 m-3">
        <div class="col">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">
            Role Description
          </h3>

          <div v-if="isEditingRoleDescription">
            <h4 class="tw-text-lg tw-font-bold">Primary Responsibilities</h4>
            <textarea
              v-model="roleToHire.roleDescription.primaryResponsibilities"
            />

            <h4 class="tw-text-lg tw-font-bold">Project Description</h4>
            <textarea
              v-model="roleToHire.roleDescription.projectDescription"
            />
          </div>

          <div v-else>
            <h4 class="tw-text-lg tw-font-bold">Primary Responsibilities</h4>
            <p>
              {{ roleToHire.roleDescription.primaryResponsibilities }}
            </p>

            <h4 class="tw-text-lg tw-font-bold">Project Description</h4>
            <p>
              {{ roleToHire.roleDescription.projectDescription }}
            </p>
          </div>
        </div>
        <div>
          <div class="tw-flex tw-justify-end tw-mr-5">
            <button class="btn btn-secondary" @click="toggleEditMode(true)">
              {{ buttonSkills }}
            </button>
          </div>
        </div>
      </div>

      <div class="row bg-light p-3 m-3">
        <div class="col">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">
            Skills and Qualifications
          </h3>

          <h4 class="tw-text-lg tw-font-bold">Required skills:</h4>
          <p>
            {{ roleToHire.skillsAndQualifications.requiredSkills }}
          </p>

          <h4 class="tw-text-lg tw-font-bold">Preferred skills:</h4>
          <p>
            {{ roleToHire.skillsAndQualifications.preferredSkills }}
          </p>

          <h4 class="tw-text-lg tw-font-bold">Education level:</h4>
          <p>
            {{ roleToHire.skillsAndQualifications.educationLevel }}
          </p>

          <div class="tw-flex tw-justify-end tw-mr-5">
            <button class="btn btn-secondary">Edit</button>
          </div>
        </div>
      </div>

      <div class="row bg-light p-3 m-3">
        <div class="col">
          <h3 class="tw-text-xl tw-font-bold tw-text-center">
            Additional Information
          </h3>

          <h4 class="tw-text-lg tw-font-bold">Others:</h4>
          <p>
            {{ roleToHire.additionalInformation.others }}
          </p>
          <div class="tw-flex tw-justify-end tw-mr-5">
            <button class="btn btn-secondary">Edit</button>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="tw-flex tw-justify-center mt-3">
            <button class="btn btn-secondary"><NuxtLink to="/shortlistedCVs" style="text-decoration: none; color: inherit">Get relevant CVs</NuxtLink></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, useAttrs } from "vue";
const route = useRoute();

onMounted(() => {
  console.log(route.query.roleId);

  // Fetch role info from API
});

const roleToHire = {
  supervisorDetails: {
    department: "HRHO",
    supervisor: "Uklit",
    supervisorEmail: "test@test.com",
  },
  internshipRoleDetails: {
    roleId: "123",
    roleName: "HR Intern",
    internshipPeriod: "May 2025 - Aug 2025",
  },
  roleDescription: {
    primaryResponsibilities:
      "Assist with recruitment processes, including posting job ads, screening resumes and scheduling interviews.",
    projectDescription:
      "Work on updating employee handbook and assist in organizing the annual employee engagement survey.",
  },
  skillsAndQualifications: {
    requiredSkills:
      "Strong communication skills, attention to detail, proficiency in Microsoft Office Suite.",
    preferredSkills:
      "Familiarity with HR software (JobsDB, LinkedIn, SAP SuccessFactors), basic knowledge of labour laws.",
    educationLevel:
      "Currently pursuing a degree in Human Resources, Business Administration, or a related field.",
  },
  additionalInformation: {
    others:
      "Previous internship experience in a Human Resources Internship is preferred.",
  },
};

async function editProjectDescription() {
  console.log("Editing project description");
}

const isEditingRoleDescription = ref(false);
let buttonSkills = "Edit";

async function toggleEditMode() {
  if (!isEditingRoleDescription.value) {
    isEditingRoleDescription.value = true;
    buttonSkills = "Save";
  } else {
    // Save changes
    isEditingRoleDescription.value = false;
    buttonSkills = "Edit";
  }
  return buttonSkills;
}
</script>

<style scoped>
textarea {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  width: 100%;
  height: 100px;
  background-color: transparent;
  color: #000
}
</style>