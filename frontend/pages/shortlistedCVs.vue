<template>
    <div>
        <Header header-text="Shortlisted CVs" />

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

            <div class="row row-cols-1 row-cols-md-3 g-4">
                <div v-for="(candidate, candidateId) in sortedShortlistedCandidates" :key="candidateId" class="col-md-3">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title text-center">{{ candidate.candidateName }}</h5>
                            <div class="text-center my-3">
                                <span>Course of Study: {{ candidate.courseOfStudy }}</span><br>
                                <span :class="getMatchColor(candidate.matchPercent)">{{ candidate.matchPercent }}% match</span><br>
                                <span>English Score: {{ candidate.candidateEnglishScore }}</span>
                            </div>
                            <div class="card-text text-body-secondary text-center my-2">
                                <li v-for="(keyword, index) in candidate.keywords.split(',')" :key="index" class="list-group-item">{{ keyword }}</li>
                            </div>
                        </div>
                        <div class="card-footer text-center">
                            <a :href="candidate.cvLink" class="btn btn-secondary text-center stretched-link w-100" target="_blank" rel="noopener noreferrer">
                                View CV
                            </a>
                        </div>
                    </div>
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

const shortlistedCandidates = {
    candidate1: {
        candidateId: "1",
        candidateName: "Nit",
        matchPercent: "88",
        courseOfStudy: "Human Resources",
        candidateEnglishScore: "25",
        keywords: "Onboarding, President of school HR club, Talent Acquisition",
        cvLink: "https://indoramaventures.sharepoint.com/:b:/r/sites/IVL_Internship/Shared%20Documents/2025_resume/cv1.pdf?csf=1&web=1&e=1Ykopv"
    },
    candidate2: {
        candidateId: "2",
        candidateName: "Pim",
        matchPercent: "83",
        courseOfStudy: "Human Resources",
        candidateEnglishScore: "22",
        keywords: "Onboarding, Microsoft Excel",
        cvLink: "https://indoramaventures.sharepoint.com/:b:/r/sites/IVL_Internship/Shared%20Documents/2025_resume/cv1.pdf?csf=1&web=1&e=1Ykopv"
    },
    candidate3: {
        candidateId: "3",
        candidateName: "Pit",
        matchPercent: "79",
        courseOfStudy: "Business Administration",
        candidateEnglishScore: "20",
        keywords: "Human Resources, Recruitment",
        cvLink: "https://indoramaventures.sharepoint.com/:b:/r/sites/IVL_Internship/Shared%20Documents/2025_resume/cv1.pdf?csf=1&web=1&e=1Ykopv"
    },
    candidate4: {
        candidateId: "4",
        candidateName: "Kim",
        matchPercent: "59",
        courseOfStudy: "Business Administration",
        candidateEnglishScore: "18",
        keywords: "Onboarding, Talent Acquisition",
        cvLink: "https://indoramaventures.sharepoint.com/:b:/r/sites/IVL_Internship/Shared%20Documents/2025_resume/cv1.pdf?csf=1&web=1&e=1Ykopv"
    },
    candidate5: {
        candidateId: "5",
        candidateName: "Jim",
        matchPercent: "80",
        courseOfStudy: "Human Resources",
        candidateEnglishScore: "15",
        keywords: "Onboarding, Microsoft Excel",
        cvLink: "https://indoramaventures.sharepoint.com/:b:/r/sites/IVL_Internship/Shared%20Documents/2025_resume/cv1.pdf?csf=1&web=1&e=1Ykopv"
    },
    candidate6: {
        candidateId: "6",
        candidateName: "Bin",
        matchPercent: "70",
        courseOfStudy: "Accounting",
        candidateEnglishScore: "22",
        keywords: "Onboarding",
        cvLink: "https://indoramaventures.sharepoint.com/:b:/r/sites/IVL_Internship/Shared%20Documents/2025_resume/cv1.pdf?csf=1&web=1&e=1Ykopv"
    },
}

const sortedShortlistedCandidates = Object.values(shortlistedCandidates).sort((a, b) => b.matchPercent - a.matchPercent);

const getMatchColor = (matchPercent) => {
    if (matchPercent >= 80) {
        return "high";
    } else if (matchPercent >= 60) {
        return "medium";
    } else {
        return "low";
    }
}

</script>

<style scoped>
.low {
    color: red;
}

.medium {
    color: orange;
}

.high {
    color: green;
}

</style>