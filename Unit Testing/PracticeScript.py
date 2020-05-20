# Unit Test Practice Exercise

import random

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You got the right number!')
            return True
    else:
        print('Only numbers between 1 and 10')
            

if __name__ == '__main__':   
    answer = random.randint(1,10)
    # print(answer)
    
    while True:
        try:
            guess = int(input('Guess a number from 1-10: '))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print('Please enter the number')
            continue
        

