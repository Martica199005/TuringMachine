# TuringMachine

The objectives of the theme are to understand and deepen the way a Turing Machine works, what is a configuration of a Turing machine, the acceptance of a word as well familiarization with Python language; keyboard reading, using arrays and a dictionaries.

A Turing machine M represents a tuple (K, Σ, δ, q, F) where: K is the set of states of M Σ - the alphabet of the machine δ: K x Σ → K x Σ x {L, R, H} - transition function q - initial state 0 F - the set of final states

To encode a Turing machine, we will use the following conventions:

-The states are represented as consecutive integers, and the initial state is always 0

-The alphabet is the set of alphabetic ASCII characters, from A to Z and the symbol #.

-To the left and right of the word all positions are empty. Empty positions are mark explicitly with the symbol ‘#’ and may appear as input / output within transitions. If we end up in situations where to the left of the cursor or to the right we are left with an empty string "" we will add a "#"

-The execution of the machine stops when we can no longer transition from current condition.

The coding of a machine will have, on the first line, the number of states, on the second line, the list of the final states separated by space, and on the following lines, one transition at a time each line.

-readTM(): The input / output data files are provided line by line to stdin automatically redirected by the hackerrank from a file. First line - the type of task you are performing (a test contains only one type of task) The second line - the list of inputs based on which you will have to provide the output The third line - the number of states Fourth line - a list of final states The following lines, to the end of the file - each line represents a transition from your machine's delta.

Depending on the first line read there are 3 different functions:

-step():

It receives a Turing machine configuration and the rules as parameters and returns the resulting configuration after executing a step of the machine or False value if the machine stops.

A configuration will be encoded as a triplet (u, q, v) where: u - is the word to the left of the cursor q - is the current state v - is the word to the right of the cursor

The following functions are called from the step():

eliminate_parenthesis() : eliminates the parenthesis from the first and last element in list input_lines which is the list containing all the items of the 2 line read

rule_found(): check if for a given configuration there is the rule

go_right_1(), go_left_1(), hold() : depending on the applied rule they go on the left, on the right or hold on the current character

accept(): It receives as parameter a machine M (the final states, the number of states and the rules) and a word, and returns the Boolean value True, if the word is accepted, or False, if so contrary. ! This requirement guarantees that there will be no cycles in the machine. !

k_accept(): It receives as a parameter an integer k, a machine M (the final states, the number of states and the rules) and a word w, and returns the Boolean value True, if the word is accepted in k, or False, otherwise. ! FOR THIS REQUIREMENT THERE CAN BE CYCLES IN THE MACHINE. !
