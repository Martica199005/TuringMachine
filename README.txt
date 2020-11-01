
The objectives of the theme are to understand and deepen the way a Turing Machine works, what is a configuration of a Turing machine, 
the acceptance of a word as well familiarization with Python language; keyboard reading, using arrays and a
dictionaries.

A Turing machine M represents a tuple (K, Σ, δ, q, F) where: 
K is the set of states of M
Σ - the alphabet of the machine
δ: K x Σ → K x Σ x {L, R, H} - transition function
q - initial state 0
F - the set of final states

0) Reading a MT from a keyboard :
Implement a readTM function that receives a string that contains an encoding
Turing machines and returns an internal representation of it. Hint: For this from
then you can use tuples and Python dictionaries.

To encode a Turing machine, we will use the following conventions:

-The states are represented as consecutive integers, and the initial state is
always 0

-The alphabet is the set of alphabetic ASCII characters, from A to Z and the symbol
#.

-To the left and right of the word all positions are empty. Empty positions are
mark explicitly with the symbol ‘#’ and may appear as input / output within
transitions. If we end up in situations where to the left of the cursor or to the right
we are left with an empty string "" we will add a "#"

-The execution of the machine stops when we can no longer transition from current condition.

The coding of a machine will have, on the first line, the number of states, on the second line, the list of the final states separated by space, and on the following lines, one transition at a time each line.

Example:
2
0 1
0 a 1 b L

The machine above has two states, 0 and 1, and both are final. The only transition to
its is δ (0, a) = (1, b, L).

-readTM():
The input / output data files as an example the details are provided line by line to stdin automatically redirected by the hackerrank 
from a file. You will need to read:
First line - the type of task you are performing (a test contains only one type of task)
The second line - the list of inputs based on which you will have to provide the output
The third line - the number of states
Fourth line - a list of final states
The following lines, to the end of the file - each line represents a transition from your machine's delta
Reading keyboard data is part of solving the theme! What Hackerrank does automatically in the back is to redirect your input from the file to stdin, your program reads executes and prints, Hackerrank takes the output from stdout puts it in an output file and diffs between output and reference.

1) One step (⊢) of the execution of the Turing machine

Implement the step function, which receives a machine configuration as a parameter
Turing and returns the resulting configuration after executing a step of the machine or
False value if the machine stops.

A configuration will be encoded as a triplet (u, q, v) where:
u - is the word to the left of the cursor
q - is the current state
v - is the word to the right of the cursor

2) Accepting a word
Implement the accept function which receives as parameter a machine M and a word, and
returns the Boolean value True, if the word is accepted, or False, if so
contrary.
! This requirement guarantees that there will be no cycles in the machine. !

3) Accepting a word after k steps
Implement the k_accept function which receives as a parameter an integer k, a machine M and
a word w, and returns the Boolean value True, if the word is accepted in k, or
False, otherwise.
! FOR THIS REQUIREMENT THERE CAN BE CYCLES IN THE MACHINE. !

Test mode and structure of a test file:
There are three types of test files, each of which tests functionality
step, accept and k_accept functions.
A test file has the following structure:
● On the first line - the type of task.
● On the second line, a list of inputs corresponding to the task separated by space
● On the rest of the lines to the end of the text file the configuration of the M machine on which it is
will test the inputs

An output file will look like this:
● A line in which the separate output corresponding to the task is in order
through space.

Type 1:

input:
step
<config_1> <config_2>… <config_n>
<MT coding>
The second line contains a list of configurations that will represent one by one
the input of the step function defined at 1.
output:
<next_config_1> <next_config_2>… <next_config_n>
The output consists of the list of step-turned configurations for each element in
input.

Type 2:

input:
I accept
word_1 word_2… word_n
<MT coding>
The second line contains a list of words that will in turn represent the input
accept function defined in 2.
output:
bool_accept_1 bool_accept_2… bool_accept_n
The output consists of the list of Booleans corresponding to the answer I accept for
each element in the input.

Type 3:

The number of k steps corresponding to the word is delimited by it by a comma.
input:
k_accept
word_1, k_1 word_2, k_2… word_n, k_n
<MT coding>
The second line contains a list of pairs: (word, maximum number of transitions
permissions for the current word) which will in turn represent the input of the function
k_accept defined at 3.
output:
bool_k_accept_1 bool_k_accept_2… bool_k_accept_n








