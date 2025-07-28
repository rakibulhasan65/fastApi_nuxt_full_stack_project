import { useRouter } from "vue-router";

export const useAuth = () => {
  // Initialize token with proper SSR handling
  const token = useState<string | null>("auth-token", () => {
    if (process.client) {
      return localStorage.getItem("auth-token");
    }
    return null;
  });

  const config = useRuntimeConfig();
  const apiBase = config.public.apiBase;
  const router = useRouter();

  // Computed property to check if user is authenticated
  const isAuthenticated = computed(() => {
    return !!token.value;
  });

  const login = async (username: string, password: string) => {
    try {
      const response = await $fetch(`${apiBase}/users/login`, {
        method: "POST",
        body: { username, password },
      });

      token.value = response.access_token;

      if (process.client) {
        localStorage.setItem("auth-token", response.access_token);
      }

      await router.push("/admin/dashboard");
    } catch (error) {
      console.error("Login failed:", error);
      throw error;
    }
  };

  const register = async (
    username: string,
    password: string,
    email: string
  ) => {
    try {
      await $fetch(`${apiBase}/users/register`, {
        method: "POST",
        body: { username, password, email },
      });

      return true;
    } catch (error) {
      console.error("Registration failed:", error);
      throw error;
    }
  };

  const logout = () => {
    token.value = null;
    if (process.client) {
      localStorage.removeItem("auth-token");
    }
    router.push("/");
  };

  const getToken = () => {
    if (token.value) return token.value;
    if (process.client) {
      const saved = localStorage.getItem("auth-token");
      if (saved) {
        token.value = saved;
        return saved;
      }
    }
    return null;
  };

  // Initialize token on client-side hydration
  const initAuth = () => {
    if (process.client && !token.value) {
      const saved = localStorage.getItem("auth-token");
      if (saved) {
        token.value = saved;
      }
    }
  };

  return {
    login,
    register,
    logout,
    getToken,
    initAuth,
    token: readonly(token),
    isAuthenticated,
  };
};
