# CrewAI 연습 프로젝트

이 디렉토리는 CrewAI 학습을 위한 연습 예제들을 포함합니다.

## 시작하기

### 1. 환경 설정

```bash
# 가상환경 활성화
source ../VENV/bin/activate

# 패키지 설치
pip install -r ../requirements.txt
```

### 2. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 API 키를 추가하세요:

```env
OPENAI_API_KEY=your_api_key_here
```

### 3. 예제 실행

각 예제는 순서대로 실행하세요:

```bash
# 예제 1: 기본 Agent
python 01_basic_agent.py

# 예제 2: Task 할당
python 02_task_assignment.py

# 예제 3: 여러 Agent 협업
python 03_multi_agent.py
```

## 학습 순서

자세한 학습 플랜은 [CREWAI_PRACTICE_PLAN.md](./CREWAI_PRACTICE_PLAN.md)를 참고하세요.

1. **기초 단계**: Agent, Task, Crew 기본 개념
2. **중급 단계**: Tools, Memory, Process 최적화
3. **고급 단계**: 커스텀 LLM, 복잡한 워크플로우
4. **실전 프로젝트**: 실제 비즈니스 시나리오 구현

## 참고사항

- 각 예제는 독립적으로 실행 가능합니다
- API 키가 필요합니다 (OpenAI, Anthropic 등)
- 실행 시간은 LLM 응답 시간에 따라 다를 수 있습니다

