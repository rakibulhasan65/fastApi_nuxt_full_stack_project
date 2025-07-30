export const useAuth = () => {
  const token = useState<string | null>("auth-token", () => null);
  const config = useRuntimeConfig();
  const apiBase = config.public.apiBase;

  const isAuthenticated = computed(() => !!token.value);

  const login = async (username: string, password: string) => {
    const response = await $fetch(`${apiBase}/users/login`, {
      method: "POST",
      body: { username, password },
    });

    token.value = response.access_token;

    if (process.client) {
      localStorage.setItem("auth-token", response.access_token);
    }

    return true;
  };

  const register = async (
    username: string,
    password: string,
    email: string
  ) => {
    await $fetch(`${apiBase}/users/register`, {
      method: "POST",
      body: { username, password, email },
    });

    return true;
  };

  const logout = () => {
    token.value = null;
    if (process.client) {
      localStorage.removeItem("auth-token");
    }
    navigateTo("/");
  };

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
    initAuth,
    token: readonly(token),
    isAuthenticated,
  };
};
