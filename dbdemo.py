from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    "mysql+asyncmy://root:12345678@127.0.0.1:3306/mydjango?charset=utf8mb4",
    # 将输出所有执行SQL的日志（默认是关闭的）
    echo=True,
    # 连接池大小（默认是5个）
    pool_size=10,
    # 允许连接池最大的连接数（默认是10个）
    max_overflow=20,
    # 获得连接超时时间（默认是30s）
    pool_timeout=10,
    # 连接回收时间（默认是-1，代表永不回收）
    pool_recycle=3600,
    # 连接前是否预检查（默认为False）
    pool_pre_ping=True,
)

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

AsyncSessionFactory = sessionmaker(
    # Engine或者其子类对象（这里是AsyncEngine）
    bind=engine,
    # Session类的代替（默认是Session类）
    class_=AsyncSession,
    # 是否在查找之前执行flush操作（默认是True）
    autoflush=True,
    # 是否在执行commit操作后Session就过期（默认是True）
    expire_on_commit=False
)

