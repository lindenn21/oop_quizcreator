class CollectedData:
    def __init__(self, file_name='collected_data.txt'):
        self.file_name = file_name
        self.questions = []
        self.file = open(self.file_name, 'w')


