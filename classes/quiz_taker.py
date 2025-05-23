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

    def run_quiz(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        print(f"\nStarting Quiz: {lines[0]}\n")
        questions = []
        line_index = 1

        while line_index < len(lines):
            if lines[line_index] and lines[line_index][0].isdigit() and lines[line_index][1] == ".":
                question_text = lines[line_index]
                line_index += 1
                choices = []
                for _ in range(4):
                    letter, choice_text = lines[line_index].split(". ", 1)
                    is_correct = choice_text.endswith("*")
                    if is_correct:
                        choice_text = choice_text[:-1]
                    choices.append({"text": choice_text, "is_correct": is_correct})
                    line_index += 1
                questions.append({
                    "question": question_text[question_text.find('.') + 1:].strip(),
                    "choices": choices
                })
            else:
                line_index += 1

        random.shuffle(questions)
        score = 0
        results = []

        for number, question in enumerate(questions, start=1):
            print(f"\n{number}. {question['question']}")
            choices = question['choices']
            random.shuffle(choices)

            letter_map = {}
            correct_letter = ""
            for i, choice in enumerate(choices):
                letter = chr(65 + i)
                letter_map[letter] = choice
                if choice["is_correct"]:
                    correct_letter = letter
                print(f"{letter}. {choice['text']}")

            user_input = input("Your answer (A/B/C/D): ").strip().upper()
            is_correct = user_input == correct_letter
            if is_correct:
                score += 1
            results.append({
                "question_num": number,
                "user_letter": user_input,
                "correct_letter": correct_letter,
                "user_choice": letter_map.get(user_input, {"text": "Invalid"})["text"],
                "correct_choice": letter_map[correct_letter]["text"],
                "is_correct": is_correct
            })

        print("\n=== QUIZ RESULTS ===")
        for result in results:
            if result["is_correct"]:
                print(f"{result['question_num']}. {result['user_letter']}. {result['user_choice']}")
            else:
                print(f"{result['question_num']}. {result['user_letter']}. {result['user_choice']} -> {result['correct_letter']}. {result['correct_choice']}")
        print(f"\nSCORE: {score}/{len(questions)}\n")
        self.manager.main_menu()