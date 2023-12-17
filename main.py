from data import *
import time
import random

# score
score = 0

# Main character Intro
print("Hello, my name is John")
time.sleep(1)
print("Whats your name?")
time.sleep(0.5)
name = input("")
time.sleep(1)
print("Hello, " + name + "!")
time.sleep(0.9)
print("I'm stuck in a castle and tied by and ogore.")
time.sleep(1)
print("I really need to get out!")
time.sleep(0.5)
print("The ogore said that if you play a trivia game, you can get me out!")
time.sleep(0.5)
print("Get more than 7 of the 10 questions right to free me!, lets start!")
time.sleep(2)
# debug program
#for i in range(0, 29):
    #print(questions[i])
    #print(answers[i])

#delete the question
def deleteQuestionandAnswer(questions, answers, k):
    questions.remove(questions[k])
    answers.remove(answers[k])

# Question Loop
for i in range(0, 10):
    k = random.randint(0, len(questions)-1)
    question = questions[k]
    answer = answers[k]
    time.sleep(2)
    print(question)
    answeruser = input("ANSWER: ")
    if answeruser == answer:
        print("CORRECT")
        deleteQuestionandAnswer(questions, answers, k)
        score += 1
        print("Score:")
        print(score)
    else:
        print("Incorrect!")
        print("The correct answer was " + answer)
        deleteQuestionandAnswer(questions, answers, k)
        print("Score:")
        print(score)
time.sleep(2)
# Win or Lose
if score > 7:
    print("GREAT JOB YOU WIN!!!!!!!!") 
    time.sleep(1)
    print("NOW IM FREEEE!")
    time.sleep(1)
    print("Score:")
    print(score)
else:
    print("IM STILL STUCK HERE! :(")
    time.sleep(1)
    print("Score:")
    print(score)


