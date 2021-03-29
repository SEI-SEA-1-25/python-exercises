# Write a function called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   print(letter)
#
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
# dd = {}
# dd["foo"] = 1
# dd["foo"] += 1
# if "foo" in dd:
#   print(dd["foo"])
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 3}

def letter_count(string):
  # this is where the unique letters
  dd = {}
  # strings can be looped like lists
  for letter in string:
    # check if the current string is in the dict or not
    if letter not in dd:
      # if the letter is not found, create it!
      dd[letter] = 1
    else: 
      # otherwise, if it is found, increment it!
      dd[letter] += 1

  return dd

soln = letter_count('some other strings too. Like Spam. 🐍🐍')

print(soln)

# we want this
banana_dict = {
  'b': 1,
  'a': 3,
  'n': 2
}
