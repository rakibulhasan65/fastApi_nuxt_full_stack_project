// nuxt.config.ts
export default defineNuxtConfig({
  compatibilityDate: "2025-08-01",
  devtools: { enabled: true },
  modules: ["@nuxtjs/tailwindcss"], // ✅ এই লাইনটাই যথেষ্ট Tailwind এর জন্য
  css: ["~/assets/css/main.css"], // ✅ Required for inline Tailwind config
  runtimeConfig: {
    public: {
      apiBase:
        process.env.NUXT_PUBLIC_API_BASE || "http://127.0.0.1:8000/api/v1",
    },
  },
  // ❌ Remove postcss configuration - @nuxtjs/tailwindcss handles this automatically
});
