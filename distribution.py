"""
distribution.py
Author: Will Laycock
Credit: Me

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

text = input("Please enter a string of text (the bigger the better): ")
s=list(text)
ac=(s.count('a'))
bc=(s.count('b'))
cc=(s.count('c'))
dc=(s.count('d'))
ec=(s.count('e'))
fc=(s.count('f'))
gc=(s.count('g'))
hc=(s.count('h'))
ic=(s.count('i'))
jc=(s.count('j'))
kc=(s.count('k'))
lc=(s.count('l'))
mc=(s.count('m'))
nc=(s.count('n'))
oc=(s.count('o'))
pc=(s.count('p'))
qc=(s.count('q'))
rc=(s.count('r'))
sc=(s.count('s'))
tc=(s.count('t'))
uc=(s.count('u'))
vc=(s.count('v'))
wc=(s.count('w'))
xc=(s.count('x'))
yc=(s.count('y'))
zc=(s.count('z'))

print('The distribution of characters in "{0}" is: '.format())

