<template>
  <div class="p-6 max-w-screen mx-auto">
    <h1 class="text-2xl font-bold mb-4 text-gray-800">Product Management</h1>

    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
      <div
        class="flex flex-col sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4"
      >
        <div class="text-sm text-gray-600">
          create new product
          <a
            href="/admin/products/create"
            class="text-blue-500 hover:underline"
          >
            Create
          </a>
        </div>
        <div class="relative">
          <input
            v-model="searchTerm"
            @input="fetchProducts"
            type="text"
            placeholder="Search for items"
            class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500"
          />
          <div
            class="absolute inset-y-0 left-0 flex items-center ps-3 pointer-events-none"
          >
            <svg
              class="w-5 h-5 text-gray-500"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
              ></path>
            </svg>
          </div>
        </div>
      </div>

      <table class="w-full text-sm text-left text-gray-500">
        <!-- loading state -->
        <tbody v-if="loading">
          <tr>
            <td colspan="9" class="text-center py-4">Loading...</td>
          </tr>
        </tbody>
        <thead class="text-xs text-gray-700 uppercase bg-gray-50">
          <tr>
            <th class="p-4">
              <input
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500"
              />
            </th>
            <th class="px-6 py-3">Product Code</th>
            <th class="px-6 py-3">Image</th>
            <th class="px-6 py-3">Name</th>
            <th class="px-6 py-3">Price</th>
            <th class="px-6 py-3">Category</th>
            <th class="px-6 py-3">In Stock</th>
            <th class="px-6 py-3">Status</th>
            <th class="px-6 py-3">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="product in products"
            :key="product.id"
            class="bg-white border-b border-gray-200 hover:bg-gray-50"
          >
            <td class="w-4 p-4">
              <input
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500"
              />
            </td>
            <th class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap">
              {{ product.product_code }}
            </th>
            <td class="px-6 py-4">
              <img
                :src="product.image"
                alt="Product Image"
                class="w-10 h-10 rounded-full"
              />
            </td>
            <td class="px-6 py-4">{{ product.name }}</td>
            <td class="px-6 py-4">{{ product.price }}</td>
            <td class="px-6 py-4">{{ product.category.name }}</td>
            <td class="px-6 py-4">
              {{ product.in_stock > 0 ? product.in_stock : "Stock Out" }}
            </td>
            <td class="px-6 py-4">
              <span
                class="inline-flex items-center justify-center w-3 h-3 rounded-full
                {{ product.is_active === 1 ? 'bg-green-400' : 'bg-red-400' }}"
                >{{ product.is_active === 1 ? "Active" : "Inactive" }}</span
              >
            </td>
            <td class="px-6 py-4">
              <a href="#" class="font-medium text-blue-600 hover:underline"
                >Edit</a
              >
              <button
                @click="deleteProduct(product.id)"
                class="font-medium text-red-600 hover:underline ms-2"
              >
                Delete
              </button>
            </td>
          </tr>
        </tbody>
        <!-- pagination  -->
        <tfoot>
          <tr>
            <td colspan="9" class="px-6 py-4">
              <nav
                class="flex items-center justify-between"
                aria-label="Table navigation"
              >
                <span class="text-sm text-gray-700">
                  Page {{ page }} of {{ totalPages }} | Total:
                  {{ totalCount }} items
                </span>
                <div class="inline-flex items-center space-x-2">
                  <button
                    @click="page > 1 ? page-- : null"
                    class="px-3 py-1 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-4 focus:ring-gray-200"
                  >
                    Previous
                  </button>
                  <!-- pagination numbers 1,2,3 -->
                  <div class="flex justify-center">
                    <span class="inline-flex gap-1">
                      <button
                        v-for="n in totalPages"
                        :key="n"
                        @click="page = n"
                        class="px-3 py-1 text-sm font-medium border border-gray-300 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-300 transition"
                        :class="
                          page === n
                            ? 'bg-blue-500 text-white'
                            : 'bg-white text-gray-700'
                        "
                      >
                        {{ n }}
                      </button>
                    </span>
                  </div>

                  <button
                    @click="page < totalPages ? page++ : null"
                    class="px-3 py-1 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-4 focus:ring-gray-200"
                  >
                    Next
                  </button>
                </div>
              </nav>
            </td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
const config = useRuntimeConfig();
const apiBase = config.public.apiBase;

const products = ref([]);
const page = ref(1);
const limit = ref(5);
const totalPages = ref(1);
const searchTerm = ref("");
const sortBy = ref("id");
const sortOrder = ref("desc");
const totalCount = ref(0);
const currentPage = ref(1);

const loading = ref(false);

const fetchProducts = async () => {
  try {
    loading.value = true;
    const skip = (page.value - 1) * limit.value;
    const response = await fetch(
      `${apiBase}/products/products?skip=${skip}&limit=${limit.value}&search=${searchTerm.value}&sort_by=${sortBy.value}&order_by=${sortOrder.value}`
    );
    if (!response.ok) {
      loading.value = false;
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    if (data && data.products) {
      products.value = data.products;
      totalPages.value = data.totalPages;
      totalCount.value = data.totalCount;
      currentPage.value = page.value;
      loading.value = false;
    } else {
      loading.value = false;
    }
  } catch (error) {
    loading.value = false;
    console.error("Error fetching products:", error);
  }
};

onMounted(fetchProducts);

watch(page, () => {
  fetchProducts();
});

watch(searchTerm, () => {
  page.value = 1;
  fetchProducts();
});
</script>
