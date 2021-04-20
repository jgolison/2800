# we use itertools to create all possible combinations of a certain length
import itertools

# main function, which handles putting together all of the individual expressions
# into the final boolean expression
def main_func(worddict):
    # create all possible word-combos
    word_combos = covers(worddict)[1]
    # and the covers expression, checking to see if all the words together
    # cover the entire gameboard of characters
    word_covers = covers(worddict)[0]
    count = 0
    fin = ""
    # loops through all word combinations and creates an expression for that
    # particular word combo
    while count < len(word_covers):
        # fetches the valid statement
        valid_statement = valid(word_combos[count])
        # appends the word covers, word flows, and valid statements together
        fin = fin + "(" + word_covers[count] + " AND " + flows(word_combos[count][0], word_combos[count][1], 
              word_combos[count][2]) + " AND " + valid_statement + ")" + " OR "
        count +=1
    # because the above loop will add " OR " even to the last clause, we just
    # slice the last four characters off the end
    fin = fin[:-4]
    return fin
    
    
# creates the covers expression to check whether all of the words together
# cover the entire gameboard, as well as all of the possible word combos
def covers(worddict):
    # itertools easily allows combination calculating of a fixed length
    combos = list(itertools.combinations(worddict, 3))
    covers_list = []
    # this loop creates the actual covers expression
    for word_combo in combos:
        str = ""
        for word in word_combo:
            str = str + word + "-"
        str = str + "covers"
        covers_list.append(str)
    # since having both the list of combinations and the covers expression
    # are helpful later, we return both
    return covers_list, combos


#Creates the wxwywzflow? subexpression given w1, w2, and w3.
#Adds no spaces padding to beginning or end.
def flows(w1, w2, w3):
    # with three words, there are six possible orderings of how the words
    # could follow one another. if even one of these orderings flows,
    # this means the flows expression is satisfied. so, we create the
    # six possible flow orderings, and attach the orderings with " OR "
    # to represent that only one of these must be satisfied.
    l1 = "((%s->%s AND %s->%s) OR " % (w1, w2, w2, w3) 
    l2 = "(%s->%s AND %s->%s) OR " % (w1, w3, w3, w2)
    l3 = "(%s->%s AND %s->%s) OR " % (w2, w3, w3, w1)
    l4 = "(%s->%s AND %s->%s) OR " % (w2, w1, w1, w3)
    l5 = "(%s->%s AND %s->%s) OR " % (w3, w2, w2, w1)
    l6 = "(%s->%s AND %s->%s))" % (w3, w1, w1, w2)
    result = l1 + l2 + l3 + l4 + l5 + l6
    return result

# function to create the valid? expression, given
# a gameboard and a set of words, checks if all of the words are valid
def valid(combos):
    # a list that will eventually contain all alphabetized letter combos
    letter_combos = []
    count = 0
    while count < len(combos):
        # if any of the words have 2 or fewer letters in them, we don't need
        # to iterate through them to find all 2 character substrings
        if len(combos[count]) <= 2:
            # this appends the alphabetized string to the final list
            letter_combos.append(''.join(sorted(combos[count])))
        else:
            inner_count = 0
            # for all larger words, this will iterate through and find all
            # overlapping 2 character substrings of a string
            while inner_count < len(combos[count]) - 1:
                # and then alphabetizes the strings and appends to final list
                letter_combos.append(''.join
                                     (sorted(combos[count][inner_count] + 
                                             combos[count][inner_count + 1])))
                inner_count +=1
        count +=1
    # converting a list into dictionary keys and then back into a list is
    # an easy way to remove any duplicates, because dict keys are unique.
    # we do not need duplicates - we only need to check the validity of a 
    # substring once. ordering does not matter. if "hi" is valid, so is "ih",
    # which is why we choose to alphabetize and remove duplicates.
    letter_combos = list(dict.fromkeys(letter_combos))
    # from here, we just need to add the DS (duplicate side) and AND 
    # to the letter combinations
    final_string = ""
    for each in letter_combos:
        final_string = final_string + "DS" + " AND "  + each
    # this loop will add an extra "DS AND " at the beginning; this slices it out
    final_string = final_string[7:]
    # it will also not add the last "DS" at the end, so we add it in
    final_string = final_string + "DS"
    # the string is now complete
    return final_string

# Tests that with a word included that is longer than 2/3 characters, valid
# creates all the letter combinations we want    
def test_valid():
    assert valid(["ahe", "hi", "verylongword"]) == """ahDS AND ehDS AND hiDS AND evDS AND erDS AND ryDS AND lyDS AND loDS AND noDS AND gnDS AND gwDS AND owDS AND orDS AND drDS"""
    
# Tests that valid, when given words it will need to alphabetize, does so
# Also tests that valid works properly on just a single word, i.e. does not
# add " AND " but does add "DS"
def test_valid_alph():
    assert valid(["he"]) == "ehDS"    

if __name__ == "__main__":
    test_valid()
    test_valid_alph()
    print("Everything passed")







