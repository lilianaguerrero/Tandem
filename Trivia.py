from Question import Question
import json, random

Q_LIST = []
def format_questions():
    with open("Apprentice_TandemFor400_Data.json") as json_file:
        raw_questions = json.load(json_file)
        for item in raw_questions:
            responses = [item["correct"]]
            for response in item["incorrect"]:
                responses.append(response)
            rand_options = responses[:]
            random.shuffle(rand_options)
            quest_prompt = item['question']
            for resp in rand_options:
                quest_prompt += " " + resp + "  "
            Q_LIST.append(Question(quest_prompt[0:],item['correct']))

def run_test(Q_LIST):
    score = 0 
    sampling = random.sample(Q_LIST, k=10)
    print("Good luck in this game of Trivia- Type in the correct answer from the options & hit enter!")
    for question in sampling:
        response = input(question.prompt)
        if response == question.answer:
            print("You got the right answer: " + question.answer)
            score += 1
        else:
            print("Wrong answer try again next time, the correct answer: " + question.answer)
    print("You got " + str(score) + "/10 correct!")

format_questions()
run_test(Q_LIST)



        


 