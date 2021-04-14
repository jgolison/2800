import itertools
# ^ use this to actually create all the possible word/etc combinations

# One dimensional array containing all words in the dictionary
# Stipulated that this will only contain words with letters contained on 
# the gameboard
worddict = ["ahe", "edb", "bgfc", "ahd", "letter", "fun", "words!"]
# Two dimensional array containing the actual gameboard
# Two dimensional so that letters in each distinct subarray can be on the same
# "side"
gameboard = [['c', 'd'], ['e', 'f'], ['g', 'h'], ['a', 'b']]

def main_func(worddict, gameboard):
    # create all possible word-combos
    word_combos = covers(worddict)[1]
    word_covers = covers(worddict)[0]
    count = 0
    fin = ""
    while count < len(word_covers):
        # right now, this code does not include statements for "valid?"
        # but this is where we would call to the skeleton function below
        # called "valid" and add that as part of our final expression
        fin = fin + "(" + word_covers[count] + " AND " + flows(word_combos[count][0], word_combos[count][1], word_combos[count][2]) + ")" + " OR "
        count +=1
    fin = fin[:-3]
    return fin
    
    
# creates the covers expression to check whether all of the words together
    # cover the entire gameboard
def covers(worddict):
    combos = list(itertools.combinations(worddict, 3))
    covers_list = []
    for word_combo in combos:
        str = ""
        for word in word_combo:
            str = str + word + "-"
        str = str + "covers"
        covers_list.append(str)
    return covers_list, combos

#Creates the wxwywzflow? subexpression given w1, w2, and w3.
#Adds no spaces padding to beginning or end.
def flows(w1, w2, w3):
    l1 = "((%s->%s AND %s->%s) OR " % (w1, w2, w2, w3) 
    l2 = "(%s->%s AND %s->%s) OR " % (w1, w3, w3, w2)
    l3 = "(%s->%s AND %s->%s) OR " % (w2, w3, w3, w1)
    l4 = "(%s->%s AND %s->%s) OR " % (w2, w1, w1, w3)
    l5 = "(%s->%s AND %s->%s) OR " % (w3, w2, w2, w1)
    l6 = "(%s->%s AND %s->%s))" % (w3, w1, w1, w2)
    result = l1 + l2 + l3 + l4 + l5 + l6
    return result

# unfinished function to create the valid? expression, given
    # a gameboard and a set of words, checks if all of the words are valid
def valid(combos, gameboard):
    return ""



print(main_func(worddict, gameboard))