<template>
  <div>

    <Header headerText="1. Choose role to hire"/>

    <!-- Filter button at the right of the page -->
    <div class="tw-flex tw-justify-end tw-mt-5 tw-mr-5">
      <button class="btn btn-secondary">Filter</button>
    </div>

    <!-- List of roles to hire in bootstrap cards -->
    <div class="container">
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div
          v-for="(role, roleId) in rolesToHire"
          :key="roleId"
          class="col-md-3"
        >
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">Role to hire: {{ role.roleName }}</h5>
            </div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Department: {{ role.department }}</li>
              <li class="list-group-item">Supervisor: {{ role.supervisor }}</li>
              <li class="list-group-item">
                Expected Internship Period: <br />{{
                  role.expectedInternshipPeriod
                }}
              </li>
            </ul>
            <div class="card-body text-center">
              <button
                @click="redirectToRoleInfo(role.roleId)"
                class="btn btn-secondary text-center stretched-link"
              >
                Get more info
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const rolesToHire = {
  role1: {
    roleId: "123",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Uklit",
    expectedInternshipPeriod: "May 2025 - August 2025",
  },
  role2: {
    roleId: "124",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Natnisha",
    expectedInternshipPeriod: "May 2025 - August 2025",
  },
  role3: {
    roleId: "125",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Amy",
    expectedInternshipPeriod: "May 2025 - August 2025",
  },
  role4: {
    roleId: "126",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Patchy",
    expectedInternshipPeriod: "May 2025 - August 2025",
  },
  role5: {
    roleId: "126",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Pao",
    expectedInternshipPeriod: "May 2025 - August 2025",
  },
};

async function redirectToRoleInfo(roleId) {
  console.log(roleId);
  await navigateTo({
    path: "/role",
    query: {
      roleId: roleId,
    },
  });
}
</script>