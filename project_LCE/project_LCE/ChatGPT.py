from django.test import TestCase
import os

# 2306161759 김용록 Chat GPT를 사용하기 위한 API 라이브러리.
import openai

# 2310251851 김용록 예외처리 라이브러리
import subprocess

# 2308211801 김용록 OpenAI API 키 .gitignore 설정.
from dotenv import load_dotenv 
    # pip3 install python-dotenv
    # 만약에 경고가 뜬다면 : python3 -m pip install --upgrade pip

try:
    load_dotenv() 
        # env 파일을 읽기 위해 키-값 쌍을 현재 작업 환경의 환경 변수로 로드하는 역할.
    openAiApi_key = os.getenv("API_KEY")

    # 2306161759 김용록 OpenAI API 유료 키 설정.
    openai.api_key = openAiApi_key


    # 2306161800 김용록 chating 관련 코드.
    def chat_with_gpt3(prompt):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            n=1,
            stop=None,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()

    # 2306161801 김용록 voice 관련 코드.
    # https://platform.openai.com/docs/guides/speech-to-text 참고
    def chat_with_voice():
        audio_file= open("/path/to/file/audio.mp3", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # 2306161800 김용록 대화 예제 코드.
    def chat_start():
        # 2306161804 김용록 input 값을 나의 목소리 인식할 수 있게 변경.
        user_input = ''
        while user_input != 'bye': # bye 라고 하면 대화 끝
            # custom_instruction = "You are a English teacher in Korea. If i said i don't know, You have to help me in Korean or English."

            user_input = input('사용자: ')
            prompt = f'User: {user_input}\n AI:'
            ai_response = chat_with_gpt3(prompt)
            print('AI:', ai_response)

        


except subprocess.CalledProcessError as e:
    print("에러 발생 code : ", e.returncode ,"\n")
    print("에러 stderr : ", e.stderr)

def __init__():
    chat_start()