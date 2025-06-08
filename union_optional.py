from typing import Union, Optional, Any

a: Union[int, float] = 111
b: Union[int, float] = 111.5
c: int | float = 111.5

# 写法是等价的 可以传str，也可以传None
x: Optional[str] = "x"
x1: Union[str, None] = "x"
x2: str | None = "x"


# Any任意类型 不指定类型就是任意类型
f: Any = 100
f1 = 100
