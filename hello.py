#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""


#The python interpreter is like an "instance" and can be used for testing
#Like,try set a = 6, then a + 2, then a = "hello", then a + " world"
#argc = argument count, argv = argument vector
#so, len(sys.argv) = argc


# Function Variables are local to the function

import sys

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    #sys.argv contains the command line arguments, 0 is the script itself
    name = sys.argv[1]
  else:
    name = 'World'
  print('Howdy!', name)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()


# Don't forget the * repeat operator

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
  """
  Returns the string 's' repeated 3 times.
  If exclaim is true, add exclamation marks.
  """

  result = s + s + s #Could also use "s * 3" which is faster
                     # Because it only calculates 1 time
                     # + + + does the calculation 3 times.

  if exclaim:
    result = result + "! ! !"
  return result               