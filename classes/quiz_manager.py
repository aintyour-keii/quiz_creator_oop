import os
from classes.quiz_creator import QuizCreator
from classes.quiz_taker import QuizTaker

class QuizManager:
    def __init__(self):
        self.quizzes_folder = "quizzes"
        os.makedirs(self.quizzes_folder, exist_ok=True)
        self.creator = QuizCreator(self.quizzes_folder)
        self.taker = QuizTaker()

    def main_menu(self):
        print("\nQuiz Program")
        print("1. Create a Quiz")
        print("2. Take Quiz")
        print("3. Exit")

        user_input = input("Enter an option: ").strip()
        if user_input == "1":
            # call a method in quiz creator class
            pass
        elif user_input == "2":
            # call a method in quiz taker class
            pass
        elif user_input == "3":
            # quit program
            pass
        else:
            # invalid input, call main menu function
            pass