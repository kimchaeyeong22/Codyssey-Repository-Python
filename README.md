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



### 브랜치 생성 및 병합 실습

- `feature/readme-improvements` 브랜치를 생성했습니다.
- 해당 브랜치에서 README 개선 작업을 진행했습니다.
- 작업 완료 후 `main` 브랜치에 Fast-forward 방식으로 병합했습니다.
- `git log --oneline --graph --decorate --all` 명령어로 브랜치 및 커밋 이력을 확인했습니다.
- 관련 실행 화면은 `screenshots/07_git_branch_merge_history.png`에 첨부했습니다.



### Git clone 및 pull 실습 증빙

- `git clone` 명령어를 사용하여 GitHub 원격 저장소를 새로운 로컬 폴더에 복제했습니다.
- 복제 결과 저장소 데이터 수신 및 변경 사항 처리가 정상적으로 완료되었습니다.
- 복제한 저장소 폴더에서 `git pull origin main` 명령어를 실행했습니다.
- `Already up to date.` 메시지를 확인하여 원격 저장소의 최신 변경 사항이 이미 반영되어 있음을 확인했습니다.

**실행 증빙 스크린샷**
- `screenshots/08_git_clone.png`: 원격 저장소 복제 실행 결과
- `screenshots/09_git_pull.png`: 원격 저장소 변경 사항 가져오기 실행 결과


## 클래스 구성 및 역할

프로그램은 Quiz와 QuizGame 두 개의 클래스로 구성되어 있으며, 각 클래스가 서로 다른 책임을 담당하도록 분리했습니다.

### 1. Quiz 클래스 (`quiz.py`)

- 퀴즈 한 문제의 데이터를 관리하는 문제 모델 클래스입니다.
- 질문(question), 선택지(choices), 정답(answer)을 저장합니다.
- `display()` 메서드를 통해 질문과 선택지를 화면에 출력합니다.
- `check_answer()` 메서드를 통해 사용자가 입력한 답이 정답인지 확인합니다.

### 2. QuizGame 클래스 (`quiz_game.py`)

- 퀴즈 게임 전체의 흐름을 관리하는 클래스입니다.
- 여러 Quiz 객체를 목록으로 관리합니다.
- 퀴즈 실행, 새 퀴즈 추가, 퀴즈 목록 출력, 최고 점수 확인 기능을 담당합니다.
- JSON 파일을 이용해 퀴즈 데이터와 최고 점수를 저장하고 불러옵니다.
- 사용자 메뉴 입력을 처리하고 프로그램의 실행 및 종료를 관리합니다.

### 클래스 간 관계

QuizGame은 여러 개의 Quiz 객체를 보유하고 활용합니다. Quiz는 개별 문제의 데이터와 정답 확인을 담당하고, QuizGame은 이러한 Quiz 객체들을 이용해 전체 게임을 진행합니다.