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

ss=list(text)

ac=(ss.count('a'))
bc=(ss.count('b'))
cc=(ss.count('c'))
dc=(ss.count('d'))
ec=(ss.count('e'))
fc=(ss.count('f'))
gc=(ss.count('g'))
hc=(ss.count('h'))
ic=(ss.count('i'))
jc=(ss.count('j'))
kc=(ss.count('k'))
lc=(ss.count('l'))
mc=(ss.count('m'))
nc=(ss.count('n'))
oc=(ss.count('o'))
pc=(ss.count('p'))
qc=(ss.count('q'))
rc=(ss.count('r'))
sc=(ss.count('s'))
tc=(ss.count('t'))
uc=(ss.count('u'))
vc=(ss.count('v'))
wc=(ss.count('w'))
xc=(ss.count('x'))
yc=(ss.count('y'))
zc=(ss.count('z'))

a=[ac,bc,cc,dc,ec,fc,gc,hc,ic,jc,kc,lc,mc,nc,oc,pc,qc,rc,sc,tc,uc,vc,wc,xc,yc,zc]
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
z=list(zip(a,b))

def compare(a, b):
    if a[0]>b[0]:
         return True
    elif a[0]==b[0] and a[1]<b[1]:
        return True
    else:
        return False
        
        
   

def bsort(z, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(z): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(z[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    z[index-1], z[index] = z[index], z[index-1] # and swap it
bsort(z, compare)
zip(*z)

print('The distribution of characters in "{0}" is: '.format(text))

if a[0] > 0:
    print(int((a[0])*(b[0])))
if a[1] > 0:
    print(int((a[1])*(b[1])))
if a[2] > 0:
    print(int((a[2)*(b[2])))
if a[3] > 0:
    print(int((a[3])*(b[3])))
if a[4] > 0:
    print(int((a[4])*(b[4])))
if a[5] > 0:
    print(int((a[5])*(b[5])))
if a[6] > 0:
    print(int((a[6])*(b[6])))
if a[7] > 0:
    print(int((a[7])*(b[7])))
if a[8] > 0:
    print(int((a[8])*(b[8])))
if a[9] > 0:
    print(int((a[9])*(b[9])))
if a[10] > 0:
    print(int((a[10])*(b[10])))
if a[11] > 0:
    print(int((a[11])*(b[11])))
if a[12] > 0:
    print(int((a[12])*(b[12])))
if a[13] > 0:
    print(int((a[13])*(b[13])))
if a[14] > 0:
    print(int((a[14])*(b[14])))
if a[15] > 0:
    print(int((a[15])*(b[15])))
if a[16] > 0:
    print(int((a[16])*(b[16])))
if a[17] > 0:
    print(int((a[17])*(b[17])))
if a[18] > 0:
    print(int((a[18])*(b[18])))
if a[19] > 0:
    print(int((a[19])*(b[19])))
if a[20] > 0:
    print(int((a[20])*(b[20])))
if a[21] > 0:
    print(int((a[21])*(b[21])))
if a[22] > 0:
    print(int((a[22])*(b[22])))
if a[23] > 0:
    print(int((a[23])*(b[23])))
if a[24] > 0:
    print(int((a[24])*(b[24])))
if a[25] > 0:
    print(int((a[25])*(b[25])))






