from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_bank.append(Question(ques['question'], ques['correct_answer']))

quiz_bran = QuizBrain(question_bank)

while quiz_bran.still_has_question() :
    quiz_bran.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_bran.score}/{len(quiz_bran.question_list)}")
    
