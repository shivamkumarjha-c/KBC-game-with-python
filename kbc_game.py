print("welcome to shivam\'s kon banega crorepatti" )
print("with each correct answer you keep adding money to your wallet!")
print("but one answer and you will be out and cant earn more!")
print("""the pricing is like\n round.1 2000\nround.2 4000\nround.3 8000\nround.4 10000\nround.5 20000\n round6.50000\n
round.7 1lakh\nround.8 5lakh\n round.9 10lakh\n round 10 1crore\n""")
print("from round 1-6 if you lose you can still keep money")
print("but if you wish to continue and lose you take nothing")
question = [ "1. How many days are there in a week?",
    "2. What is the capital of India?",
    "3. Which planet is known as the Red Planet?",
    "4. Who wrote the Indian national anthem?",
    "5. What is the chemical symbol for gold?",
    "6. Which gas do plants absorb during photosynthesis?",
    "7. Who was the first Indian to travel into space?",
    "8. Which is the smallest prime number greater than 50?",
    "9. Which scientist formulated the three laws of planetary motion?",
    "10. What is the value of the Euler totient function φ(36)?"]
answer = ["7","new delhi","mars","rabindranath tagore","au","carbon dioxide","rakesh sharma","53","johannes kepler","12"]
count = 0
lost = False
quit_game = False
prizes = [2000, 4000, 8000, 10000, 20000,
          50000, 100000, 500000, 1000000, 10000000]
for i in range(10):
    if i >= 6:
        print("remember: if you lose you get nothing")
    print(question[i])
    print("if you dont wanna continue type quit or continue with typing answer")
    answer1= input("enter your answer: ").lower()
    if answer1 == "quit":
        quit_game = True
        break
    if answer1 != answer[i] and i>=6:
        lost = True
    if answer1 == answer[i]:
        print("you are right")
        count += 1
    else:
        print("you are wrong")
        break
if lost:
    print("you earn nothing")
elif quit_game:
    print("you earned", prizes[count-1]  if count > 0 else "0")

elif count ==0:
    print("seriously bro")

else:
    print("you earned", prizes[count-1])
