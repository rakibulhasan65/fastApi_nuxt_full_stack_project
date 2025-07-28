<template>
  <div class="flex h-screen bg-gray-100">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-md hidden md:block">
      <div class="p-4 font-bold text-lg border-b">Admin Panel</div>
      <nav class="p-4">
        <ul class="space-y-2">
          <li>
            <a
              href="/admin/dashboard"
              class="block p-2 rounded hover:bg-gray-200"
              >Dashboard</a
            >
          </li>
          <li>
            <a href="#" class="block p-2 rounded hover:bg-gray-200">Users</a>
          </li>
          <li>
            <a href="#" class="block p-2 rounded hover:bg-gray-200">Settings</a>
          </li>
        </ul>
      </nav>
    </aside>

    <!-- Mobile Sidebar Button -->
    <div class="md:hidden fixed top-4 left-4 z-50">
      <button @click="toggleSidebar" class="p-2 bg-white rounded shadow">
        ☰
      </button>
    </div>

    <!-- Offcanvas Sidebar for Mobile -->
    <transition name="fade">
      <aside
        v-if="showSidebar"
        class="fixed top-0 left-0 w-64 h-full bg-white shadow-md z-40 md:hidden"
      >
        <div class="p-4 flex justify-between items-center border-b">
          <span class="font-bold text-lg">Admin Panel</span>
          <button @click="toggleSidebar">✕</button>
        </div>
        <nav class="p-4">
          <ul class="space-y-2">
            <li>
              <a
                href="/admin/dashboard"
                class="block p-2 rounded hover:bg-gray-200"
                >Dashboard</a
              >
            </li>
            <li>
              <a href="#" class="block p-2 rounded hover:bg-gray-200">Users</a>
            </li>
            <li>
              <a href="#" class="block p-2 rounded hover:bg-gray-200"
                >Settings</a
              >
            </li>
          </ul>
        </nav>
      </aside>
    </transition>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col">
      <!-- Top Navbar -->
      <header class="bg-white shadow-md p-4 flex justify-between items-center">
        <h1 class="text-xl font-semibold">Dashboard</h1>
        <button
          class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
          @click="logoutAndRedirect"
        >
          Logout
        </button>
      </header>

      <!-- Page Content -->
      <main class="flex-1 p-6 overflow-y-auto">
        <p class="text-gray-700">
          Welcome to the dashboard! You can manage users, settings, and more.
        </p>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
const { logout, isAuthenticated, initAuth } = useAuth();
const showSidebar = ref(false);

definePageMeta({
  middleware: "auth",
});

const toggleSidebar = () => {
  showSidebar.value = !showSidebar.value;
};
// Initialize auth on page load
onMounted(() => {
  initAuth();
});

const logoutAndRedirect = () => {
  logout();
  navigateTo("/");
};

watch(isAuthenticated, (newVal) => {
  if (!newVal) {
    navigateTo("/");
  }
});
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
