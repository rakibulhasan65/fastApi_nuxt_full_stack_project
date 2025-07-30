export default defineNuxtRouteMiddleware((to) => {
  const { token, initAuth } = useAuth();

  if (process.client) {
    initAuth();

    const protectedRoutes = ["/admin", "/admin/dashboard"];
    const isProtected = protectedRoutes.some((route) =>
      to.path.startsWith(route)
    );

    if (isProtected && !token.value) {
      return navigateTo("/");
    }
  }
});
