from quiz_engine import QuizEngine

quiz = QuizEngine()

while quiz.still_has_questions():
    print(f"Your score : {quiz.score}")
    q_text = quiz.next_question()
    user_answer = input(f"Q.{quiz.question_number}: {q_text}")
    if quiz.check_answer(user_answer):
        print("You are right")
    else:
        print("You are wrong")
