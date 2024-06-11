<template>
  <div>

    <Header headerText="1. Choose role to hire" />

    <FloatLabel class="">
        <Dropdown v-model="selectedFilter" inputId="dd-filters" :options="filters" optionLabel="name" class="w-full" />
        <label for="dd-filters">Sort by</label>
    </FloatLabel>    

    <!-- List of roles to hire in bootstrap cards -->
    <div class="container">
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div v-for="(role, roleId) in filteredRoles" :key="roleId" class="col-md-3">
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
              <button @click="redirectToRoleInfo(role.roleId)" class="btn btn-secondary text-center stretched-link">
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
    roleId: "127",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Pao",
    expectedInternshipPeriod: "May 2025 - August 2025",
  },
  role6: {
    roleId: "128",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Oom",
    expectedInternshipPeriod: "May 2025 - August 2025",
  },
  role7: {
    roleId: "129",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Susie",
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

const filters = [
  { name: "Department", value: "department" },
  { name: "Expected Internship Period", value: "expectedInternshipPeriod" },
];

let selectedFilter = ref(filters[0]);
const rolesArray = Object.values(rolesToHire);
const filteredRoles = computed(() => {
  return rolesArray.sort((a, b) => {
    if (selectedFilter.value.value === "department") {
      return a.department.localeCompare(b.department);
    } else if (selectedFilter.value.value === "expectedInternshipPeriod") {
      return a.expectedInternshipPeriod.localeCompare(b.expectedInternshipPeriod);
    }
  });
});



</script>
