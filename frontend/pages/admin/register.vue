<template>
  <div class="max-w-md mx-auto p-4">
    <h2 class="text-xl mb-4">Register</h2>
    <form @submit.prevent="handleRegister">
      <input v-model="username" placeholder="Username" class="input" />
      <input v-model="email" placeholder="Email" class="input" />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        class="input"
      />
      <button class="btn mt-2">Register</button>
    </form>
  </div>
</template>

<script setup lang="ts">
const username = ref("");
const email = ref("");
const password = ref("");
const { register } = useAuth();

const handleRegister = async () => {
  const success = await register(username.value, email.value, password.value);
  if (success) navigateTo("/");
};
</script>
