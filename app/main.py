from fastapi import FastAPI
from app.api.v1.endpoints import users, product
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
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(product.router, prefix="/api/v1/products")
