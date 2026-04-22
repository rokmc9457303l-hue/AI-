"AI 활용 업무 생산성 향import requests
import json
import os
from datetime import datetime

# --- 설정 (P-Reinforce 규격) ---
LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
VAULT_PATH = r"C:\Users\admin\Downloads\AI-Project\10_Wiki\🛠️ Projects"

def run_analysis(topic, urls):
    print("\n🚀 P-Reinforce 유튜브 전략 엔진 가동 중...")
    
    prompt = f"""
    너는 최고의 유튜브 전략가이자 심리학자다. 
    아래 주제와 경쟁 채널 URL들을 분석하여 벤치마킹 마스터플랜을 짜라.
    
    주제: {topic}
    경쟁 URL: {urls}
    
    구조:
    1. Hook Strategy (초반 30초 전략)
    2. Storytelling Flow (영상 전개 구조)
    3. Thumbnail Design (클릭률 극대화 썸네일 카피 및 구도)
    4. Master Plan Workflow (최종 실행 단계)
    
    응답은 반드시 마크다운 형식으로 작성하라.
    """

    payload = {
        "model": "model-identifier",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()['choices'][0]['message']['content']
        
        # 파일 저장
        filename = f"유튜브_전략_리포트_{datetime.now().strftime('%m%d_%H%M')}.md"
        filepath = os.path.join(VAULT_PATH, filename)
        
        # P-Reinforce 템플릿 적용
        template = f"""---
id: {datetime.now().timestamp()}
category: "[[10_Wiki/🛠️ Projects]]"
confidence_score: 0.98
last_reinforced: {datetime.now().strftime('%Y-%m-%d')}
---

# [[{topic} - 벤치마킹 리포트]]

{result}

## 🔗 지식 연결
- Related: [[유튜브_롱폼_마스터_워크플로우]]
"""
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(template)
            
        print(f"\n✅ 분석 완료! 파일이 생성되었습니다: {filepath}")
        
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        print("💡 안내: LM Studio에서 'AI Server'를 시작했는지 다시 확인해주세요.")

if __name__ == "__main__":
    print("--- TubeBench AI 마스터 전략기 ---")
    u_topic = input("분석할 주제를 입력하세요: ")
    u_urls = input("유튜브 URL(들)을 입력하세요: ")
    run_analysis(u_topic, u_urls)
