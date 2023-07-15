

Day2
=====
# 23년 6월 1일 새로 만든 토큰
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

# 23년 6월 5일 새로 만든 토큰
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

# 23년 6월 26일 새로 만든 토큰
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

# my SQL 설치해보자
## MySQL 설치:
터미널에서 다음 명령어를 실행하여 MySQL을 설치합니다:

brew install mysql

## MySQL 서비스 시작:
설치가 완료되면 다음 명령어를 사용하여 MySQL 서비스를 시작합니다:

brew services start mysql

## 초기 설정:
다음 명령어로 MySQL 보안 설정을 실행합니다:

mysql_secure_installation

이 명령어를 실행하면 MySQL의 루트 비밀번호를 설정하고, 보안 관련 설정을 변경할 수 있습니다. 지시에 따라 원하는 설정을 선택하십시오.
8자리로 선택하여 20165270 으로 설정.

### 서버 실행 없이 위 명령어 실행 안됨

## MySQL 접속:
MySQL 서버가 실행 중인지 확인하려면 다음 명령어를 실행합니다:

brew services list

## MySQL 서버가 실행 중인 경우, 다음 명령어로 MySQL에 접속할 수 있습니다:
위 명령어를 실행하면 비밀번호를 입력하라는 프롬프트가 나타납니다. 초기 설정 단계에서 설정한 루트 비밀번호를 입력하십시오.

mysql -u root -p
20165270

완료.