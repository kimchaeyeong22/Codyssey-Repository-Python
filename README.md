# Python Quiz Game

## 1. 프로젝트 개요

Python으로 제작한 콘솔 기반 퀴즈 게임입니다.

사용자는 퀴즈를 풀고, 새로운 퀴즈를 추가하며, 최고 점수를 확인할 수 있습니다.

## 2. 주제 및 선정 이유

- 주제: 개발 및 컴퓨터 기초 상식
- 선정 이유: Python 프로그래밍과 컴퓨터 관련 기초 지식을 퀴즈 형식으로 학습하기 위해 선정했습니다.

## 3. 실행 방법

Python 3.10 이상이 필요합니다.

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
python main.py
```

## 4. 주요 기능

1. **퀴즈 풀기**: 저장된 퀴즈를 풀고 점수를 확인합니다.
2. **퀴즈 추가하기**: 질문, 4개의 선택지, 정답을 입력하여 새로운 퀴즈를 추가합니다.
3. **퀴즈 목록 보기**: 등록된 퀴즈 목록을 확인합니다.
4. **최고 점수 보기**: 지금까지 기록된 최고 점수를 확인합니다.
5. **데이터 저장 및 불러오기**: 퀴즈와 최고 점수를 JSON 파일에 저장하고 다시 불러옵니다.
6. **입력 오류 처리**: 빈 입력, 숫자가 아닌 입력, 범위를 벗어난 입력을 검사합니다.

## 5. 파일 구조

```text
python-quiz-game/
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
├── README.md
├── .gitignore
└── screenshots/
```

## 6. state.json 설명

`state.json`은 퀴즈 데이터와 최고 점수를 저장하는 JSON 파일입니다.

- `quizzes`: 질문, 선택지, 정답 정보
- `best_score`: 지금까지 기록된 최고 점수

프로그램을 처음 실행하면 기본 퀴즈 데이터가 생성됩니다. 이후 퀴즈를 추가하거나 점수가 갱신되면 데이터가 자동으로 저장됩니다.




## 테스트 실행

프로젝트에 포함된 자동 테스트를 실행하려면 터미널에서 다음 명령어를 입력합니다.

```bash
python -m unittest -v
현재 다음 항목을 자동으로 검사합니다.
- 퀴즈 질문 저장 여부
- 선택지 개수 확인
- 정답 판별 기능
- 오답 판별 기능
- 기본 퀴즈 개수 확인
모든 테스트가 통과하면 OK 메시지가 출력됩니다.



## Git 실습 기록

- git clone을 사용하여 원격 저장소를 복제했습니다.
- git pull을 사용하여 원격 저장소의 변경 사항을 가져오는 실습을 진행합니다.


## 이하 추가 내용
## GitHub 저장소 및 커밋 기록 
https://github.com/kimchaeyeong22/Codyssey-Repository-Python.git
### 커밋 기록
* 8792999 (HEAD -> main, origin/main) Add new screenshots
* 82bf234 Add new screenshots
* f7debe9 Document git clone and pull practice
* c44b9b3 Improve quiz display test assertions
* 3b24403 Add type hints to Quiz class
* 15d5cb9 Add quiz display test
* b006649 Add unit tests for quiz functionality
* 65346d0 Document automated tests
* 8b6149b (feature/readme-improvements) Update project files
* afb7410 Update project files
* b225fd4 Update project files
* 5230adb Add Quiz class
* 1d9949f Update project files