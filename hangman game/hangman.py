"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The program choose a random word to let users play hangman game.
    After player inputs a alpha, the program would tell them they are right or wrong,
    and how many times they can guess.
    In the end, the program would show the answer to player.
    """
    answer = random_word()
    dashed_answer = dashed(answer)
    new_ans = dashed_answer
    print('The word looks like: '+str(dashed_answer))
    steps = N_TURNS
    print('You have '+str(steps)+' guesses left.')
    guess(answer, new_ans, steps)


def guess(answer, new_ans, steps):
    """
    These steps help the program know when to stop the game.
    :param answer: the random word chose by the program.
    :param new_ans: to show player how many letters they are right and how many words they have to guess.
    :param steps: integer, the number of guess the player has.
    :return: the program would tell player they are right or wrong after they input an alpha.
    """
    while steps != 0:
        if new_ans == answer:
            break
        else:
            input_ch = input('Your guess: ')
            if not input_ch.isalpha():
                # If users input not alpha (such as integer), the program will ask users to input again.
                print('Illegal format.')
            elif len(input_ch) != 1:
                # If users input more than one alpha, the program will ask users to input again.
                print('Illegal format.')
            else:
                upper_input = upper(input_ch)
                if answer.find(upper_input) == -1:
                    steps = steps - 1
                new_ans = solve(upper_input, answer, new_ans, steps)


def solve(upper_input, answer, new_ans, steps):
    """
    :param upper_input: upper alpha, depending on the alpha player inputs.
    :param answer: the random word chose by the program.
    :param new_ans: to show player how many letters they are right and how many words they have to guess.
    :param steps: integer, the number of guess the player has.
    :return: the program would tell player they are right or wrong after they input an alpha.
    """
    if upper_input in answer:
        ans = ''
        m = answer.find(upper_input)
        ans += new_ans[0:m]
        ans += answer[m:(m+1)]
        ans += new_ans[(m+1):]
        new_ans = ans
        if upper_input in answer[(m+1):]:
            # When the users input an alpha, which having two identical letters in the random word.
            ans = ''
            n = answer[(m+1):].find(upper_input)
            ans += new_ans[0:(m+1+n)]
            ans += answer[(m+1+n):(m+1+n+1)]
            ans += new_ans[(m+1+n+1):]
            new_ans = ans
            if upper_input in answer[(m+1+n+1):]:
                # When the users input an alpha, which having three identical letters in the random word.
                ans = ''
                p = answer[(m+1+n+1):].find(upper_input)
                ans += new_ans[0:(m+1+n+1+p)]
                ans += answer[(m+1+n+1+p):(m+1+n+1+p+1)]
                ans += new_ans[(m+1+n+1+p+1):]
                new_ans = ans
        print('You are correct!')
        if not new_ans == answer:
            print('The word looks like: '+str(new_ans))
            print('You have '+str(steps)+' guesses left.')
        else:
            print('You win!')
            print('The word was: '+str(answer))
    else:
        print("There is no " + str(upper_input) + "'s in the word.")
        print('The word looks like: ' + str(new_ans))
        if steps != 0:
            print('You have ' + str(steps) + ' guesses left.')
        else:
            print('You are completely hung : (')
            print('The word was: ' + str(answer))
    return new_ans


def upper(input_ch):
    """
    If users input lower case, the program would upper it.
    :param input_ch: an alpha, users input to run the program.
    :return: upper alpha.
    """
    ans = ''
    if input_ch.islower():
        ans += input_ch.upper()
    else:
        ans += input_ch
    return ans


def random_word():
    """
    Players can play hangman depending on the words below.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def dashed(answer):
    """
    Because the program cannot show the answer to players in the beginning,
    the program should cover the answer.
    :param answer: a random word chose by the program.
    :return: to change the answer into "-", depending on the number of the answer.
    """
    ans = ''
    for i in answer:
        if i.isalpha():
            ans += '-'
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
