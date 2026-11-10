import json
from pathlib import Path

from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.state_file = Path(__file__).resolve().parent / "state.json"
        self.quizzes = []
        self.best_score = 0

        self.load_data()

    def create_default_quizzes(self):
        return [
            Quiz(
                "Python 파일의 기본 확장자는?",
                [".html", ".py", ".css", ".js"],
                2
            ),
            Quiz(
                "HTML의 주된 역할은?",
                ["웹 페이지 구조 작성", "데이터베이스 관리", "운영체제 실행", "네트워크 연결"],
                1
            ),
            Quiz(
                "Git의 주된 목적은?",
                ["이미지 편집", "버전 관리", "영상 재생", "파일 압축"],
                2
            ),
            Quiz(
                "다음 중 Python의 자료형이 아닌 것은?",
                ["int", "str", "list", "html"],
                4
            ),
            Quiz(
                "컴퓨터에서 CPU의 주요 역할은?",
                ["데이터 저장", "화면 출력", "명령어 처리", "전원 공급"],
                3
            )
        ]

    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            with self.state_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터가 저장되었습니다.")

        except OSError as error:
            print(f"데이터 저장 중 오류가 발생했습니다: {error}")

    def load_data(self):
        if not self.state_file.exists():
            print("저장된 데이터가 없습니다. 기본 퀴즈를 불러옵니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = 0
            self.save_data()
            return

        try:
            with self.state_file.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("잘못된 데이터 형식입니다.")

            self.quizzes = [
                Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"]
                )
                for item in data.get("quizzes", [])
            ]

            self.best_score = int(data.get("best_score", 0))

            if not self.quizzes:
                self.quizzes = self.create_default_quizzes()

            print("저장된 데이터를 불러왔습니다.")

        except (
            json.JSONDecodeError,
            OSError,
            KeyError,
            TypeError,
            ValueError,
            UnicodeDecodeError
        ) as error:
            print(f"데이터를 불러오는 중 오류가 발생했습니다: {error}")
            print("기본 퀴즈로 복구합니다.")

            self.quizzes = self.create_default_quizzes()
            self.best_score = 0
            self.save_data()

    def list_quizzes(self):
        print("\n===== 퀴즈 목록 =====")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")
        print(f"현재 최고 점수: {self.best_score}점")

    def play_quiz(self):
        print("\n===== 퀴즈 시작 =====")

        score = 0

        for quiz in self.quizzes:
            quiz.display()

            while True:
                try:
                    user_answer = input("정답 번호를 입력하세요: ").strip()

                    if not user_answer:
                        print("답을 입력하세요.")
                        continue

                    user_answer = int(user_answer)

                    if 1 <= user_answer <= len(quiz.choices):
                        break

                    print(f"1부터 {len(quiz.choices)} 사이의 숫자를 입력하세요.")

                except ValueError:
                    print("숫자만 입력하세요.")

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n===== 퀴즈 결과 =====")
        print(f"총 점수: {score} / {len(self.quizzes)}")

        if score > self.best_score:
            self.best_score = score
            print("최고 점수가 갱신되었습니다!")

        self.save_data()

    def add_quiz(self):
        print("\n===== 새 퀴즈 추가 =====")

        question = input("질문을 입력하세요: ").strip()

        while not question:
            print("질문은 비워 둘 수 없습니다.")
            question = input("질문을 입력하세요: ").strip()

        choices = []

        for index in range(4):
            choice = input(f"{index + 1}번 선택지를 입력하세요: ").strip()

            while not choice:
                print("선택지는 비워 둘 수 없습니다.")
                choice = input(f"{index + 1}번 선택지를 입력하세요: ").strip()

            choices.append(choice)

        while True:
            try:
                answer = int(input("정답 번호를 입력하세요 (1~4): "))

                if 1 <= answer <= 4:
                    break

                print("1부터 4 사이의 숫자를 입력하세요.")

            except ValueError:
                print("숫자만 입력하세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("새 퀴즈가 추가되었습니다!")

    def run(self):
        while True:
            print("\n===== Python Quiz Game =====")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가하기")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 보기")
            print("5. 종료하기")

            try:
                choice = input("메뉴 번호를 선택하세요: ").strip()

                if not choice:
                    print("메뉴 번호를 입력하세요.")
                    continue

                if not choice.isdigit():
                    print("숫자만 입력하세요.")
                    continue

                choice = int(choice)

                if choice == 1:
                    self.play_quiz()

                elif choice == 2:
                    self.add_quiz()
                    self.save_data()

                elif choice == 3:
                    self.list_quizzes()

                elif choice == 4:
                    self.show_best_score()

                elif choice == 5:
                    self.save_data()
                    print("프로그램을 종료합니다.")
                    break

                else:
                    print("1부터 5 사이의 번호를 입력하세요.")

            except (KeyboardInterrupt, EOFError):
                print("\n입력이 중단되었습니다. 데이터를 저장하고 종료합니다.")
                self.save_data()
                break