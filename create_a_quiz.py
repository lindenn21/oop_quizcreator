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





