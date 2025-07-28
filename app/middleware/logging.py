from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import time

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request, call_next):
        start_time = time.time()
        print("🚀 Middleware working...")
        response = await call_next(request)
        duration = time.time() - start_time
        print(f"Request: {request.method} {request.url} - Duration: {duration:.4f} seconds")
        return response
