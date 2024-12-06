import csv
from random import randint

with open('dictionary.csv', 'r', encoding='UTF-8') as file:
    dictionary = list(csv.reader(file))
    quit = False
    print('It\'s time to test your German! Enter Q to quit.\n')
    
    while True:
        attempt_num = 0
        index = randint(1,len(dictionary)-1)
        word = dictionary[index][3]
        
        
        print('Was ist das: ' +  word)
        guess = input()

        if dictionary[index][4] == 'noun':
            target = dictionary[index][0] + ' ' + dictionary[index][1]
        else:
            target = dictionary[index][1]

        if guess == 'Q':
            break

        while True:
            
            if guess == target:
                print('\nGenau!\n')
                break
            else:
                attempt_num += 1
                if attempt_num != 2:
                    print('\nNochmal, was ist das: ' + word)
                    guess = input()
                else:
                    print(f'\nNein, das ist {target}\n')
                    break

                
