# /backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. CORS 미들웨어 임포트
from . import services, models

app = FastAPI()

# --- 2. CORS 미들웨어 설정 ---
# 허용할 출처 목록
origins = [
    "http://localhost:5173", # Vue.js 개발 서버 주소
    "http://localhost:8080", # vue-cli의 기본 개발 서버 주소
    # 추가적으로 허용할 프론트엔드 주소가 있다면 여기에 추가
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # origins 목록에 있는 출처의 요청을 허용
    allow_credentials=True,      # 요청에 쿠키를 포함할지 여부
    allow_methods=["*"],         # 모든 HTTP 메소드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],         # 모든 HTTP 헤더 허용
)
# ---------------------------

@app.post("/api/analyze", response_model=models.AnalysisResult)
async def analyze_abstract(data: models.AbstractInput):
    result = await services.run_analysis(data.title, data.text)
    return result

@app.get("/")
def read_root():
    return {"message": "AI Abstract Detector API is running."}