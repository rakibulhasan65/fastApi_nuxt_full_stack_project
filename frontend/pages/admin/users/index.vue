<template>
  <div class="p-6 max-w-screen mx-auto">
    <h1 class="text-2xl font-bold mb-4 text-gray-800">User Management</h1>

    <!-- <div class="overflow-x-auto">
      <table
        class="min-w-full bg-white border border-gray-200 shadow rounded-lg"
      >
        <thead>
          <tr class="bg-gray-100 text-left text-sm font-medium text-gray-700">
            <th class="px-4 py-2 border-b">ID</th>
            <th class="px-4 py-2 border-b">Username</th>
            <th class="px-4 py-2 border-b">Email</th>
            <th class="px-4 py-2 border-b">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="user in users"
            :key="user.id"
            v-if="users.length > 0"
            class="hover:bg-gray-50 transition duration-150"
          >
            <td class="px-4 py-2 border-b">{{ user.id }}</td>
            <td class="px-4 py-2 border-b">{{ user.username }}</td>
            <td class="px-4 py-2 border-b">{{ user.email }}</td>
            <td class="px-4 py-2 border-b space-x-2">
              <nuxt-link
                :to="`/admin/users/${user.id}/edit`"
                class="bg-yellow-500 hover:bg-yellow-600 text-white py-1 px-3 rounded text-sm"
              >
                ✏️ Edit
              </nuxt-link>
              <button
                @click="deleteUser(user.id)"
                class="bg-red-600 hover:bg-red-700 text-white py-1 px-3 rounded text-sm"
              >
                🗑️ Delete
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div> -->

    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
      <div
        class="flex flex-col sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4"
      >
        <div>
          <button
            class="inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 font-medium rounded-lg text-sm px-3 py-1.5"
            type="button"
          >
            <svg
              class="w-3 h-3 text-gray-500 me-3"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                d="M10 0a10 10 0 1 0 10 10A10.011 10.011 0 0 0 10 0Zm3.982 13.982a1 1 0 0 1-1.414 0l-3.274-3.274A1.012 1.012 0 0 1 9 10V6a1 1 0 0 1 2 0v3.586l2.982 2.982a1 1 0 0 1 0 1.414Z"
              />
            </svg>
            Last 30 days
            <svg class="w-2.5 h-2.5 ms-2.5" fill="none" viewBox="0 0 10 6">
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m1 1 4 4 4-4"
              />
            </svg>
          </button>
          <!-- dropdown body unchanged -->
        </div>
        <div class="relative">
          <input
            type="text"
            placeholder="Search for items"
            class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500"
          />
          <div
            class="absolute inset-y-0 left-0 flex items-center ps-3 pointer-events-none"
          >
            <svg
              class="w-5 h-5 text-gray-500"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
              ></path>
            </svg>
          </div>
        </div>
      </div>

      <table class="w-full text-sm text-left text-gray-500">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50">
          <tr>
            <th class="p-4">
              <input
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500"
              />
            </th>
            <th class="px-6 py-3">ID</th>
            <th class="px-6 py-3">User Name</th>
            <th class="px-6 py-3">Email</th>
            <th class="px-6 py-3">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="user in users"
            :key="user.id"
            v-if="users.length > 0"
            class="bg-white border-b border-gray-200 hover:bg-gray-50"
          >
            <td class="w-4 p-4">
              <input
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500"
              />
            </td>
            <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
              {{ user.id }}
            </th>
            <td class="px-6 py-4">{{ user.username }}</td>
            <td class="px-6 py-4">{{ user.email }}</td>
            <td class="px-6 py-4">
              <a href="#" class="font-medium text-blue-600 hover:underline"
                >Edit</a
              >
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const config = useRuntimeConfig();
const apiBase = config.public.apiBase;

const users = ref([]);

const fetchUsers = async () => {
  try {
    const response = await fetch(`${apiBase}/users/users`);
    users.value = await response.json();
  } catch (error) {
    console.error("Error fetching users:", error);
  }
};

const deleteUser = async (id) => {
  try {
    await fetch(`${apiBase}/users/users/${id}`, { method: "DELETE" });
    fetchUsers();
  } catch (error) {
    console.error("Error deleting user:", error);
  }
};

onMounted(fetchUsers);
</script>
