"""  The Script for the game
"""
from data import question_data
NUM_QUESTIONS = 10


class Question:
    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer


questions_bank = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    questions_bank.append(question)


class QuizBrain:
    def __init__(self, questions_list) -> None:
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        user_input = 'None'
        while user_input.lower()[0] not in ['t', 'f']:
            user_input = input(f"Q{self.question_number}. {question.text} "
                               "True or False? ")
        if user_input == 't':
            user_choice = "True"
        else:
            user_choice = "False"
        if user_choice == question.answer:
            self.score += 1
            print(f"You are correct, your score is "
                  f"{quizbrain.score}/{self.question_number + 1}.")
        else:
            print(f"You are incorrect, your score is "
                  f"{quizbrain.score}/{self.question_number + 1}.")
        print(f"Q{self.question_number + 1}. {question.text} "
              f"{question.answer}. ")
        self.question_number += 1


if __name__ == "__main__":
    quizbrain = QuizBrain(questions_bank)
    print('f')
    while quizbrain.question_number < len(quizbrain.questions_list):
        quizbrain.next_question()

