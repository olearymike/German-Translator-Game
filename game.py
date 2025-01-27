import csv
import random

# This reads the csv file where all the words are stored and begins the game
with open('dictionary.csv', 'r', encoding='UTF-8') as file:
    dictionary = list(csv.reader(file))
    desired_set = ''
    desired_category = ''
    # The program asks the user which part of speech they would like to study. The code repeats until a specified PoS is selected, or if they select all.
    while True:
        desired_set = input('What part of speech would you like to work with? [\'nouns\', \'verbs\', \'adjectives\', \'adverbs\', or \'all\']: ')
        if desired_set == 'all':
            break
        elif desired_set == 'nouns' or desired_set == 'verbs' or desired_set == 'adjectives' or desired_set == 'adverbs':
            dictionary = [d for d in dictionary if desired_set in d]
            break
        else:
            continue
    
    # If applicable, the program asks the user if they'd like to study a specific category within their desired part of speech

    if desired_set == 'nouns':
        while True:
            desired_category = input('What category would you like to study? [\'clothes\', \'animals\', \'house\', \'body\', \'all\']: ')
            if desired_category == 'all':
                break
            elif desired_category == 'clothes' or desired_category == 'animals' or desired_category == 'house' or desired_category == 'body':
                dictionary = [d for d in dictionary if desired_category in d]
                break
            else:
                continue
            

    quit = False
    print('It\'s time to test your German! Enter Q to quit.\n')
    combo = 0
    
    # The program runs a loop until the letter 'Q' is inputted, causing the game to end
    while True:
        attempt_num = 0
        
        # "Randomly" generates a number between 0 and the number of lines in the csv file
        index = random.randint(1,len(dictionary) - 1)
        # Taking the index variable, it grabs an English word from the dictionary.csv
        word = dictionary[index][3]
        
        # Asks the user what the selected word is in German
        print('Was ist das: ' +  word)
        guess = input()

        # If the word is a noun, it adds the article behind the word
        # For example, if the word is "cat", the user would need to respond with "die Katze" instead of just "Katze"
        if dictionary[index][4] == 'nouns':
            target = dictionary[index][0] + ' ' + dictionary[index][1]
        else:
            target = dictionary[index][1]
        
        # If the user inputs Q, the program ends.
        if guess == 'Q':
            break

        while True:
            
            # If the user correctly guesses the word, they are congratulated, their combo is increased by 1, and the loop continues
            if guess == target:
                responses = ['Genau!', 'Richtig!', 'Sehr Gut!', 'Gute Arbiet!']
                combo += 1
                if combo % 5 == 0:
                    print(f'\n{random.choice(responses)}\nCombo: {combo}\n')
                else:
                    print(f'\n{random.choice(responses)}\n')
                break
            else:
                combo = 0
                # If their guess was incorrect, they get a strike and are asked the question again. The combo count also gets reset to 0
                attempt_num += 1
                if attempt_num != 2:
                    
                    print('\nNochmal, was ist das: ' + word)
                    guess = input()
                else:
                    # If the user guesses the word wrong twice, their strikes are set back to 0 and are told the correct answer
                    attempt_num = 0
                    print(f'\nNein, das ist {target}\n')
                    # The user is then again asked what the word means in German
                    print('Nochmal, was ist das: ' + word)
                    guess = input()
                    print('')
                    break

                
