# /backend/app/services.py
import time # 임시로 시간 지연을 만들기 위해
import asyncio
async def run_analysis(title: str, original_text: str):
    print(f"분석 시작: {title}")

    # [1단계] LLM API로 초록 20개 생성 (지금은 임시 데이터)
    ai_abstracts = await generate_abstracts_mock(title)

    # [2단계] 의미 벡터 변환 (지금은 생략)

    # [3단계] 유사도 계산 (지금은 임의의 값)
    avg_score = 0.9123

    # [4단계] 최종 판별
    is_ai = avg_score > 0.85 # 임계값

    print(f"분석 완료: 평균 유사도 {avg_score}")
    return {
        "is_ai_generated": is_ai,
        "average_similarity": avg_score,
        "message": "AI가 작성한 초록으로 강하게 의심됩니다." if is_ai else "사람이 작성한 초록으로 보입니다."
    }

async def generate_abstracts_mock(title: str):
    # 실제 API 호출을 흉내 내기 위해 잠시 대기
    await asyncio.sleep(2)
    return [f"'{title}'에 대한 AI 생성 초록 {i+1}" for i in range(20)]