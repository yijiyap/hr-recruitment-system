<template>
  <div class="row bg-light p-3 m-3">
    <div class="col">
      <h3 class="tw-text-xl tw-font-bold tw-text-center">
        {{ sectionTitle }}
      </h3>

      <div v-if="!isEditingSubsection">
        <div v-for="subsection in reactiveSubsections" :key="subsection">
          <h4 class="tw-text-lg tw-font-bold">{{ subsection.subsectionTitle }}</h4>
          <p>
            {{ subsection.subsectionText }}
          </p>
        </div>
      </div>

      <div v-else>
        <div v-for="subsection in reactiveSubsections" :key="subsection">
          <h4 class="tw-text-lg tw-font-bold">{{ subsection.subsectionTitle }}</h4>
          <textarea v-model="subsection.subsectionText" />
        </div>
      </div>
    </div>
    <div>
      <div class="tw-flex tw-justify-end tw-mr-5">
        <button v-if="isEditingSubsection" class="btn btn-secondary tw-mr-3" @click="$emit('cancelEdit')">
          Back to original
        </button>
        <button class="btn btn-secondary" @click="toggleEditMode">
          {{ toggleEditButton }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue';

const props = defineProps({
  sectionTitle: String,
  subsections: Array,
});

// Initialize reactiveSubsections with the current prop value
const reactiveSubsections = reactive([...props.subsections]);

// Keep a deep copy of the original subsections to revert changes
let originalSubsections = JSON.parse(JSON.stringify(props.subsections));

let toggleEditButton = "Edit";

const isEditingSubsection = ref(false);

function toggleEditMode() {
  isEditingSubsection.value =!isEditingSubsection.value;
  toggleEditButton = isEditingSubsection.value? "Save" : "Edit";
}

// function cancelEdit() {
//   // Revert to the original subsections does not work
//   reactiveSubsections.splice(0, reactiveSubsections.length,...originalSubsections);
//   isEditingSubsection.value = false;
//   toggleEditButton = "Edit";
// }
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