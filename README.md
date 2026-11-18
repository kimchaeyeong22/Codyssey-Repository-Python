# Python Quiz Game

## 0. 사전 지식 및 주요 용어

프로젝트의 구조와 실행 방법을 이해하기 위해 필요한 기본 용어와 주요 명령어를 정리했습니다.

### 0-1. 주요 용어

| 용어 | 설명 |
|---|---|
| Python | 프로그램을 작성하고 실행하는 프로그래밍 언어 |
| 콘솔(Console) | 명령어를 입력하고 프로그램 실행 결과를 확인하는 환경 |
| 클래스(Class) | 데이터와 기능을 하나로 묶어 정의한 설계도 |
| 객체(Object) | 클래스를 바탕으로 생성된 실제 데이터와 기능의 단위 |
| 메서드(Method) | 클래스 내부에 정의된 함수 |
| JSON | 데이터를 키(Key)와 값(Value)의 형태로 표현하는 데이터 형식 |
| 예외 처리(Exception Handling) | 실행 중 발생하는 오류에 대응하는 방법 |
| Git | 소스 코드의 변경 이력을 기록하고 관리하는 버전 관리 시스템 |
| GitHub | Git 저장소를 온라인에서 관리하고 공유하는 플랫폼 |
| 저장소(Repository) | 프로젝트 파일과 변경 이력을 관리하는 공간 |
| 커밋(Commit) | 파일의 변경 사항을 기록하는 작업 |
| 브랜치(Branch) | 기존 작업 흐름과 분리하여 개발할 수 있는 작업 공간 |
| 인코딩(Encoding) | 문자를 컴퓨터가 저장하고 해석할 수 있는 데이터로 표현하는 방식 |

### 0-2. 주요 명령어

| 명령어 | 설명 |
|---|---|
| `python main.py` | Python 프로그램 실행 |
| `python -m unittest -v` | 자동 테스트 실행 및 상세 결과 확인 |
| `git status` | 현재 Git 작업 상태 확인 |
| `git add .` | 변경된 파일을 커밋 대상으로 추가 |
| `git commit -m "메시지"` | 변경 사항을 커밋으로 기록 |
| `git push` | 로컬 커밋을 원격 저장소에 업로드 |
| `git clone` | 원격 저장소를 로컬 컴퓨터에 복제 |
| `git pull` | 원격 저장소의 변경 사항을 가져와 로컬 작업에 반영 |
| `Get-Content .\README.md -Encoding UTF8` | PowerShell에서 UTF-8 인코딩으로 README 파일 내용 확인 |

### 0-3. 참고 사항

- Python 명령어는 프로젝트 폴더에서 실행합니다.
- Git 명령어는 해당 프로젝트의 Git 저장소에서 실행합니다.
- PowerShell 명령어는 Windows 터미널 환경에서 사용합니다.
- JSON 파일은 프로그램의 데이터를 저장하고 다시 불러오는 데 사용합니다.

## 1. 프로젝트 개요

Python을 활용하여 개발한 콘솔 기반 퀴즈 게임입니다. VS Code에서 코드를 작성하고, JSON 파일을 활용하여 퀴즈 관리 및 데이터 저장 기능을 구현했습니다.

사용자는 퀴즈 풀기, 새로운 퀴즈 추가, 등록된 퀴즈 목록 확인 및 최고 점수 조회 기능을 이용할 수 있습니다.

## 2. 주제 및 선정 이유

- 주제: 개발 및 컴퓨터 기초 상식
- 선정 이유: 지금 진행하고 있는 미션과 가까운 주제로 하고 싶었으며 Python 프로그래밍과 컴퓨터 관련 기초 지식을 퀴즈 형식으로 학습하기 위해 선정했습니다.


## 3. 실행 방법

**실행 환경**
- Python 3.10 이상
- VS Code 또는 터미널(PowerShell, CMD 등)

**실행 순서**

1. 프로젝트 저장소를 내려받거나 프로젝트 폴더를 엽니다.
2. 터미널에서 프로젝트 폴더로 이동합니다.
3. 다음 명령어를 실행합니다.

```bash
python main.py
```

프로그램이 실행되면 콘솔 메뉴가 표시되며, 원하는 기능을 선택하여 퀴즈 게임을 이용할 수 있습니다.



## 4. 주요 기능

1. **퀴즈 풀기**: 저장된 퀴즈를 풀고 점수를 확인합니다.
2. **퀴즈 추가하기**: 질문, 4개의 선택지, 정답을 입력하여 새로운 퀴즈를 추가합니다.
3. **퀴즈 목록 보기**: 등록된 퀴즈 목록을 확인합니다.
4. **최고 점수 보기**: 지금까지 기록된 최고 점수를 확인합니다.
5. **데이터 저장 및 불러오기**: 퀴즈와 최고 점수를 JSON 파일에 저장하고 다시 불러옵니다.
6. **입력 오류 처리**: 빈 입력, 숫자가 아닌 입력, 범위를 벗어난 입력을 검사합니다.

<img width="896" height="421" alt="01_main_menu" src="https://github.com/user-attachments/assets/2ef64e49-0b25-44a4-82dc-6120aa3ffc11" />


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

<img width="974" height="963" alt="JSON" src="https://github.com/user-attachments/assets/6575626f-7a4a-429b-a9e4-d06e8cbb68a5" />

## 6-1. 클래스 구성 및 역할

프로그램은 Quiz와 QuizGame 두 개의 클래스로 구성되어 있으며, 각 클래스가 서로 다른 책임을 담당하도록 분리했습니다.

### 6-1-1. Quiz 클래스 (`quiz.py`)

- 퀴즈 한 문제의 데이터를 관리하는 문제 모델 클래스입니다.
- 질문(question), 선택지(choices), 정답(answer)을 저장합니다.
- `display()` 메서드를 통해 질문과 선택지를 화면에 출력합니다.
- `check_answer()` 메서드를 통해 사용자가 입력한 답이 정답인지 확인합니다.

<img width="410" height="310" alt="스크린샷 2026-11-10 122709" src="https://github.com/user-attachments/assets/d2be587f-a603-4bae-ad44-20ba87b076b2" />



### 6-1-2. QuizGame 클래스 (`quiz_game.py`)

- 퀴즈 게임 전체의 흐름을 관리하는 클래스입니다.
- 여러 Quiz 객체를 목록으로 관리합니다.
- 퀴즈 실행, 새 퀴즈 추가, 퀴즈 목록 출력, 최고 점수 확인 기능을 담당합니다.
- JSON 파일을 이용해 퀴즈 데이터와 최고 점수를 저장하고 불러옵니다.
- 사용자 메뉴 입력을 처리하고 프로그램의 실행 및 종료를 관리합니다.

<img width="648" height="835" alt="스크린샷 2026-11-10 130406" src="https://github.com/user-attachments/assets/42238fb3-59ba-4d95-af76-0d2d2145407e" />
<img width="548" height="824" alt="스크린샷 2026-11-10 130427" src="https://github.com/user-attachments/assets/a4214c09-890f-4c31-9355-4b67aaf8a50b" />
<img width="563" height="765" alt="스크린샷 2026-11-10 130443" src="https://github.com/user-attachments/assets/82966eee-ecc7-45fc-895f-2c779331951f" />
<img width="507" height="662" alt="스크린샷 2026-11-10 130456" src="https://github.com/user-attachments/assets/1089f5cc-e835-4444-9532-bcbc954b478c" />
<img width="571" height="699" alt="스크린샷 2026-11-10 130516" src="https://github.com/user-attachments/assets/6bc7d8fa-09a0-46a8-b0c4-c936e9b7a5d1" />


### 6-1-3. 클래스 간 관계 및 비교

`QuizGame`은 여러 개의 `Quiz` 객체를 리스트로 보유하며, 이 객체들을 활용하여 전체 게임을 진행합니다.

- **Quiz:** 개별 퀴즈 한 문제의 데이터를 관리합니다. 문제와 선택지, 정답을 저장하고 문제 출력 및 사용자의 답안이 정답인지 확인합니다.
- **QuizGame:** 퀴즈 게임 전체의 흐름을 관리합니다. 여러 `Quiz` 객체를 생성하고 활용하며, 퀴즈 진행, 점수 계산, 퀴즈 추가 및 목록 조회, JSON 데이터 저장과 불러오기를 담당합니다.

즉, `Quiz`가 개별 문제의 내용을 관리한다면, `QuizGame`은 여러 문제를 활용하여 게임이 정상적으로 진행되도록 관리하는 역할을 합니다.


<img width="539" height="164" alt="quiz와 quizgame 차이" src="https://github.com/user-attachments/assets/96cbbe6a-e5ba-4f71-9817-5a24a3716a08" />






## 6-2. 클래스 사용 이유 및 객체지향 설계

이 프로젝트는 객체지향 프로그래밍(OOP) 개념을 적용하여 `Quiz` 클래스와 `QuizGame` 클래스를 사용한다.

### 6-2-1. 추상화 (Abstraction)

클래스를 사용하면 관련 데이터와 기능을 하나로 묶어 관리할 수 있다.

- `Quiz` 클래스: 질문, 선택지, 정답 등의 퀴즈 데이터를 관리한다.
- `QuizGame` 클래스: 퀴즈 진행, 점수 계산, 퀴즈 추가 및 목록 관리 등의 게임 기능을 담당한다.

각 클래스는 자신의 역할에 필요한 데이터와 기능을 관리하므로 프로그램의 구조를 이해하고 유지보수하기 쉽다.

### 6-2-2. 재사용성 (Reusability)

클래스를 활용하면 동일한 구조와 기능을 여러 객체에서 재사용할 수 있다.

- `Quiz` 클래스로 여러 개의 퀴즈 객체를 생성할 수 있다.
- 각각의 퀴즈 객체는 동일한 데이터 구조와 기능을 공유하면서 서로 다른 질문과 정답을 가질 수 있다.
- `QuizGame` 클래스에 구현된 게임 기능을 재사용하여 새로운 퀴즈를 추가하거나 게임 기능을 확장할 수 있다.

### 6-2-3. 클래스 사용의 장점

- 코드의 중복을 줄이고 관리 효율성을 높인다.
- 데이터와 기능을 역할에 따라 구분하여 구조화한다.
- 기능 수정 및 추가가 쉬워 유지보수성이 향상된다.
- 향후 새로운 게임 기능을 추가할 때 기존 클래스를 활용할 수 있다.


## 6-3. 기능별 로직 분리 및 담당 메서드

프로그램의 기능을 입력 검증, 게임 진행, 데이터 입출력의 세 영역으로 구분하여 각 메서드가 담당하는 역할을 명확하게 구성했습니다.

### 6-3-1. 입력 검증 (Input Validation)

사용자의 입력이 올바른 형식과 범위인지 확인합니다.

- `QuizGame.run()`: 메뉴 번호의 빈 입력, 숫자가 아닌 입력, 1~5 범위를 벗어난 입력을 검사합니다.
- `QuizGame.play_quiz()`: 정답 번호가 비어 있거나 숫자가 아닌 경우, 선택지 범위를 벗어난 경우 다시 입력하도록 처리합니다.
- `QuizGame.add_quiz()`: 질문과 선택지의 빈 입력을 방지하고 정답 번호가 1~4 범위인지 검사합니다.

<img width="220" height="458" alt="스크린샷 2026-11-10 131048" src="https://github.com/user-attachments/assets/d23d5a35-c92c-4680-ab45-e8173c57dcaf" />


### 6-3-2. 게임 진행 (Game Flow)

퀴즈 실행과 사용자에게 제공되는 게임 기능을 관리합니다.

```
- `QuizGame.run()`: 메뉴를 출력하고 사용자가 선택한 기능을 실행합니다.
- `QuizGame.play_quiz()`: 퀴즈를 순서대로 출제하고 정답을 확인하여 점수를 계산합니다.
- `QuizGame.add_quiz()`: 새로운 퀴즈를 생성하고 목록에 추가합니다.
- `QuizGame.list_quizzes()`: 등록된 퀴즈 목록을 출력합니다.
- `QuizGame.show_best_score()`: 현재 최고 점수를 출력합니다.
- `Quiz.display()`: 개별 퀴즈의 질문과 선택지를 출력합니다.
- `Quiz.check_answer()`: 사용자의 답이 정답인지 확인합니다.
```

<img width="329" height="794" alt="스크린샷 2026-11-10 131250" src="https://github.com/user-attachments/assets/0cc04cb0-d3c2-4541-97db-30cb5502efe4" />

<img width="1117" height="1036" alt="스크린샷 2026-11-10 130546" src="https://github.com/user-attachments/assets/adb1a840-5093-4f63-a357-e16b18002179" />


### 6-3-3. 데이터 입출력 (Data I/O)

JSON 파일을 이용하여 퀴즈 데이터와 최고 점수를 저장하고 불러옵니다.
```
- `QuizGame.load_data()`: 프로그램 시작 시 `state.json` 파일을 읽어 퀴즈와 최고 점수를 불러옵니다. 파일이 없거나 데이터에 문제가 있으면 기본 퀴즈로 복구합니다.
- `QuizGame.save_data()`: 현재 퀴즈 목록과 최고 점수를 JSON 형식으로 저장합니다.
```

<img width="178" height="200" alt="스크린샷 2026-11-10 130850" src="https://github.com/user-attachments/assets/daedb0b5-023f-417c-a634-efe13ac34956" />


### 6-3-4. 로직 분리의 목적

각 메서드가 담당하는 기능을 구분하여 코드의 가독성과 유지보수성을 높였습니다.

- **입력 검증:** `run()`과 `play_quiz()`에서 사용자 입력의 유효성을 확인하고 잘못된 입력에 대응합니다.
- **게임 진행:** `play_quiz()`에서 퀴즈 출제, 정답 확인 및 점수 계산을 처리합니다.
- **데이터 입출력:** `save_data()`와 `load_data()`에서 JSON 파일을 통한 퀴즈 데이터와 최고 점수의 저장 및 불러오기를 담당합니다.
- **퀴즈 관리:** `add_quiz()`에서 새로운 퀴즈를 추가하고, 등록된 퀴즈 목록을 조회하는 기능을 관리합니다.

이처럼 기능별로 메서드의 책임을 구분하면 특정 기능을 수정할 때 관련된 메서드를 중심으로 작업할 수 있습니다. 이를 통해 기존 기능에 미치는 영향을 줄이고 향후 기능을 추가하거나 변경하기 쉽게 구성했습니다.







## 7. 테스트 실행

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


<img width="901" height="713" alt="03_main_menu" src="https://github.com/user-attachments/assets/3f8648b3-2f34-4b6c-ba3d-8878aa0d4a28" />
<img width="1085" height="1045" alt="04_main_menu" src="https://github.com/user-attachments/assets/7fdcde04-f15e-45a0-9ca2-63c30cb9280e" /> 
```

## 7-1. 대량 데이터 처리 및 성능 최적화

### 7-1-1. 대량 데이터 처리 시 고려사항

현재 프로젝트는 JSON 파일을 이용하여 퀴즈 데이터를 저장하고 불러온다.

퀴즈 데이터가 1,000개 이상으로 증가하면 다음과 같은 성능 문제가 발생할 수 있다.

- **메모리 사용량:** 모든 퀴즈 데이터를 한 번에 메모리에 불러오면 데이터가 증가할수록 메모리 사용량도 증가한다.
- **응답 시간:** 많은 퀴즈 데이터를 불러오거나 저장할 때 파일 입출력 시간이 길어질 수 있다.
- **검색 속도:** 리스트를 처음부터 순차적으로 검색하면 데이터가 증가할수록 검색 시간이 늘어난다.

### 7-1-2. 메모리 관리 방안

- 필요한 퀴즈 데이터만 불러와 사용하는 방식을 고려한다.
- 퀴즈 목록을 페이지 단위로 나누어 표시하여 불필요한 데이터 처리를 줄인다.
- 사용하지 않는 임시 객체와 데이터를 불필요하게 유지하지 않도록 관리한다.
- 데이터가 매우 커지는 경우 SQLite와 같은 데이터베이스 사용을 고려한다.

### 7-1-3. 응답 시간 및 검색 속도 개선 방안

- 퀴즈 검색 시 현재의 순차 검색 방식(O(n)) 대신 ID를 키로 사용하는 딕셔너리 구조(O(1) 평균 검색 시간)를 활용할 수 있다.
- 자주 사용하는 데이터는 메모리에 캐싱하여 반복적인 파일 읽기를 줄인다.
- 퀴즈 데이터를 추가하거나 수정할 때 불필요한 전체 파일 입출력을 최소화한다.
- 대량의 데이터는 SQLite 데이터베이스와 인덱스를 활용하여 검색 성능을 개선할 수 있다.

### 7-1-4. 대량 데이터 처리 성능 검증 계획

1,000개 이상의 퀴즈 데이터를 생성하여 다음 항목을 측정할 수 있다.

| 측정 항목 | 검증 방법 |
|---|---|
| 메모리 사용량 | 데이터 로딩 전후의 메모리 사용량 비교 |
| 데이터 로딩 시간 | 1,000개 이상 데이터 불러오기 시간 측정 |
| 검색 응답 시간 | 특정 퀴즈 검색에 걸리는 시간 측정 |
| 저장 시간 | 대량 데이터 저장에 걸리는 시간 측정 |

데이터 개수를 1,000개, 5,000개, 10,000개로 증가시키면서 성능 변화를 비교한다.

### 7-1-5. 향후 개선 방향

현재 프로젝트는 JSON 파일 기반의 간단한 데이터 관리 방식을 사용한다.

향후 데이터가 증가하면 다음과 같은 단계적 개선을 적용할 수 있다.

- 소규모 데이터: 현재 JSON 파일 방식 유지
- 중간 규모 데이터: 딕셔너리 검색 및 캐싱 적용
- 대규모 데이터: SQLite 데이터베이스와 인덱스 적용
- 매우 큰 데이터: 필요한 데이터만 조회하는 페이지 단위 처리 적용

이를 통해 데이터 규모가 증가하더라도 메모리 사용량과 응답 시간을 효율적으로 관리할 수 있도록 확장할 계획이다.



## 7-2. 데이터 백업 및 복구 (Backup & Rollback)

### 7-2-1. 백업의 필요성

현재 프로그램은 `state.json` 파일을 이용하여 퀴즈 데이터와 최고 점수 등을 저장한다.

데이터 저장 중 오류가 발생하거나 JSON 파일이 손상되면 기존 데이터가 유실될 수 있으므로, 저장 전 백업을 생성하는 방식을 설계한다.

### 7-2-2. 백업 생성 방식

`state.json` 파일을 새 데이터로 덮어쓰기 전에 기존 파일을 백업한다.

- 원본 파일: `state.json`
- 백업 파일: `state.json.bak`
- 기존 데이터가 존재하면 저장 전에 백업 파일을 생성한다.
- 백업 파일은 기존 정상 데이터를 보존하는 복구용 스냅샷으로 사용한다.
- 새 데이터 저장이 정상적으로 완료되었는지 확인한다.

### 7-2-3. 데이터 복구 및 롤백 절차

데이터 손상이나 저장 오류가 발생하면 다음 절차에 따라 복구한다.

1. 프로그램 실행 시 `state.json`의 JSON 형식과 데이터 구조를 검사한다.
2. 원본 데이터가 손상된 경우 `state.json.bak` 파일이 존재하는지 확인한다.
3. 백업 파일의 JSON 형식과 데이터 구조가 정상인지 검사한다.
4. 백업 파일이 정상이라면 해당 데이터를 원본 `state.json`으로 복원한다.
5. 복원된 데이터가 정상적으로 로딩되는지 확인한다.
6. 백업 파일도 손상되었거나 존재하지 않는 경우 기본 퀴즈 데이터를 이용하여 복구한다.


## 7-3. 프로그램 종료 및 예외 처리 (Signal Handling)

프로그램 실행 중 사용자의 입력이 중단되는 상황에 대비하여 종료 예외 처리를 구현했습니다.

### 7-3-1. KeyboardInterrupt 처리
- 사용자가 `Ctrl + C`를 눌러 프로그램 실행을 중단하면 `KeyboardInterrupt` 예외가 발생합니다.
- 예외를 감지하면 종료 안내 메시지를 출력하고 현재 데이터를 `state.json` 파일에 저장한 후 프로그램을 종료합니다.

### 7-3-2. EOFError 처리
- 입력 스트림이 종료되어 더 이상 사용자 입력을 받을 수 없는 경우 `EOFError` 예외가 발생합니다.
- 해당 예외도 안전하게 처리하여 종료 전에 데이터를 저장하도록 구성했습니다.

### 7-3-3. 데이터 동기화 및 저장
- 퀴즈 추가, 게임 점수 갱신 등 데이터가 변경되면 `save_data()`를 호출하여 JSON 파일에 반영합니다.
- 프로그램을 정상 종료하거나 입력이 중단되는 경우에도 `save_data()`를 호출합니다.
- 저장된 데이터는 다음 프로그램 실행 시 `load_data()`를 통해 불러옵니다.

이를 통해 비정상적인 입력 중단 상황에서도 변경된 퀴즈와 최고 점수가 가능한 한 보존되도록 했습니다.

※ 저장 과정에서 파일 접근 오류가 발생하면 예외 처리 메시지를 출력합니다.


<img width="790" height="584" alt="EOFError" src="https://github.com/user-attachments/assets/29794d7f-917c-48c8-9829-c000f1d968ed" />
<img width="974" height="963" alt="JSON" src="https://github.com/user-attachments/assets/ba954368-c233-42ec-b471-6c8ba8469469" />



### 7-3-4. 백업 및 복구 시 주의사항

- 백업 파일을 원본 파일과 같은 디렉터리에 보관하여 복구가 쉽도록 한다.
- 백업 파일을 새로운 데이터로 덮어쓰기 전에 기존 백업 상태를 고려한다.
- 복구 전에 백업 파일의 유효성을 먼저 검사한다.
- 복구가 완료되기 전까지 기존 백업 파일을 삭제하지 않는다.
- 중요한 데이터의 유실을 방지하기 위해 주기적인 백업 및 별도 저장소 보관을 고려한다.

### 7-3-5. 향후 개선 방향

현재 구현된 기본 퀴즈 복구 기능에 백업 및 롤백 기능을 추가하는 방향으로 개선할 계획이다.

향후에는 다음 기능을 적용할 수 있다.

- 저장 전 자동 백업 생성
- 백업 파일의 유효성 검사
- 손상된 데이터의 백업 파일 기반 복원
- 여러 시점의 백업을 보관하는 스냅샷 관리
- 복구 성공 및 실패 로그 기록

이를 통해 데이터 손상이나 저장 오류가 발생하더라도 기존 데이터를 최대한 보존하고 안정적으로 복구할 수 있도록 한다.



## 8. Git 실습 기록

- git clone을 사용하여 원격 저장소를 복제했습니다.
- git pull을 사용하여 원격 저장소의 변경 사항을 가져오는 실습을 진행합니다.

### 8-1. Git Commit 규칙

### 8-1-1. 커밋 단위 규정 (Commit Guidelines)

작업 내용을 논리적으로 구분하여 작은 단위로 커밋한다.

- 하나의 커밋에는 하나의 주요 작업만 포함한다.
- 서로 관련 없는 변경 사항은 별도의 커밋으로 분리한다.
- 기능 추가, 버그 수정, 문서 수정, 테스트 추가 등을 구분한다.
- 프로그램이 정상적으로 동작하고 변경 사항을 확인한 후 커밋한다.
- 불필요한 임시 파일이나 개인정보는 커밋하지 않는다.

### 8-1-2. 커밋 메시지 작성 규칙 (Commit Message Convention)

커밋 메시지는 다음 형식을 사용한다.

**작성 형식**

`<type>: <작업 내용>`

**Type 종류**

| Type | 설명 |
|---|---|
| feat | 새로운 기능 추가 |
| fix | 오류 및 버그 수정 |
| docs | 문서 수정 및 추가 |
| test | 테스트 코드 추가 및 수정 |
| refactor | 코드 구조 개선 |
| style | 코드 형식 및 스타일 수정 |
| chore | 설정 및 기타 작업 |


### 8-1-3. 커밋 메시지 작성 예시

```bash
git commit -m "feat: Add quiz creation feature"
git commit -m "fix: Fix score calculation error"
git commit -m "docs: Update README.md"
git commit -m "test: Add unit tests for quiz functionality"
git commit -m "refactor: Improve quiz data handling"'''
```

## 8-2. GitHub 저장소 및 커밋 기록 

```### 커밋 기록
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
```

### 8-3. 브랜치 생성 및 병합 실습

- `feature/readme-improvements` 브랜치를 생성했습니다.
- 해당 브랜치에서 README 개선 작업을 진행했습니다.
- 작업 완료 후 `main` 브랜치에 Fast-forward 방식으로 병합했습니다.
- `git log --oneline --graph --decorate --all` 명령어로 브랜치 및 커밋 이력을 확인했습니다.
- 관련 실행 화면은 `screenshots/07_git_branch_merge_history.png`에 첨부했습니다.

### 8-4. Git clone 및 pull 실습 증빙

- `git clone` 명령어를 사용하여 GitHub 원격 저장소를 새로운 로컬 폴더에 복제했습니다.
- 복제 결과 저장소 데이터 수신 및 변경 사항 처리가 정상적으로 완료되었습니다.
- 복제한 저장소 폴더에서 `git pull origin main` 명령어를 실행했습니다.
- `Already up to date.` 메시지를 확인하여 원격 저장소의 최신 변경 사항이 이미 반영되어 있음을 확인했습니다.

**실행 증빙 스크린샷**
- `screenshots/08_git_clone.png`: 원격 저장소 복제 실행 결과
- `screenshots/09_git_pull.png`: 원격 저장소 변경 사항 가져오기 실행 결과

<img width="2386" height="1393" alt="clone,pull 실습" src="https://github.com/user-attachments/assets/3151696e-87e4-4017-bf65-fa31b37fade5" />
<img width="1804" height="1818" alt="clone,pull 실습 2" src="https://github.com/user-attachments/assets/f74f39d0-0faa-4990-b623-61e52732dd64" />

## 8-5. README 파일 확인 및 인코딩 문제 해결

Git으로 복제한 프로젝트 폴더에서 README.md 파일의 내용을 확인하기 위해 PowerShell의 Get-Content 명령어를 사용했습니다.

Get-Content .\README.md

처음에는 기본 인코딩 설정으로 파일을 읽어 한글이 깨져 출력되는 현상이 발생했습니다. 이는 파일의 실제 인코딩과 PowerShell이 파일을 읽는 방식이 일치하지 않아 발생한 문제입니다.

이를 해결하기 위해 파일의 인코딩을 UTF-8로 명시하여 다시 확인했습니다.

Get-Content .\README.md -Encoding UTF8

그 결과 README 파일의 한글 내용이 정상적으로 출력되는 것을 확인했습니다.

확인 사항

Git으로 복제한 프로젝트 폴더에서 README 파일에 접근할 수 있는지 확인

PowerShell의 Get-Content 명령어를 이용한 파일 내용 출력

UTF-8 인코딩 지정에 따른 한글 출력 문제 해결

**실행 증빙 스크린샷**

<img width="1657" height="1747" alt="인코딩 문제 해결" src="https://github.com/user-attachments/assets/2ccbb3c2-60d6-48ea-b372-f7d7d5df9cdf" />
<img width="1429" height="1756" alt="인코딩 문제 해결 2" src="https://github.com/user-attachments/assets/9889a2f9-bef5-4445-9d35-d8eea6448382" />



## 8-6. Git 커밋 이력 및 개발 진행 과정

본 프로젝트는 Git을 활용하여 개발 과정을 단계별로 기록했습니다.

- 전체 커밋 수: **31개**
- 사용 브랜치: `main`, `feature/readme-improvements`
- 주요 작업: 프로젝트 초기 설정, Quiz 클래스 구현, 게임 기능 개발, JSON 데이터 관리, 단위 테스트 작성, 테스트 개선, 문서화 및 Git 실습

  <img width="1725" height="1620" alt="커밋 갯수 10개 7" src="https://github.com/user-attachments/assets/9c28cebd-b181-4189-ae2b-5297acdc79ec" />

### 8-6-1. 주요 개발 커밋

```
| 커밋 해시 | 커밋 메시지 | 작업 내용 |
|---|---|---|
| `1d9949f` | Update project files | 프로젝트 기본 파일 및 .gitignore 구성 |
| `5230adb` | Add Quiz class | Quiz 클래스 구현 |
| `b225fd4` | Update project files | 메인 프로그램 및 퀴즈 게임 기능 구현 |
| `65346d0` | Document automated tests | 자동화 테스트 문서 작성 |
| `b006649` | Add unit tests for quiz functionality | 퀴즈 기능 단위 테스트 추가 |
| `15d5cb9` | Add quiz display test | 퀴즈 출력 테스트 추가 |
| `3b24403` | Add type hints to Quiz class | Quiz 클래스 타입 힌트 추가 |
| `c44b9b3` | Improve quiz display test assertions | 테스트 검증 개선 |
| `f7debe9` | Document git clone and pull practice | Git clone 및 pull 실습 문서 작성 |
| `44bffe5` | Update README.md | 프로젝트 README 문서 수정 |
```



### 8-7. 전체 Git 커밋 로그

```
﻿* 049d116 (HEAD -> main, origin/main) Update project files
* 44bffe5 Update README.md
* cbc1a34 Update project files
* a647e35 Update project files
* cef35fd Add new screenshots
* 74731f8 Update project files
* 9c59711 Update project files
* ead0388 Update project files
* d8abb12 Update project files
* 06b2130 Update project files
* 24eb4d2 Update project files
* 17d8c62 Update project files
* 12cd68d Update project files
* 2bb4a06 Add new screenshots
* e8bb788 Update project files
* 927dc64 Add new screenshots
* 41964b6 Update project files
* ff65e74 Add new screenshots
* 8792999 Add new screenshots
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
```

<img width="1045" height="787" alt="커밋 갯수 10개 4" src="https://github.com/user-attachments/assets/fd2506e5-a426-40da-89cc-b2382fdaecb3" />

- [git_commit_history.txt](git_commit_history.txt)

전체 로그 확인 명령어:

`git log --oneline --graph --decorate --all`

### 8-8. 커밋 이력 확인 방법

GitHub 저장소의 커밋 기록과 `git_commit_history.txt`를 통해 전체 커밋 개수와 개발 진행 과정을 확인할 수 있습니다.



## 9. 유지 보수 및 향후 개선 계획
## 9-1. 요구사항 변경 시 수정 대상 및 영향 범위 (Change Impact Analysis)

프로그램의 새로운 요구사항이 발생하면 관련 파일과 메서드를 확인하여 필요한 부분만 수정한다. 이를 통해 기존 기능에 미치는 영향을 최소화하고 유지보수성을 높인다.

### 9-1-1. 기능별 수정 대상


| 변경 요구사항 | 수정 대상 | 영향 범위 |
|---|---|---|
| 퀴즈 점수 계산 방식 변경 | `quiz_game.py`의 점수 계산 로직 | 퀴즈 결과 및 최고 점수 |
| 퀴즈 데이터 구조 변경 | `quiz.py`의 `Quiz` 클래스 | 퀴즈 생성, 데이터 로딩 및 저장 |
| 퀴즈 저장 방식 변경 | `quiz_game.py`의 `save_data()` | 데이터 저장 및 파일 관리 |
| 퀴즈 불러오기 방식 변경 | `quiz_game.py`의 데이터 로딩 메서드 | 프로그램 초기화 및 데이터 복구 |
| 퀴즈 진행 방식 변경 | `quiz_game.py`의 퀴즈 진행 관련 메서드 | 사용자 입력 및 퀴즈 결과 |
| 새로운 퀴즈 기능 추가 | `quiz_game.py` 및 필요한 경우 `quiz.py` | 메뉴, 퀴즈 데이터 및 관련 기능 |


### 9-1-2. 주요 변경 사항별 영향 분석

**① 점수 계산 방식 변경**

- 수정 대상: `quiz_game.py`의 점수 계산 로직
- 영향 범위: 퀴즈 정답 판정, 최종 점수, 최고 점수 기록
- 주의사항: 점수 계산 방식을 변경한 후 기존 최고 점수 저장 기능이 정상적으로 작동하는지 확인한다.

**② 퀴즈 데이터 구조 변경**

- 수정 대상: `quiz.py`의 `Quiz` 클래스
- 영향 범위: 퀴즈 객체 생성, JSON 데이터 변환, 데이터 저장 및 불러오기
- 주의사항: 데이터 구조를 변경하면 기존에 저장된 JSON 데이터와의 호환성을 확인해야 한다.

**③ 데이터 저장 방식 변경**

- 수정 대상: `quiz_game.py`의 `save_data()` 메서드 및 관련 데이터 로딩 메서드
- 영향 범위: 퀴즈 데이터, 최고 점수, 데이터 백업 및 복구
- 주의사항: 저장 형식이 변경되면 기존 데이터의 손실이나 호환성 문제가 발생하지 않도록 검증한다.

### 9-1-3. 변경 작업 시 검증 절차

요구사항 변경 후 다음 항목을 확인한다.

1. 변경 대상 파일과 메서드를 확인한다.
2. 수정으로 인해 영향을 받는 다른 기능을 파악한다.
3. 기존 기능이 정상적으로 작동하는지 테스트한다.
4. 데이터 저장 및 불러오기 기능을 검증한다.
5. 점수 계산과 최고 점수 기록을 확인한다.
6. 문제가 없으면 변경 사항을 Git에 커밋한다.

### 9-1-4. 유지보수 및 확장성

기능별로 역할을 분리하여 요구사항 변경 시 관련된 부분만 수정하도록 설계한다.

이를 통해 코드 중복을 줄이고 기존 기능에 대한 영향을 최소화하며, 새로운 기능을 추가할 때도 유지보수가 쉽도록 한다.


## 10. 결론 및 핵심 원리 요약

### 10-1. 프로젝트 수행 결과

Python을 활용하여 콘솔 기반 퀴즈 게임을 구현하고, 퀴즈 진행과 관리, 점수 계산, JSON 파일을 이용한 데이터 저장 및 불러오기 기능을 완성했습니다.

또한 클래스를 활용하여 역할과 책임을 분리하고, 예외 처리와 단위 테스트를 통해 프로그램의 안정성과 기능을 확인했습니다. Git과 GitHub를 이용하여 코드 변경 이력을 관리하고 프로젝트 진행 과정을 기록했습니다.

### 10-2. 퀴즈 프로그램의 작동 원리

퀴즈 게임은 `Quiz`와 `QuizGame` 클래스가 서로 협력하여 작동합니다.

**퀴즈 진행 과정**

1. `Quiz` 객체를 생성하여 문제, 선택지, 정답을 저장합니다.
2. `display()` 메서드로 문제와 선택지를 출력합니다.
3. 사용자에게 답안을 입력받습니다.
4. `check_answer()` 메서드에서 사용자 답안과 정답을 비교합니다.
5. 정답 여부에 따라 점수를 계산하고 최고 점수를 갱신합니다.

**핵심 원리**
- 객체 생성: 하나의 문제를 하나의 `Quiz` 객체로 표현합니다.
- 반복 처리: 여러 Quiz 객체를 순서대로 처리하여 문제를 출제합니다.
- 조건 비교: 사용자 답안과 저장된 정답이 일치하는지 확인합니다.
- 점수 관리: 정답 결과를 바탕으로 현재 점수와 최고 점수를 관리합니다.

### 10-3. JSON 데이터 저장 및 불러오기 원리

JSON(JavaScript Object Notation)은 데이터를 키(Key)와 값(Value)의 형태로 표현하는 데이터 형식입니다. Python에서는 `json` 모듈을 이용하여 JSON 데이터를 처리할 수 있습니다.

**데이터 저장 과정**

1. Python 객체에 저장된 퀴즈와 최고 점수를 준비합니다.
2. 퀴즈 데이터를 딕셔너리와 리스트 형태로 구성합니다.
3. `json.dump()`를 사용하여 Python 데이터를 JSON 형식으로 변환하고 `state.json` 파일에 저장합니다.

**데이터 불러오기 과정**

1. `json.load()`를 사용하여 JSON 파일의 내용을 읽습니다.
2. 읽어온 데이터를 Python의 딕셔너리와 리스트 형태로 변환합니다.
3. 퀴즈 정보를 바탕으로 `Quiz` 객체를 다시 생성합니다.
4. 저장된 최고 점수와 퀴즈 정보를 게임에 반영합니다.

**핵심 개념**

| 구분 | 역할 |
|---|---|
| JSON | 데이터를 저장하고 전달하기 위한 형식 |
| `json.dump()` | Python 데이터를 JSON 파일에 저장 |
| `json.load()` | JSON 파일을 읽어 Python 데이터로 변환 |
| `state.json` | 퀴즈 정보와 최고 점수를 보관하는 파일 |
| 직렬화(Serialization) | 객체나 데이터를 저장 가능한 형식으로 변환하는 과정 |
| 역직렬화(Deserialization) | 저장된 데이터를 다시 프로그램에서 사용할 수 있는 형태로 변환하는 과정 |

### 10-4. 프로젝트를 통해 이해한 핵심 원리

| 핵심 원리 | 이해한 내용 |
|---|---|
| 객체지향 프로그래밍(OOP) | 클래스와 객체를 활용하여 데이터와 기능을 역할에 맞게 구성 |
| 책임 분리 | 메서드마다 담당 기능을 구분하여 코드의 가독성과 유지보수성 향상 |
| 반복문과 조건문 | 여러 문제를 반복 출제하고 정답 여부에 따라 결과 처리 |
| 데이터 입출력(I/O) | JSON 파일을 활용하여 프로그램 종료 후에도 데이터 보존 |
| 예외 처리 | 잘못된 입력과 파일 관련 오류에 대응하여 프로그램의 비정상 종료 방지 |
| 단위 테스트 | 개별 기능이 예상한 결과를 반환하는지 테스트 코드로 검증 |
| 버전 관리(Git) | 커밋과 브랜치를 활용하여 코드 변경 이력을 기록하고 관리 |

### 10-5. 최종 정리

이번 프로젝트를 통해 단순히 Python 문법을 사용하는 것을 넘어, 프로그램의 구조를 설계하고 기능을 구현하며 데이터를 저장하고 관리하는 과정을 경험했습니다.

특히 객체지향 프로그래밍을 통한 역할 분리, 반복문과 조건문을 활용한 퀴즈 진행, JSON을 이용한 데이터 영속성 확보 등 실제 프로그램을 구성하는 핵심 원리를 이해할 수 있었습니다.

앞으로는 기존 코드의 구조를 개선하고 새로운 기능을 추가하면서 코드의 재사용성, 안정성 및 유지보수성을 지속적으로 높이고자 합니다.





