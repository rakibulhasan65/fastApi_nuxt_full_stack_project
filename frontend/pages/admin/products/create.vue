<!-- pages/product/add.vue -->
<template>
  <div class="min-h-screen bg-gray-50 py-10 px-4">
    <div class="max-w-3xl mx-auto bg-white p-8 rounded-2xl shadow-md">
      <h2 class="text-3xl font-semibold text-gray-800 mb-6">Add New Product</h2>

      <form @submit.prevent="submitForm" class="space-y-6">
        <!-- Product Code -->
        <div>
          <label
            for="product_code"
            class="block text-sm font-medium text-gray-700"
            >Product Code</label
          >
          <input
            v-model="form.product_code"
            type="text"
            id="product_code"
            class="mt-1 block w-full rounded-lg border-2 border-gray-400 py-2 px-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            placeholder="Optional"
          />
        </div>

        <!-- Product Name -->
        <div>
          <label for="name" class="block text-sm font-medium text-gray-700"
            >Product Name</label
          >
          <input
            v-model="form.name"
            type="text"
            id="name"
            class="mt-1 block w-full rounded-lg border-2 border-gray-400 py-2 px-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
            required
          />
        </div>

        <!-- Price & In Stock -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label for="price" class="block text-sm font-medium text-gray-700"
              >Price</label
            >
            <input
              v-model.number="form.price"
              type="number"
              id="price"
              class="mt-1 block w-full rounded-lg border-2 border-gray-400 py-2 px-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
              required
            />
          </div>
          <div>
            <label
              for="in_stock"
              class="block text-sm font-medium text-gray-700"
              >In Stock</label
            >
            <input
              v-model.number="form.in_stock"
              type="number"
              id="in_stock"
              class="mt-1 block w-full rounded-lg border-2 border-gray-400 py-2 px-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
            />
          </div>
        </div>

        <!-- Category -->
        <div>
          <label
            for="category_id"
            class="block text-sm font-medium text-gray-700"
            >Category</label
          >
          <select
            v-model="form.category_id"
            id="category_id"
            class="mt-1 block w-full rounded-lg border-2 border-gray-400 py-2 px-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
            required
          >
            <option disabled value="">Select category</option>
            <option
              v-for="category in categories"
              :key="category.id"
              :value="category.id"
            >
              {{ category.name }}
            </option>
          </select>
        </div>

        <!-- Description -->
        <div>
          <label
            for="description"
            class="block text-sm font-medium text-gray-700"
            >Description</label
          >
          <textarea
            v-model="form.description"
            id="description"
            rows="4"
            class="mt-1 block w-full rounded-lg border-2 border-gray-400 py-2 px-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
            required
          ></textarea>
        </div>

        <!-- Image Upload -->
        <div>
          <label class="block text-sm font-medium text-gray-700"
            >Product Image</label
          >
          <input
            type="file"
            accept="image/*"
            @change="handleImageUpload"
            class="mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:bg-primary-100 file:text-primary-700 hover:file:bg-primary-200"
          />
          <div v-if="form.image" class="mt-4">
            <img
              :src="form.image"
              alt="Preview"
              class="w-32 rounded-lg shadow-md"
            />
          </div>
        </div>

        <!-- Is Active Checkbox -->
        <div>
          <label class="inline-flex items-center">
            <input
              v-model="form.is_active"
              type="checkbox"
              class="rounded border-gray-300 text-primary-600 shadow-sm focus:ring-primary-500"
            />
            <span class="ml-2 text-sm text-gray-700">Active</span>
          </label>
        </div>

        <!-- Submit -->
        <div>
          <button
            type="submit"
            class="w-full sm:w-auto bg-primary-600 text-white px-6 py-2 rounded-lg hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            Submit Product
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const form = ref({
  product_code: "",
  name: "",
  price: 0,
  in_stock: 0,
  category_id: "",
  description: "",
  image: "",
  is_active: false,
});

const categories = ref([
  { id: 1, name: "Electronics" },
  { id: 2, name: "Clothing" },
  { id: 3, name: "Books" },
]);

function handleImageUpload(event: Event) {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      form.value.image = e.target?.result as string;
    };
    reader.readAsDataURL(file);
  }
}

function submitForm() {
  console.log("Submitted:", form.value);
  // API call logic here
}
</script>

<style scoped>
/* Optional: define Tailwind primary color for consistency */
:root {
  --color-primary: #3b82f6;
}
</style>
