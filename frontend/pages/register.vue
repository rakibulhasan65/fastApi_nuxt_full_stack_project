<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50">
    <div class="w-full max-w-md bg-white shadow-xl rounded-xl p-6">
      <h2 class="text-2xl font-semibold text-center text-gray-800 mb-6">Create an Account</h2>
      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Username</label>
          <input
            v-model="username"
            placeholder="Enter your username"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input
            v-model="email"
            type="email"
            placeholder="Enter your email"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Password</label>
          <input
            v-model="password"
            type="password"
            placeholder="Enter your password"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded-lg transition duration-300"
        >
          Register
        </button>

        <p class="text-center text-sm text-gray-500 mt-4">
          Already have an account?
          <NuxtLink to="/" class="text-blue-600 hover:underline">Login here</NuxtLink>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "login",
});

const username = ref("");
const email = ref("");
const password = ref("");
const { register } = useAuth();

const handleRegister = async () => {
  const success = await register(username.value, password.value, email.value);
  if (success) navigateTo("/");
};
</script>
