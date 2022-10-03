from Day_17_question_model import Question
from Day_17_data import question_data
from Day_17_quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    the_question = question["question"]
    the_answer = question["correct_answer"]
    new_question = Question(the_question,the_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    if not quiz.still_has_questions():
        print("You've completed the quiz")
        print(f"Your final score was: {quiz.score}/{quiz.question_number}")
