  <template>
    <div class="min-h-screen flex items-center justify-center bg-gray-50">
      <div class="w-full max-w-md bg-white shadow-xl rounded-xl p-6">
        <h1 class="text-2xl font-semibold text-center text-gray-800 mb-6">Login to Your Account</h1>
        <form @submit.prevent="submit" class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Username</label>
            <input
              v-model="username"
              placeholder="Enter your username"
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
            Login
          </button>

          <p class="text-center text-sm text-gray-500 mt-4">
            Don't have an account?
            <NuxtLink to="/register" class="text-blue-600 hover:underline">Register here</NuxtLink>
          </p>
        </form>
      </div>
    </div>
  </template>

  <script setup>
  definePageMeta({
    layout: "login",
  });
  const username = ref("");
  const password = ref("");
  const { login } = useAuth();

  const submit = async () => {
    try {
      await login(username.value, password.value);
      navigateTo("/admin/dashboard");
    } catch (e) {
      alert("Login failed");
    }
  };


  </script>
