from QuizEngine4Trivia import QuizEngine
import html

quiz = QuizEngine()

while quiz.still_has_questions():
    print(f"Your score : {quiz.score}\n\n")
    current = quiz.next_question()
    print({html.unescape(current.question)})

    count = 0
    for possible_answer in current.possible_answers:
        print(f"{count}: {html.unescape(possible_answer)}")
        count += 1

    user_answer = int(input("Answer .:"))
    if 0 <= user_answer <= count:
        if quiz.check_answer(current.possible_answers[user_answer]):
            print("You are right")
        else:
            print("You are wrong")

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
