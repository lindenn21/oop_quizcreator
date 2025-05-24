import random
class QuizCreator:
    def __init__(self, file_name="collected_data1.txt"):
       self.file_name = file_name

    def LoadQuiz(self):
        with open("collected_data1.txt", "r") as the_quiz:
            quiz_content = the_quiz.readlines()

        quiz = []
        num = 0
        while num < len(quiz_content):
            # Sets the line num and strip() cleans \n and unnecessary spaces
            line = quiz_content[num].strip()
            if line.startswith("Questions: "):
                question = line.strip()
                a = quiz_content[num + 1].strip()
                b = quiz_content[num + 2].strip()
                c = quiz_content[num + 3].strip()
                d = quiz_content[num + 4].strip()
                answer = quiz_content[num + 5].strip().upper()
                quiz.append({
                    f"question": question,
                    "choices": {"A": a, "B": b,
                                "C": c, "D": d},
                    "correct_answer": answer
                })

                num += 6
            else:
                num += 1
        random.shuffle(quiz)






