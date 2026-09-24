# FastAPI 라이브러리에서 FastAPI 클래스를 가져온다.
from fastapi import FastAPI

# "앱"을 하나 만든다. 이 app이 식당의 '주방' 역할을 한다.
app = FastAPI(title="의도-엔티티 분류기 백엔드")


# @app.get("/health") 는 "GET 방식으로 /health 주소가 호출되면
# 바로 아래 함수를 실행해라"라는 뜻이다. (이런 @ 표시를 '데코레이터'라고 부른다)
@app.get("/health")
def health():
    # 파이썬 딕셔너리를 반환하면 FastAPI가 자동으로 JSON으로 바꿔서 응답한다.
    return {"status": "ok"}
