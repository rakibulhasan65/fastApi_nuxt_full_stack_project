
// Alternative: middleware/auth.global.ts for global auth checking
export default defineNuxtRouteMiddleware((to) => {
  const { token, initAuth } = useAuth();

  // Initialize auth state on client-side
  if (process.client) {
    initAuth();
  }

  // Define protected routes
  const protectedRoutes = ["/admin/dashboard", "/admin"];

  // Check if current route is protected
  const isProtectedRoute = protectedRoutes.some((route) =>
    to.path.startsWith(route)
  );

  // Redirect to login if accessing protected route without token
  if (isProtectedRoute && !token.value) {
    return navigateTo("/");
  }
});
