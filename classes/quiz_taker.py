import os
import random

class QuizTaker:
    def __init__(self, folder, manager):
        self.quizzes_folder = folder
        self.manager = manager

    def take_quiz(self):
        quizzes = [file for file in os.listdir(self.quizzes_folder) if file.endswith(".txt")]
        if not quizzes:
            print("No quizzes found. Please create one first.")
            return self.manager.main_menu()

        print("Select A Quiz:")
        for index, quiz in enumerate(quizzes, start=1):
            print(f"{index}. {quiz.replace('.txt', '').replace('_', ' ').title()}")

        try:
            choice = int(input("Select a quiz number to take: "))
            if 1 <= choice <= len(quizzes):
                quiz_path = os.path.join(self.quizzes_folder, quizzes[choice - 1])
                self.run_quiz(quiz_path)
            else:
                print("Invalid number.")
                self.take_quiz()
        except ValueError:
            print("Please enter a valid number.")
            self.take_quiz()

    def run_quiz(self):
        pass