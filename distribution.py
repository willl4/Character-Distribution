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
q,t=zip(*z)
print(q)
print('The distribution of characters in "{0}" is: '.format(text))

if q[0] > 0:
    print((q[0])*(t[0]))
if q[1] > 0:
    print((q[1])*(t[1]))
if q[2] > 0:
    print((q[2])*(t[2]))
if q[3] > 0:
    print((q[3])*(t[3]))
if q[4] > 0:
    print((q[4])*(t[4]))
if q[5] > 0:
    print((q[5])*(t[5]))
if q[6] > 0:
    print((q[6])*(t[6]))
if q[7] > 0:
    print((q[7])*(t[7]))
if q[8] > 0:
    print((q[8])*(t[8]))
if q[9] > 0:
    print((q[9])*(t[9]))
if q[10] > 0:
    print((q[10])*(t[10]))
if q[11] > 0:
    print((q[11])*(t[11]))
if q[12] > 0:
    print((q[12])*(t[12]))
if q[13] > 0:
    print((q[13])*(t[13]))
if q[14] > 0:
    print((q[14])*(t[14]))
if q[15] > 0:
    print((q[15])*(t[15]))
if q[16] > 0:
    print((q[16])*(t[16]))
if q[17] > 0:
    print((q[17])*(t[17]))
if q[18] > 0:
    print((q[18])*(t[18]))
if q[19] > 0:
    print((q[19])*(t[19]))
if q[20] > 0:
    print((q[20])*(t[20]))
if q[21] > 0:
    print((q[21])*(t[21]))
if q[22] > 0:
    print((q[22])*(t[22]))
if q[23] > 0:
    print((q[23])*(t[23]))
if q[24] > 0:
    print((q[24])*(t[24]))
if q[25] > 0:
    print((q[25])*(t[25]))
