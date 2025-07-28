<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="w-full max-w-md bg-white p-8 rounded-2xl shadow-xl">
      <h2 class="text-2xl font-bold text-center text-gray-800 mb-6">Admin Login</h2>
      
      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-gray-600 mb-1">Username</label>
          <input
            v-model="username"
            placeholder="Enter your username"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div>
          <label class="block text-gray-600 mb-1">Password</label>
          <input
            v-model="password"
            type="password"
            placeholder="Enter your password"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition duration-300"
        >
          Login
        </button>
      </form>

      <p class="text-center text-sm text-gray-600 mt-4">
        Don't have an account?
        <NuxtLink to="/admin/register" class="text-blue-500 hover:underline">Register</NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
const username = ref("");
const password = ref("");
const { login } = useAuth();
const router = useRouter();

const handleLogin = async () => {
  try {
    await login(username.value, password.value);
    router.push("/admin/dashboard");
  } catch (error) {
    alert("Login failed");
  }
};
</script>
