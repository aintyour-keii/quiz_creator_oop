import os
from classes.quiz_creator import QuizCreator
from classes.quiz_taker import QuizTaker

class QuizManager:
    def __init__(self):
        self.quizzes_folder = "quizzes"
        os.makedirs(self.quizzes_folder, exist_ok=True)

    def main_menu(self):
        pass