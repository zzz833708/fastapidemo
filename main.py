from typing import Union, Dict

from fastapi import FastAPI, Path
from pydantic import BaseModel, field_validator

app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"name": "hello"}
#
#
# # 路由参数 必传  /books/xxx
# @app.get("/books/{name}")
# async def item_info(name: str = Path(max_length=5, description="Book id")):
#     return {"name": f"hello{name}"}
#
#
# # 查询参数 /items?page=100&size=30
# @app.get("/items")
# async def book_list(page: int, size: int = 100):  # page: 查询参数，没指定默认值，是必填的  size：指定了默认值，就可以不传
#     return {
#         "page": page,
#         "size": size
#     }
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float | None = 0
#
#     @field_validator("name")
#     @classmethod
#     def validate_name(cls, value: str):
#         if " " in value:
#             raise ValueError("Name should not contain spaces.")
#         return value
#
#
# # 传入指定的字段 json
# @app.put("/items/{name}")
# async def update_item(name: str, item: Item):
#     print(item)
#     print(item.name)
#     print(item.description)
#     return {"message": "ok"}
#
#
# from fastapi import Cookie
#
#
# @app.get('/cookie/get')
# async def get_cookie(username: str | None = Cookie(default="lihua")):
#     print("username:", username)
#     return 'success'
#
#
# from fastapi.responses import JSONResponse
#
#
# @app.get('/cookie/set')
# async def set_cookie():
#     response = JSONResponse(content={"message": "success"})
#     response.set_cookie('sessionid', 'xxx')
#     return response
#
#
# from fastapi import Header
#
#
# @app.get('/header')
# def get_header(
#         user_agent: str | None = Header(default=None),
#         host: str | None = Header(default=None),
# ):
#     print('user-agent:', user_agent)
#     print('host:', host)
#     return 'success'


# from fastapi import Depends
#
#
# async def common(q: str | None = None, skip: int = 0, limit: int = 10):
#     skip = 100
#     return {"q": q, "skip": skip, "limit": limit}
#
#
# @app.get('/items')
# async def read_items(common: Dict = Depends(common)):
#     common["q"] = "lihua"
#     print(common.get('q'), common.get('skip'), common.get('limit'))
#     return {"message": "ok"}
#
#
# @app.get("/users")
# async def read_users(common: dict = Depends(common)):
#     return common


from fastapi import Depends, FastAPI

# app = FastAPI()
#
#
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items")
async def read_items(commons=Depends(CommonQueryParams)):
    response = {"q": commons.q, "skip": commons.skip, "limit": commons.limit}
    return response
