# Brainfuck Encoded Concatenative Calculus

File becc.py contains an expression evaluator for [BECC](https://esolangs.org/wiki/Brainfuck_Encoded_Concatenative_Calculus).
It implements two functions:


## `evaluate(s, debug=False, calc=False)`

  - `s`: expression string to be evaluated
  
  - `debug`: Enable debug mode which steps through evaluation one command at a time.
  
  - `calc`: Instead of returning the reduced expression return the number of times `$` operator was called. Used for decoding Church-encoded numbers for output.

Main evaluator functionality. Will reduce the expression and return it, unless `calc` flag is set.


## `encode_nat(n)`

  - `n`: number to be encoded

Returns a string representing and unquoted Church-encoded number. For example `encode_nat(2)` will return "+<+-+-".