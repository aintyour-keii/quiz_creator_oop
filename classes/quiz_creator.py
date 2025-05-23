import os
import random

class QuizCreator:
    def __init__(self, folder):
        self.quizzes_folder = folder
    
    def create_quiz(self):
        quiz_title = input("Enter quiz title: ").strip()
        if quiz_title.lower() == "exit":
            return
        snake_case_title = quiz_title.replace(" ", "_").lower()
        questions = []

        while True:
            question_text = input("Enter question: ").strip()
            if not question_text.endswith("?"):
                question_text += " ?"
            correct_answer = input("Enter answer: ").strip()
            incorrect_options = [input("Enter incorrect answer: ").strip() for _ in range(3)]

            questions.append({
                "question": question_text,
                "answer": correct_answer,
                "other_options": incorrect_options
            })

            another = input("Would you like to enter another question? (y/n): ").strip().lower()
            if another != "y":
                break

        file_path = os.path.join(self.quizzes_folder, f"{snake_case_title}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"{quiz_title.title()}\n")
            for index, question in enumerate(questions, start=1):
                file.write(f"{index}. {question['question']}\n")
                choices = [question['answer']] + question['other_options']
                random.shuffle(choices)
                for i, choice in enumerate(choices):
                    letter = chr(65 + i)
                    if choice == question['answer']:
                        file.write(f"{letter}. {choice}*\n")
                    else:
                        file.write(f"{letter}. {choice}\n")
                file.write("\n")
        print(f"Quiz Successfully Created: {snake_case_title}.txt")