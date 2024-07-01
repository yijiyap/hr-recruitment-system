<template>
  <div class="tw-font-noto">
    <Header header-text="1. Choose role to hire" />
    <!-- List of roles to hire in bootstrap cards -->
    <div class="container">
      <div class="row tw-mb-5 mt-3">
        Sort by
        <select v-model="selectedFilter" class="form-select">
          <option v-for="filter in filters" :key="filter.value" :value="filter">{{ filter.name }}</option>
        </select>
      </div>
    
      <!-- START OF NEW DEMAND SURVEY PAGE -->
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div v-for="(role, roleId) in filteredRoles2" :key="roleId" class="col-md-3 d-flex">
          <div class="card h-100 flex-fill">
            <div class="card-body d-flex flex-column">
              <h5 class="card-title">Role to hire: {{ role.supervisor_details.department }} Intern</h5>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">Department: {{ role.supervisor_details.department }}</li>
                <li class="list-group-item">Supervisor: {{ role.supervisor_details.supervisorName }}</li>
                <li class="list-group-item">
                  Expected Internship Period: <br>{{
                    role.internship_details.preferredInternshipResource
                  }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <!-- END OF NEW DEMAND SURVEY PAGE -->
    </div>
  </div>
</template>

<script setup>
const { data: rolesToHire2 } = await useFetch("http://localhost:5003/all", {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
  },
})

console.log(rolesToHire2.value);

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

const selectedFilter = ref(filters[0]);

// computed property
const filteredRoles2 = computed(() => {
  if (rolesToHire2.value) {
    return rolesToHire2.value.sort((a, b) => {
      if (selectedFilter.value.value === "department") {
        return a.supervisor_details.department.localeCompare(b.supervisor_details.department);
      } else if (selectedFilter.value.value === "expectedInternshipPeriod") {
        return a.internship_details.preferredInternshipResource.localeCompare(
          b.internship_details.preferredInternshipResource
        );
      }
    });
  }
})

</script>
