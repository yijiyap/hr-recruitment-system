<template>
    <div>
        <Header header-text="2. Confirm the role information" />

        <div class="container-fluid my-3">
            <div class="row bg-light p-3 my-3">
                <div class="col text-center">
                    <h3 class="tw-text-xl tw-font-bold tw-text-center">
                        Supervisor details
                    </h3>
                    Department: {{ roleToHire.supervisorDetails.department }} <br >
                    Supervisor: {{ roleToHire.supervisorDetails.supervisor }} <br >
                    Supervisor email: {{ roleToHire.supervisorDetails.supervisorEmail }}
                    <br >
                </div>
                <div class="col text-center">
                    <h3 class="tw-text-xl tw-font-bold tw-text-center">
                        Internship Role Details
                    </h3>
                    Role {{ roleToHire.internshipRoleDetails.roleId }}:
                    {{ roleToHire.internshipRoleDetails.roleName }}<br >
                    Internship Period:
                    {{ roleToHire.internshipRoleDetails.internshipPeriod }} <br >
                </div>
            </div>

            <SectionRole
v-for="section in roleToHire.sections" :key="section" :section-title="section.sectionTitle"
                :subsections="section.subsections" @cancel-edit="backToOriginal" />

            <div class="row">
                <div class="tw-flex tw-justify-center mt-3">
                    <button class="btn btn-secondary">
                        <NuxtLink to="/shortlistedCVs" style="text-decoration: none; color: inherit">Get relevant CVs
                        </NuxtLink>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const roleToHire = ref({
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
    sections: {
        sectionRoleDesc: {
            sectionTitle: "Role Description",
            subsections: [
                {
                    subsectionTitle: "Primary Responsibilities",
                    subsectionText:
                        "Assist with recruitment processes, including posting job ads, screening resumes and scheduling interviews.",
                },
                {
                    subsectionTitle: "Project Description",
                    subsectionText:
                        "Work on updating employee handbook and assist in organizing the annual employee engagement survey.",
                }
            ],
        },
        sectionSkillsAndQualifications: {
            sectionTitle: "Skills and Qualifications",
            subsections: [
                {
                    subsectionTitle: "Required Skills",
                    subsectionText:
                        "Strong communication skills, attention to detail, proficiency in Microsoft Office Suite.",
                },
                {
                    subsectionTitle: "Preferred Skills",
                    subsectionText:
                        "Familiarity with HR software (JobsDB, LinkedIn, SAP SuccessFactors), basic knowledge of labour laws.",
                },
                {
                    subsectionTitle: "Education Level",
                    subsectionText:
                        "Currently pursuing a degree in Human Resources, Business Administration, or a related field.",
                },
            ],
        },
        sectionAdditionalInformation: {
            sectionTitle: "Additional Information",
            subsections: [
                {
                    subsectionTitle: "Others",
                    subsectionText:
                        "Previous internship experience in a Human Resources Internship is preferred.",
                },
            ],
        },
    }
});

const original = JSON.parse(JSON.stringify(roleToHire.value));

function backToOriginal() {
    roleToHire.value = JSON.parse(JSON.stringify(original));
}


</script>