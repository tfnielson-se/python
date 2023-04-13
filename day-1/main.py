import pdb

tasks = []
question_answer = ''


def ask_question():
    global question_answer
    qst = input("Do you have more tasks? (y/n)")
    question_answer = qst
    return question_answer


while question_answer != 'n':
    user_prompt = "Enter To-Do task: "
    user_input = input(user_prompt)
    tasks.append(user_input)
    ask_question()
else:
    print(tasks)
