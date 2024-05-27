from QuizEngine4Trivia import QuizEngine
import html

quiz = QuizEngine()

while quiz.still_has_questions():

    current = quiz.next_question()

    user_answer: int = -1
    count = 0
    while not 0 <= user_answer <= count:
        count = 0
        print(f"Your score : {quiz.score}\n\n")
        print(f"{html.unescape(current.category)}")
        print(f"{html.unescape(current.question)}\n")

        for possible_answer in current.possible_answers:
            print(f"{count}: {html.unescape(possible_answer)}")
            count += 1
        count -= 1 # roll back last increment
        user_answer = int(input("Answer .:"))

    if quiz.check_answer(current.possible_answers[user_answer]):
        print("You are right")
    else:
        print("You are wrong")

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# show the right correct answer for those we didn't know the answers on
for result in quiz.get_result():
    if not result[0]:
        print(html.unescape(result[1]))
        print(html.unescape(result[2]))

