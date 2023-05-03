questions = ("What is python?: ",
           "Who created python?: ",
           "What is the purpose of python?: ",
           "What is the difference between python1 2 and python 3?: ",
           "What is the syntax for a single-line comment in python?: ",
           "What is the function of the print statement in python?: ",
           "What is the difference between a list and a tuple?: ",
           "What is the purpose of a conditional statement in python?: ",
           "What is the purpose of a loop in python?: ",
           "What is the purpose of an if statement in python?: ")

    

options=(("A.A type of snake","B.A programming language","C.A game engine","D.An operating system"),
         ("A.Guido van Rossum","B.Linus Torvals","C.Bill Gates","D.Steve Jods"),
         ("A.To create websites","B.To develo video games","C.To automate task","D.To create mobile apps"),
         ("A.python 2 is faster than python 3","B.python 2 is nolonger supported,while python 3 is the current version","C.python 2 is easy to learn than python 3","D.There is no difference between python 2 and python 3"),
         ("A.//","B.#","C./*","D.<!-- -->"),
         ("A.To display output on the screen","B.To accept user input","C.To define a variable","D.To perform a mathematical operations"),
          ("A.A list is mutable ,while a tupple is immutable","B.A list is enclosed in parentheses,while a tuple is enclosed in square brackets","C.A list can only contain intergers,while a tuple can contain any data type","D.There is no difference between a list and a tuple in python"),
         ("A.To define a function","B.To loop through a sequence","C.To perform a mathematical operations","D.To execute difference code depending on a condition"),
         ("A.To define a function","B.To perform a mathematical operations","C.To execute code repeatedly","D.To sort a list"),
         ("A.To define a function","B.To loop through a sequence","C.To perform a mathematical operations","D.To excecute code conditionally"))
         

answers=("B","A","D","C","C","A","A","D","C","D")
guesses=[]
score=0
questions_num=0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    guess=input("Enter(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[questions_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[questions_num]} is the correct answer")    
    questions_num+=1
    
print("-------------")
print("   RESULTS   ")
print("-------------") 
print("answer: ",end="") 
for answer in answers:
    print(answer,end="")
print()
print("guesses: ",end="") 
for guess in guesses:
    print(guess,end=" ") 
print()      
     
    
score=int(score / len(questions) * 100)
print(f"your score is:{score}%")      
    
    