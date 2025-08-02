from fastapi import FastAPI
from app.api.v1.endpoints import users, product, orders , addToCart
from app.middleware.logging import LoggingMiddleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Middleware
app.add_middleware(LoggingMiddleware)

# Routes include
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(product.router, prefix="/api/v1/products")
app.include_router(orders.router, prefix="/api/v1/orders")
app.include_router(addToCart.router, prefix="/api/v1/add_to_cart")
