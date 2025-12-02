"""
CrewAI 기초 연습 1: 첫 번째 Agent 만들기

이 예제는 CrewAI의 가장 기본적인 개념을 학습합니다:
- Agent 생성
- Role, Goal, Backstory 설정
- Task 생성 및 실행
"""

from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# API 키 확인
if not os.getenv("OPENAI_API_KEY"):
    print("⚠️  OPENAI_API_KEY가 설정되지 않았습니다.")
    print("   .env 파일에 OPENAI_API_KEY를 추가해주세요.")
    exit(1)


def main():
    """기본 Agent 예제 실행"""
    
    # 1. Agent 생성
    researcher = Agent(
        role="연구원",
        goal="주어진 주제에 대해 정확하고 상세한 정보를 수집하고 분석한다",
        backstory="당신은 경험이 풍부한 연구원으로, 다양한 주제에 대해 깊이 있는 조사를 수행합니다. "
                  "신뢰할 수 있는 소스에서 정보를 수집하고, 객관적이고 정확한 분석을 제공합니다.",
        verbose=True,  # 작업 과정을 자세히 출력
        allow_delegation=False  # 다른 Agent에게 작업을 위임하지 않음
    )
    
    # 2. Task 생성
    research_task = Task(
        description="'인공지능의 미래'라는 주제에 대해 최신 동향과 주요 기술을 조사하고, "
                   "500자 이내로 요약을 작성하세요.",
        agent=researcher,
        expected_output="주제에 대한 조사 결과를 500자 이내로 요약한 텍스트"
    )
    
    # 3. Crew 생성 및 실행
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=True  # 전체 프로세스를 자세히 출력
    )
    
    print("🚀 CrewAI 작업을 시작합니다...\n")
    result = crew.kickoff()
    
    print("\n" + "="*50)
    print("📊 작업 결과:")
    print("="*50)
    print(result)
    print("="*50)


if __name__ == "__main__":
    main()


