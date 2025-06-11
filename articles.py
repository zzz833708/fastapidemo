from typing import List

from fastapi import APIRouter, Header, HTTPException, Depends
from pydantic import BaseModel


async def dddd(x_mytest2: str = Header()):
    if x_mytest2 != "dd":
        raise HTTPException(status_code=400, detail="test2测试失败")


article = APIRouter(prefix="/articles", dependencies=[Depends(dddd)], tags=["article"])


@article.get("/")
async def hello():
    return {"message": "hello"}


class UserResp(BaseModel):
    id: int
    username: str
    email: str


@article.get('/list', response_model=List[UserResp])
async def user_list(page: int = 1):
    # 假设这里从数据库或其他地方获取用户数据
    users = [
        UserResp(id=1, username="ddd", email='hy@qq.com'),
        UserResp(id=2, username='lisi', email='lisi@example.com')
    ]
    return users
