# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from array import array
from pandas.core.common import flatten
from itertools import izip_longest

def main():
    f = open('words.txt', 'r')
    contents = f.read()
    f.close()

    sample_letters = [['l', 'w', 'c'], ['u', 'o', 's'], ['n', 'h', 'd'], ['i', 'r', 'e']]

    sample_words = ["hire", "while", "loose", "zoo", "biological", "moot"]

    new_words = check_letters(sample_letters, sample_words)
    num_list = category(sample_letters, new_words)
    #print check_letters(sample_letters, sample_words)
    arr = rem_chars(contents.split('\n'))
    new_arr = check_letters(sample_letters, arr)
    #print new_arr
    check_alternating(num_list)
    cat = category(sample_letters, new_arr)
    cat2 = check_alternating(cat)

    for each in cat2:
        lst = starts(list(each), cat2)
        if check_solution(sample_letters, lst):
            return lst
            break
        else:
            next


def check_letters(letters, words):
    letters = (list(flatten(letters)))
    to_remove = []

    for each in words:
        for char in each:
            if char not in letters:
                to_remove.append(each)

    for word in to_remove:
        if word in words:
            words.remove(word)

    return words


def category(letters, words):
    num_list = []
    ls1 = letters[0]
    ls2 = letters[1]
    ls3 = letters[2]
    ls4 = letters[3]

    for each in words:
        inner_list = []
        for char in each:
            if char in ls1:
                inner_list.append(1)
            elif char in ls2:
                inner_list.append(2)
            elif char in ls3:
                inner_list.append(3)
            else:
                inner_list.append(4)
        num_list.append([inner_list, each])

    return num_list



def rem_chars(arr):
    lst = []
    for each in arr:
        lst.append(each[:-1])

    return lst



def check_alternating(num_list):
    final_list = []

    for each in num_list:
        for x in each:
            if type(x) is list:
                res = [i for i, j in izip_longest(x, x[1:])
                        if i != j]
                if len(res) < len(x):
                    next
                else:
                    final_list.append(each)
    for every in final_list:
        del every[0]

    return final_list



def starts(str_lst, word_list):
    count = 0
    while count <= len(word_list) - 1 and len(str_lst) < 5:
        len_list = len(str_lst) - 1
        print "start"
        print len_list
        print word_list[count]
        print len(str_lst[len_list]) - 1
        print str_lst

        letter_index = len(str_lst[len_list]) - 1
        letter = str_lst[len_list][letter_index]

        print letter_index
        print letter
        if word_list[count][0] == letter:
            print word_list[count]
            print word_list[count + 1]
            str_lst.append(word_list[count])
            del word_list[count]
            print word_list[count]
        count += 1
        #print count
        #print len(str_lst)
    return str_lst


def check_solution(lst_words, lst_letters):
    letters = (list(flatten(lst_letters)))
    set_letters = set(letters)
    word_letters = []
    for each in lst_words:
        lst = list(each)
        for x in lst:
            word_letters.append(x)

    set_word = set(word_letters)
    return set_letters.issubset(set_word)


main()








