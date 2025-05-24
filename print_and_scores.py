class QuizLoad:
    def __init__(self, quiz_data):
       self.quiz_data = quiz_data

    def PrintQuiz(self):
        question_num = 1
        for item in self.quiz:
            print(f"\nQuestion {question_num}: {item['question'][9:].strip()}")
            choices = item["choices"]
            print(f"A. {choices['A']}")
            print(f"B. {choices['B']}")
            print(f"C. {choices['C']}")
            print(f"D. {choices['D']}")
            users_answer = input("What is your answer?: (A/B/C/D): ").strip().upper()

            if users_answer == item['correct_answer']:
                print("Goodjob, that is correct!")
                self.score += 1
            else:
                print(f"Sorry! The correct answer is {item['correct_answer']}")
            question_num += 1


