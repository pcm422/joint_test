from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL
from typing import AsyncGenerator

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL 환경 변수가 설정되지 않았습니다.")

# 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True, future=True) # echo=True는 개발 시 SQL 로깅

# 비동기 세션 생성기
AsyncSessionFactory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False, # 비동기 작업 시 필요할 수 있음
    autocommit=False,
    autoflush=False,
)

# Dependency Injection을 위한 세션 얻기 함수
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        try:
            yield session
            await session.commit() # 기본적으로 commit 수행 (라우터에서 변경 가능)
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()