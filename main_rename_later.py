from timer import Timer
timer = Timer()
timer.CountDown()

from load_collected_data import QuizCreator
quiz_creator = QuizCreator()
quiz_load_questions = quiz_creator.LoadQuestion()

from print_and_scores import QuizLoad
quiz_data = QuizCreator().LoadQuestion()

quiz_loader = QuizLoad(quiz_data)
quiz_print = quiz_loader.PrintQuiz()
quiz_score = quiz_loader.Score()