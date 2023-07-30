# https://pypi.org/project/fastapi-redis-cache/#usage
# https://github.com/a-luna/fastapi-redis-cache

# import os

# from fastapi import FastAPI, Request, Response
# from fastapi_redis_cache import FastApiRedisCache, cache
# from sqlalchemy.orm import Session

# LOCAL_REDIS_URL = "redis://127.0.0.1:6379"

# app = FastAPI(title="FastAPI Redis Cache Example")

# @app.on_event("startup")
# def startup():
#     redis_cache = FastApiRedisCache()
#     redis_cache.init(
#         host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
#         prefix="myapi-cache",
#         response_header="X-MyAPI-Cache",
#         ignore_arg_types=[Request, Response, Session]
#     )