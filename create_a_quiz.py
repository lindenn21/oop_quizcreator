class CollectedData:
    def __init__(self, file_name='collected_data.txt'):
        self.file_name = file_name
        self.questions = []
        self.file = open(self.file_name, 'w')

    def AddQuestion(self):
        question = input(f'Enter a question')
        choice_a = input("Choice A: ")
        choice_b = input("Choice B: ")
        choice_c = input("Choice C: ")
        choice_d = input("Choice D: ")
        answer = input("What is the correct answer? (A, B, C OR D): ").upper()

        self.questions.append({f"question: ": question,
                               "choices: ": {"A": choice_a,
                                             "B": choice_b,
                                             "C": choice_c,
                                             "D": choice_d},
                               "correct answer: ": answer})

        self.file.write(f"Questions: {question}\n")
        self.file.write(f"A: {choice_a}\n")
        self.file.write(f"B: {choice_b}\n")
        self.file.write(f"C: {choice_c}\n")
        self.file.write(f"D: {choice_d}\n")
        self.file.write(f"{answer}\n")

    def start(self):
        print("Enter as many questions with multiple choices as you want: ")







