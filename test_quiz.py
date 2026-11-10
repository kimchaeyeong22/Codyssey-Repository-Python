import unittest
from unittest.mock import patch

from quiz import Quiz
from quiz_game import QuizGame


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz(
            "Python 파일의 기본 확장자는?",
            [".html", ".py", ".css", ".js"],
            2
        )

    def test_quiz_question(self):
        self.assertEqual(
            self.quiz.question,
            "Python 파일의 기본 확장자는?"
        )

    def test_quiz_choices(self):
        self.assertEqual(len(self.quiz.choices), 4)

    def test_correct_answer(self):
        self.assertTrue(self.quiz.check_answer(2))

    def test_wrong_answer(self):
        self.assertFalse(self.quiz.check_answer(1))

    def test_default_quizzes(self):
        game = QuizGame.__new__(QuizGame)
        quizzes = game.create_default_quizzes()

        self.assertGreaterEqual(len(quizzes), 5)

    def test_quiz_display(self):
        with patch("builtins.print") as mock_print:
            self.quiz.display()

        mock_print.assert_any_call(
            "\nPython 파일의 기본 확장자는?"
        )

        for index, choice in enumerate(self.quiz.choices, start=1):
            mock_print.assert_any_call(f"{index}. {choice}")

        self.assertEqual(mock_print.call_count, 5)


if __name__ == "__main__":
    unittest.main()