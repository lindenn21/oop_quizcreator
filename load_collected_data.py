import random
class QuizCreator:
    def __init__(self, file_name="collected_data1.txt"):
       self.file_name = file_name
       self.quiz = []

    def LoadQuestion(self):
        with open("collected_data1.txt", "r") as the_quiz:
            quiz_content = the_quiz.readlines()

        quiz = []
        num = 0
        while num < len(quiz_content):
            # Sets the line num and strip() cleans \n and unnecessary spaces
            line = quiz_content[num].strip()
            if line.startswith("Questions: "):
                question = line.strip()
                choice_a = quiz_content[num + 1].strip()
                choice_b = quiz_content[num + 2].strip()
                choice_c = quiz_content[num + 3].strip()
                choice_d = quiz_content[num + 4].strip()
                answer = quiz_content[num + 5].strip().upper()
                quiz.append({
                    f"question": question,
                    "choices": {"A":  choice_a, "B":  choice_b,
                                "C":  choice_c, "D":  choice_d},
                    "correct_answer": answer
                })

                num += 6
            else:
                num += 1
        random.shuffle(self.quiz)
        self.quiz = quiz
        return self.quiz






