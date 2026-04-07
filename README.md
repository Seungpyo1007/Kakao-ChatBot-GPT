# Kakao-ChatBot-GPT

카카오톡 챗봇과 OpenAI의 GPT-4를 연동하여 스마트한 대화형 서비스를 제공하는 프로젝트입니다.

## 주요 기능

- **OpenAI GPT-4 연동**: 최신 언어 모델인 GPT-4 Turbo를 사용하여 고품질의 답변을 생성합니다.
- **카카오톡 챗봇 연동**: 카카오 i 오픈빌더를 통해 카카오톡 채널에서 바로 대화할 수 있습니다.
- **도메인 특화 응답**: 특정 분야(예: 날씨 전문가)에 맞춘 전문적인 답변을 제공하도록 설정되어 있습니다.
- **비동기 처리 구조**: 카카오톡의 5초 응답 제한을 고려하여 질문 접수와 답변 확인을 분리한 구조를 가지고 있습니다.

## 🛠 기술 스택

- **Backend**: Python, Flask
- **AI**: OpenAI GPT-4 Turbo
- **Environment**: python-dotenv for secure configuration

## 📋 설치 및 실행 방법

### 1. 프로젝트 클론
```bash
git clone https://github.com/Seungpyo1007/Kakao-ChatBot-GPT.git
cd Kakao-ChatBot-GPT
```

### 2. 의존성 설치
필요한 라이브러리를 설치합니다.
```bash
pip install flask requests python-dotenv openai
```

### 3. 환경 변수 설정
`test` 폴더 내의 `env` 파일(또는 `.env`로 변경 권장)에 본인의 OpenAI API 키를 입력합니다.
```text
OPENAI_API_KEY=your_api_key_here
```

### 4. 서버 실행
```bash
python test/application_ai.py
```

## 💬 서비스 흐름

1. **질문 (/question)**: 유저가 카카오톡으로 질문을 전송하면 GPT-4가 답변을 생성하기 시작합니다.
2. **답변 (/ans)**: 유저가 "답변 확인" 등의 버튼을 누르면 생성된 AI의 답변을 출력합니다.

## 📄 라이선스

이 프로젝트는 [MIT License](LICENSE)에 따라 라이선스가 부여됩니다.
