import data
import random
index = random.randint(126, 158)
a=input('press to generate ')
if a!=' ':
    print(index,":",data.problems[index])
    cont = True
    showAnswer = True
    while cont:
        answer = input("Show the answer? press 'y' if yes or write the answer ")
        if answer == 'y':
            print(index,":", data.answers[index])
            generate = input("generate another? press 'y' if yes and 'n' if no ")
            if generate == 'y':
                index = random.randint(126, 149)
                print(index,":",data.problems[index])
            else:
                cont = False
            
        else:
            showAnswer = True
            while showAnswer:
                if int(answer) == data.answers[index]:
                    print('Right')
                    generate = input("generate another? press 'y' if yes and 'n' if no ")
                    if generate == 'y':
                        index = random.randint(126, 149)
                        print(index,":",data.problems[index])
                        answer = input("write the answer here ")
                    else:
                        showAnswer = False
                        cont = False
                else:
                    print("Wrong. Try Again")
                    answer = input("write the answer here ")
