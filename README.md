# 2800
Final Project Draft


Code Description:

  Our code has one main function for handling the input of the gameboard and the word dictionary and managing calling all of the helper functions and aggregating their outputs, and then three helper functions that create the SAT encodings for each problem constraint. There is one helper function to handle the “covers” constraint, one to handle the “flows” constraint, and one to handle the “valid” constraint. 
	
  The covers constraint in the code creates an expression representing the fact that the combination of the three words given must cover all of the letters on the board. The flows constraint creates an expression representing the need for a word to flow from its antecedent word in the solution. The validity constraint creates an expression representing that each word must only contain letters that are following the side-adjacent rule.
	
  Together, the main function takes all of the possible combinations of three words in the dictionary, and creates expressions representing the need to satisfy each of these three constraints. In the end, it returns an expression representing the state of options in the game which will either resolve to True, so the Letter Boxed is satisfiable, or False, so the Letter Boxed is not satisfiable.

