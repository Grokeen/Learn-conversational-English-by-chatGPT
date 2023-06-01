

Day 1
=======
# D-jango install
## 가상 환경 설정:
가상 환경을 설정하는 것은 권장되는 방법입니다. 가상 환경을 사용하면 프로젝트 별로 독립적인 환경을 구성할 수 있습니다. 다음 명령을 통해 가상 환경을 만들고 활성화합니다:

python3 -m venv myenv     # 가상 환경 생성
source myenv/bin/activate    # 가상 환경 활성화 (Windows에서는 'myenv\Scripts\activate'를 사용)

## Django 설치:
가상 환경이 활성화된 상태에서 다음 명령을 통해 Django를 설치합니다:

pip3 install django

## Django 프로젝트 생성:
다음 명령을 통해 Django 프로젝트를 생성합니다:

django-admin startproject projct_LCE

## 애플리케이션 생성:
프로젝트 디렉토리로 이동한 후, 다음 명령을 통해 Django 애플리케이션을 생성합니다:

cd projct_LCE
python3 manage.py startapp myapp

## 설정 변경:
myproject/settings.py 파일에서 데이터베이스 설정 등 필요한 설정을 변경합니다.

## 모델 정의:
myapp/models.py 파일에서 애플리케이션에 필요한 모델을 정의합니다.

## 데이터베이스 마이그레이션:
다음 명령을 통해 모델 변경 사항을 데이터베이스에 적용합니다:

python manage.py makemigrations
python manage.py migrate

## 개발 서버 실행:
다음 명령을 통해 개발 서버를 실행하여 웹 애플리케이션을 확인할 수 있습니다:

python3 manage.py runserver

### django 에러 발생
python3 -m pip install --upgrade pip
pip3 install django

## 이제 브라우저에서 http://localhost:8000에 접속하여 Django 기본 화면을 확인할 수 있습니다.

완료.