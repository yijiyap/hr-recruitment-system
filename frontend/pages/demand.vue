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
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div v-for="(role, roleId) in filteredRoles" :key="roleId" class="col-md-3 d-flex">
          <div class="card h-100 flex-fill">
            <div class="card-body d-flex flex-column">
              <h5 class="card-title">Role to hire: {{ role.roleName }}</h5>
              <ul class="list-group list-group-flush">
                <li class="list-group-item">Department: {{ role.department }}</li>
                <li class="list-group-item">Supervisor: {{ role.supervisor }}</li>
                <li class="list-group-item">
                  Expected Internship Period: <br>{{
                    role.expectedInternshipPeriod
                  }}
                </li>
              </ul>
            </div>
            <div class="card-footer text-center">
              <button class="btn btn-secondary text-center stretched-link w-100"
                @click="redirectToRoleInfo(role.roleId)">
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
    expectedInternshipPeriod: "First half of the year",
  },
  role2: {
    roleId: "124",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Natnisha",
    expectedInternshipPeriod: "First half of the year",
  },
  role3: {
    roleId: "125",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Amy",
    expectedInternshipPeriod: "Second half of the year",
  },
  role4: {
    roleId: "126",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Patchy",
    expectedInternshipPeriod: "Summer Break",
  },
  role5: {
    roleId: "127",
    roleName: "HR Intern",
    department: "HRHO",
    supervisor: "Pao",
    expectedInternshipPeriod: "Summer Break",
  },
  role6: {
    roleId: "128",
    roleName: "Digital Intern",
    department: "Digital",
    supervisor: "Tap",
    expectedInternshipPeriod: "First half of the year",
  },
  role7: {
    roleId: "129",
    roleName: "Digital Intern",
    department: "Digital",
    supervisor: "Mat",
    expectedInternshipPeriod: "Second half of the year",
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

const selectedFilter = ref(filters[0]);
const rolesArray = Object.values(rolesToHire);

onMounted(() => {
  console.log(selectedFilter.value.name);
});


const periodToNumber = {
  "First half of the year": 1,
  "Summer Break": 2,
  "Second half of the year": 3,
};

const filteredRoles = computed(() => {
  return rolesArray.sort((a, b) => {
    if (selectedFilter.value.value === "department") {
      return a.department.localeCompare(b.department);
    } else if (selectedFilter.value.value === "expectedInternshipPeriod") {
      return periodToNumber[a.expectedInternshipPeriod] - periodToNumber[b.expectedInternshipPeriod];
    }
  });
})

/*
  Filter for when the internship period is in "Day Month Year" string format
  If the selected filter is department, sort the roles based on department
  If the selected filter is expectedInternshipPeriod, sort the roles based on the expectedInternshipPeriod
*/
// const filteredRoles = computed(() => {
//   return rolesArray.sort((a, b) => {
//     if (selectedFilter.value.value === "department") {
//       return a.department.localeCompare(b.department);
//     } else if (selectedFilter.value.value === "expectedInternshipPeriod") {

//       // convert the expectedInternshipPeriod to a date
//       const [dayStartA, monthStartA, yearStartA, endA] = a.expectedInternshipPeriod.split(" ");
//       const [dayStartB, monthStartB, yearStartB, endB] = b.expectedInternshipPeriod.split(" ");

//       const monthNames = ["January", "February", "March", "April", "May", "June",
//         "July", "August", "September", "October", "November", "December"
//       ];
//       const monthNumberA = monthNames.indexOf(monthStartA);
//       const monthNumberB = monthNames.indexOf(monthStartB);

//       // compare year, month, day
//       if (yearStartA !== yearStartB) {
//         return yearStartA - yearStartB;
//       } else if (monthNumberA !== monthNumberB) {
//         return monthNumberA - monthNumberB;
//       } else {
//         return dayStartA - dayStartB;
//       }
//     }
//   });
// });

</script>
