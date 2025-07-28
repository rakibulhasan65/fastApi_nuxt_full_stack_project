// middleware/auth.ts
export default defineNuxtRouteMiddleware((to) => {
  const { token, initAuth } = useAuth();

  // Initialize auth state on client-side
  if (process.client) {
    initAuth();
  }

  // Check if user is authenticated
  if (!token.value) {
    return navigateTo("/");
  }
});
