from flask import Flask, jsonify, request
import requests, json, os
from dotenv import load_dotenv
import openai

# 환경 변수 로드
load_dotenv()

application = Flask(__name__)
responses = {}

# 환경 변수에서 OpenAI API 키 가져오기
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# OpenAI API 키 설정
if OPENAI_API_KEY:
    openai.api_key = OPENAI_API_KEY
else:
    raise ValueError("OpenAI API 키가 제공되지 않았습니다. .env 파일에 OPENAI_API_KEY를 설정하세요.")

@application.route("/question", methods=["POST"])
def get_question():
    global responses
    request_data = json.loads(request.get_data(), encoding='utf-8')
    user_id = request_data['userRequest']['user']['id']
    question = request_data['action']['params']['question']
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": f"질문을 받았습니다. AI에게 물어보고 올게요!: {question}"
                }
            }]
        }
    }
    
    responses[user_id] = '아직 AI가 처리 중이에요'
    
    try:
        # 도메인 특화된 프롬프트 설정
        domain_specific_prompt = f"""
        당신은 한국의 날씨 전문가입니다. 사용자가 날씨에 대해 물어보면 전문가의 입장에서 대답해주세요.
        사용자: {question}
        """
        
        # OpenAI API 호출
        gpt_response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": domain_specific_prompt}],
            max_tokens=800,
            n=1,  # 생성할 응답의 수
            stop=None,  # 응답 종료를 위한 문자열 (없음)
            temperature=0.7,  # 응답의 창의성 조절 (0.0 ~ 1.0)
        )
        
        bot_message = gpt_response['choices'][0]['message']['content'].strip()
        responses[user_id] = bot_message
    except Exception as e:
        responses[user_id] = f'실패했습니다: {str(e)}'
    
    return jsonify(response)


@application.route("/ans", methods=["POST"])
def hello2():
    global responses
    request_data = json.loads(request.get_data(), encoding='utf-8')
    user_id = request_data['userRequest']['user']['id']
    
    response = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": f"답변: {responses.get(user_id, '질문을 하신 적이 없어 보여요. 질문부터 해주세요.')}"
                }
            }]
        }
    }
    
    return jsonify(response)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
