<!-- layouts/admin.vue -->
<template>
  <div class="flex h-screen bg-gradient-to-br from-slate-50 to-blue-50">
    <!-- Desktop Sidebar -->
    <aside class="hidden lg:flex lg:flex-col lg:w-72 bg-white/80 backdrop-blur-xl shadow-2xl border-r border-slate-200/60">
      <!-- Logo Section -->
      <div class="p-6 border-b border-slate-200/60">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
            </svg>
          </div>
          <div>
            <h1 class="text-xl font-bold bg-gradient-to-r from-slate-800 to-slate-600 bg-clip-text text-transparent">Admin</h1>
            <p class="text-xs text-slate-500">Control Panel</p>
          </div>
        </div>
      </div>

      <!-- Navigation -->
      <nav class="flex-1 p-6">
        <div class="space-y-1">
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-4">Menu</div>
          
          <NuxtLink
            to="/admin/dashboard"
            class="group flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200 relative overflow-hidden"
            active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/25"
          >
            <svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2-2z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5a2 2 0 012-2h4a2 2 0 012 2v6H8V5z" />
            </svg>
            Dashboard
            <div class="absolute inset-0 bg-gradient-to-r from-blue-600/0 via-blue-600/5 to-blue-600/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </NuxtLink>

          <NuxtLink
            to="/admin/users"
            class="group flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200 relative overflow-hidden"
            active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/25"
          >
            <svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-.5a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            Users
            <div class="absolute inset-0 bg-gradient-to-r from-blue-600/0 via-blue-600/5 to-blue-600/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </NuxtLink>

          <NuxtLink
            to="/admin/analytics"
            class="group flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200 relative overflow-hidden"
            active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/25"
          >
            <svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            Analytics
            <div class="absolute inset-0 bg-gradient-to-r from-blue-600/0 via-blue-600/5 to-blue-600/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </NuxtLink>

          <NuxtLink
            to="/admin/settings"
            class="group flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200 relative overflow-hidden"
            active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/25"
          >
            <svg class="w-5 h-5 mr-3 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            Settings
            <div class="absolute inset-0 bg-gradient-to-r from-blue-600/0 via-blue-600/5 to-blue-600/0 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </NuxtLink>
        </div>
      </nav>

      <!-- User Profile Section -->
      <div class="p-6 border-t border-slate-200/60">
        <div class="flex items-center space-x-3 p-3 rounded-xl bg-gradient-to-r from-slate-50 to-blue-50 border border-slate-200/60">
          <div class="w-10 h-10 bg-gradient-to-r from-emerald-500 to-teal-600 rounded-full flex items-center justify-center">
            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-medium text-slate-900 truncate">Admin User</p>
            <p class="text-xs text-slate-500 truncate">admin@example.com</p>
          </div>
        </div>
      </div>
    </aside>

    <!-- Mobile Menu Button -->
    <div class="lg:hidden fixed top-4 left-4 z-50">
      <button
        @click="toggleSidebar"
        class="p-3 bg-white/90 backdrop-blur-sm rounded-xl shadow-lg border border-slate-200/60 hover:bg-white transition-all duration-200"
      >
        <svg class="w-6 h-6 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>
    </div>

    <!-- Mobile Sidebar Overlay -->
    <transition
      enter-active-class="transition-opacity duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-opacity duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="showSidebar"
        class="lg:hidden fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-40"
        @click="toggleSidebar"
      ></div>
    </transition>

    <!-- Mobile Sidebar -->
    <transition
      enter-active-class="transition-transform duration-300 ease-out"
      enter-from-class="-translate-x-full"
      enter-to-class="translate-x-0"
      leave-active-class="transition-transform duration-200 ease-in"
      leave-from-class="translate-x-0"
      leave-to-class="-translate-x-full"
    >
      <aside
        v-if="showSidebar"
        class="lg:hidden fixed top-0 left-0 w-80 h-full bg-white/95 backdrop-blur-xl shadow-2xl z-50 flex flex-col"
      >
        <!-- Mobile Header -->
        <div class="p-6 border-b border-slate-200/60 flex justify-between items-center">
          <div class="flex items-center space-x-3">
            <div class="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
            <span class="text-lg font-bold text-slate-800">Admin Panel</span>
          </div>
          <button
            @click="toggleSidebar"
            class="p-2 hover:bg-slate-100 rounded-lg transition-colors duration-200"
          >
            <svg class="w-6 h-6 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <!-- Mobile Navigation -->
        <nav class="flex-1 p-6">
          <div class="space-y-1">
            <NuxtLink
              to="/admin/dashboard"
              @click="toggleSidebar"
              class="flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200"
              active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2H5a2 2 0 00-2-2z" />
              </svg>
              Dashboard
            </NuxtLink>

            <NuxtLink
              to="/admin/users"
              @click="toggleSidebar"
              class="flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200"
              active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-.5a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              Users
            </NuxtLink>

            <NuxtLink
              to="/admin/analytics"
              @click="toggleSidebar"
              class="flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200"
              active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
              Analytics
            </NuxtLink>

            <NuxtLink
              to="/admin/settings"
              @click="toggleSidebar"
              class="flex items-center px-4 py-3 text-sm font-medium text-slate-700 rounded-xl hover:bg-blue-50 hover:text-blue-700 transition-all duration-200"
              active-class="bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg"
            >
              <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
              Settings
            </NuxtLink>
          </div>
        </nav>
      </aside>
    </transition>

    <!-- Main Content Area -->
    <div class="flex-1 flex flex-col min-w-0">
      <!-- Top Header -->
      <header class="bg-white/80 backdrop-blur-xl shadow-sm border-b border-slate-200/60 px-4 lg:px-8 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-4">
            <div class="lg:hidden w-6"></div> <!-- Spacer for mobile menu button -->
            <div>
              <h1 class="text-2xl font-bold text-slate-800">{{ currentPageTitle }}</h1>
              <p class="text-sm text-slate-500 mt-1">{{ currentPageDescription }}</p>
            </div>
          </div>

          <div class="flex items-center space-x-4">
            <!-- Notifications -->
            <button class="relative p-2 text-slate-500 hover:text-slate-700 hover:bg-slate-100 rounded-lg transition-all duration-200">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-5-5h5l-5-5V9a3 3 0 11-6 0v1.5L4 15h5v2a3 3 0 106 0z" />
              </svg>
              <span class="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
            </button>

            <!-- User Menu -->
            <div class="relative">
              <button class="flex items-center space-x-3 p-2 rounded-lg hover:bg-slate-100 transition-all duration-200">
                <div class="w-8 h-8 bg-gradient-to-r from-emerald-500 to-teal-600 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
                <div class="hidden md:block text-left">
                  <p class="text-sm font-medium text-slate-700">Admin</p>
                  <p class="text-xs text-slate-500">Online</p>
                </div>
              </button>
            </div>

            <!-- Logout Button -->
            <button
              @click="logoutAndRedirect"
              class="px-4 py-2 bg-gradient-to-r from-red-500 to-rose-600 text-white rounded-lg font-medium shadow-lg shadow-red-500/25 hover:shadow-red-500/40 hover:scale-105 transition-all duration-200"
            >
              <svg class="w-4 h-4 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              <span class="hidden sm:inline">Logout</span>
            </button>
          </div>
        </div>
      </header>

      <!-- Page Content -->
      <main class="flex-1 p-4 lg:p-8 overflow-y-auto bg-gradient-to-br from-slate-50/50 to-blue-50/50">
        <div class="min-w-full mx-auto">
          <slot />
        </div>
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
const showSidebar = ref(false)
const { logout, isAuthenticated, initAuth } = useAuth()

// Dynamic page titles based on route
const route = useRoute()
const currentPageTitle = computed(() => {
  const titles = {
    '/admin/dashboard': 'Dashboard',
    '/admin/users': 'User Management',
    '/admin/analytics': 'Analytics',
    '/admin/settings': 'Settings'
  }
  return titles[route.path] || 'Dashboard'
})

const currentPageDescription = computed(() => {
  const descriptions = {
    '/admin/dashboard': 'Overview of your system metrics and activities',
    '/admin/users': 'Manage user accounts and permissions',
    '/admin/analytics': 'View detailed analytics and reports',
    '/admin/settings': 'Configure system settings and preferences'
  }
  return descriptions[route.path] || 'Welcome to your admin panel'
})

const toggleSidebar = () => {
  showSidebar.value = !showSidebar.value
}

onMounted(() => {
  initAuth()
})

const logoutAndRedirect = () => {
  logout()
  navigateTo('/')
}

watch(isAuthenticated, (val) => {
  if (!val) navigateTo('/')
})

// Close sidebar when route changes
watch(() => route.path, () => {
  showSidebar.value = false
})
</script>