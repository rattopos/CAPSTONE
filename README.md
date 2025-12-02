# CAPSTONE

## CrewAI 연습 프로젝트

이 프로젝트는 CrewAI 프레임워크를 학습하고 연습하기 위한 저장소입니다.

### 빠른 시작

1. **환경 설정**
   ```bash
   # 가상환경 활성화
   source VENV/bin/activate
   
   # 패키지 설치
   pip install -r requirements.txt
   ```

2. **환경 변수 설정**
   - 프로젝트 루트에 `.env` 파일 생성
   - `OPENAI_API_KEY=your_api_key_here` 추가

3. **연습 시작**
   ```bash
   cd practice
   python 01_basic_agent.py
   ```

### 학습 자료

- **상세한 연습 플랜**: [`practice/CREWAI_PRACTICE_PLAN.md`](./practice/CREWAI_PRACTICE_PLAN.md)
- **예제 코드**: [`practice/`](./practice/) 디렉토리
- **시작 가이드**: [`practice/README.md`](./practice/README.md)

### 학습 단계

1. **기초**: Agent, Task, Crew 기본 개념
2. **중급**: Tools, Memory, Process 최적화
3. **고급**: 커스텀 LLM, 복잡한 워크플로우
4. **실전**: 실제 비즈니스 시나리오 구현

자세한 내용은 [연습 플랜](./practice/CREWAI_PRACTICE_PLAN.md)을 참고하세요.
