# CrewAI 연습 플랜

## 📋 목차
1. [환경 설정](#1-환경-설정)
2. [기초 단계](#2-기초-단계)
3. [중급 단계](#3-중급-단계)
4. [고급 단계](#4-고급-단계)
5. [실전 프로젝트](#5-실전-프로젝트)

---

## 1. 환경 설정

### 1.1 필수 패키지 설치
```bash
# 가상환경 활성화
source VENV/bin/activate

# CrewAI 및 관련 패키지 설치
pip install crewai
pip install crewai[tools]  # 도구 지원
pip install langchain-openai  # OpenAI LLM 사용 시
pip install langchain-community  # 다양한 LLM 지원
pip install python-dotenv  # 환경 변수 관리
```

### 1.2 환경 변수 설정
`.env` 파일 생성 및 API 키 설정:
```
OPENAI_API_KEY=your_api_key_here
# 또는 다른 LLM 제공자
ANTHROPIC_API_KEY=your_key_here
```

---

## 2. 기초 단계

### 2.1 첫 번째 Agent 만들기
**목표**: 단일 Agent로 기본 작업 수행하기

**연습 내용**:
- Agent 클래스 이해
- Role, Goal, Backstory 설정
- 간단한 Task 생성 및 실행

**예제 프로젝트**: `practice/01_basic_agent.py`
- 역할: 연구원
- 목표: 주어진 주제에 대해 정보 수집
- 작업: 특정 주제에 대한 요약 작성

### 2.2 Task와 Agent 연결하기
**목표**: Task를 Agent에게 할당하고 실행하기

**연습 내용**:
- Task 클래스 사용법
- Agent-Task 매핑
- Crew 생성 및 실행

**예제 프로젝트**: `practice/02_task_assignment.py`
- 여러 Task를 하나의 Agent에게 할당
- Task 간 의존성 이해

### 2.3 여러 Agent 협업하기
**목표**: 여러 Agent가 협력하여 작업 수행

**연습 내용**:
- Crew 클래스로 여러 Agent 관리
- Agent 간 작업 흐름 설계
- 순차적/병렬 작업 처리

**예제 프로젝트**: `practice/03_multi_agent.py`
- 역할: 연구원, 작가, 편집자
- 워크플로우: 연구 → 작성 → 편집

---

## 3. 중급 단계

### 3.1 Tools 통합하기
**목표**: 외부 도구를 Agent에게 제공하기

**연습 내용**:
- CrewAI Tools 사용법
- 커스텀 Tool 만들기
- 웹 검색, 파일 읽기/쓰기 등

**예제 프로젝트**: `practice/04_tools_integration.py`
- 웹 검색 Tool 사용
- 파일 시스템 Tool 사용
- 커스텀 Calculator Tool 만들기

### 3.2 Memory와 Context 관리
**목표**: Agent가 이전 대화나 작업을 기억하도록 하기

**연습 내용**:
- Memory 시스템 이해
- Context 전달 방법
- 장기 기억 vs 단기 기억

**예제 프로젝트**: `practice/05_memory_management.py`
- 대화 기록 유지
- 이전 작업 결과 재사용

### 3.3 Process와 Workflow 최적화
**목표**: 작업 프로세스 효율화하기

**연습 내용**:
- Sequential Process
- Hierarchical Process
- Consensual Process
- 작업 우선순위 설정

**예제 프로젝트**: `practice/06_process_optimization.py`
- 다양한 Process 타입 비교
- 최적의 워크플로우 설계

---

## 4. 고급 단계

### 4.1 커스텀 LLM 통합
**목표**: 다양한 LLM 제공자 사용하기

**연습 내용**:
- OpenAI, Anthropic, Ollama 등 통합
- LLM 설정 최적화
- 비용 및 성능 고려

**예제 프로젝트**: `practice/07_custom_llm.py`
- 여러 LLM 제공자 비교
- 모델별 특성 이해

### 4.2 복잡한 워크플로우 설계
**목표**: 실제 비즈니스 시나리오 모델링

**연습 내용**:
- 조건부 작업 흐름
- 에러 핸들링
- 재시도 로직
- 병렬 처리 최적화

**예제 프로젝트**: `practice/08_complex_workflow.py`
- 마케팅 캠페인 자동화
- 제품 리뷰 분석 파이프라인

### 4.3 모니터링과 로깅
**목표**: Agent 작업 추적 및 디버깅

**연습 내용**:
- CrewAI 로깅 시스템
- 작업 진행 상황 모니터링
- 성능 메트릭 수집

**예제 프로젝트**: `practice/09_monitoring.py`
- 작업 실행 시간 측정
- 에러 로그 분석

---

## 5. 실전 프로젝트

### 5.1 콘텐츠 생성 팀
**프로젝트**: 블로그 포스트 자동 생성 시스템
- **Agent**: 리서처, 작가, 편집자, SEO 전문가
- **기능**: 주제 연구 → 초안 작성 → 편집 → SEO 최적화

### 5.2 데이터 분석 팀
**프로젝트**: 데이터 분석 및 리포트 생성
- **Agent**: 데이터 수집가, 분석가, 리포트 작성자
- **기능**: 데이터 수집 → 분석 → 시각화 → 리포트 작성

### 5.3 고객 지원 팀
**프로젝트**: 자동 고객 지원 시스템
- **Agent**: 티켓 분류자, 기술 지원, 에스컬레이션 관리자
- **기능**: 티켓 분류 → 문제 해결 → 필요시 에스컬레이션

### 5.4 소프트웨어 개발 팀
**프로젝트**: 코드 리뷰 및 문서화 자동화
- **Agent**: 코드 리뷰어, 테스터, 문서 작성자
- **기능**: 코드 분석 → 테스트 케이스 생성 → 문서 작성

---

## 📚 학습 리소스

### 공식 문서
- [CrewAI 공식 문서](https://docs.crewai.com/)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewAI)

### 추천 학습 순서
1. **Week 1**: 기초 단계 (2.1 ~ 2.3)
2. **Week 2**: 중급 단계 (3.1 ~ 3.3)
3. **Week 3**: 고급 단계 (4.1 ~ 4.3)
4. **Week 4**: 실전 프로젝트 (5.1 ~ 5.4 중 선택)

### 체크리스트
- [ ] 환경 설정 완료
- [ ] 첫 번째 Agent 만들기
- [ ] Task와 Agent 연결하기
- [ ] 여러 Agent 협업하기
- [ ] Tools 통합하기
- [ ] Memory 관리하기
- [ ] Process 최적화하기
- [ ] 커스텀 LLM 통합하기
- [ ] 복잡한 워크플로우 설계하기
- [ ] 모니터링 시스템 구축하기
- [ ] 실전 프로젝트 완성하기

---

## 💡 팁

1. **작은 것부터 시작**: 복잡한 시스템보다는 간단한 예제부터 시작하세요.
2. **로그 확인**: Agent의 작업 과정을 자세히 로깅하여 이해도를 높이세요.
3. **에러 처리**: 각 단계에서 발생할 수 있는 에러를 미리 고려하세요.
4. **비용 관리**: LLM API 호출 비용을 모니터링하세요.
5. **커뮤니티 활용**: CrewAI Discord나 GitHub Discussions를 적극 활용하세요.

---

## 🎯 다음 단계

각 단계를 완료한 후:
1. 코드를 `practice/` 디렉토리에 저장
2. 각 예제에 대한 README 작성
3. 실행 결과와 학습 내용 기록
4. 다음 단계로 진행

**행운을 빕니다! 🚀**

