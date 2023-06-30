# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


# easy way https://stackoverflow.com/questions/22161075/how-to-scramble-the-words-in-a-sentence-python
def easy_random_method(word):
    random_word_list = list(word)
    random.shuffle(random_word_list)
    easy_random = ' '.join(random_word_list)
    return easy_random

def hard_random_method(word):
    count = 0
    list_word = list(word)
    char_replace = []
    for index in list_word:
        if count == 1:
            char_replace.append(index)
            list_word.remove(index)
        if count == 3:
            list_word.insert(count, char_replace[0])
        count += 1
    hard_word = ' '.join(list_word)
    return hard_word
def main():
    user_word = input("Enter a word: ")
    easy_random_word = easy_random_method(user_word)
    hard_random_word = hard_random_method(user_word)
    print("Your original word: ", user_word, "\n Now Mixed up: \n", "my way -> ", hard_random_word, "\n",
          "random lib way: ", "\n", easy_random_word)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()