from datetime import date
from pydantic import BaseModel, PositiveInt, ValidationError
from typing import Optional, Dict


class User(BaseModel):
    id: int
    name: str = "lihua"
    date_join: date | None = None  # 默认为None
    tags: Dict[str, PositiveInt]


if __name__ == '__main__':
    try:
        user = User(
            id=1,
            name="李四",
            # date_join=date(2021, 1, 1),  # 这是严格模式
            # date_join="2030-01-01",
            tags={"a": 1, "b": 2}
        )
        print(user)
    except ValidationError as e:
        print(e)
