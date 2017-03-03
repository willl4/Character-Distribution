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

c=[ac,bc,cc,dc,ec,fc,gc,hc,ic,jc,kc,lc,mc,nc,oc,pc,qc,rc,sc,tc,uc,vc,wc,xc,yc,zc]
l=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
z=zip(c,l)

def compare(a, b):
    if a[0]>b[0]:
         return True
    elif a[0]<b[0]:
        return False
    elif a[0]==b[0] and a[1]>b[1]:
        return True
    elif a[0]==b[0] and a[1]<b[1]:
        return False
        
        
   

def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it

print('The distribution of characters in "{0}" is: '.format(text))

print("a"*ac)
print("b"*bc)
print("c"*cc)
print("d"*dc)
print("e"*ec)
print("f"*fc)
print("g"*gc)
print("h"*hc)
print("i"*ic)
print("j"*jc)
print("k"*kc)
print("l"*lc)
print("m"*mc)
print("n"*nc)
print("o"*oc)
print("p"*pc)
print("q"*qc)
print("r"*rc)
print("s"*sc)
print("t"*tc)
print("u"*uc)
print("v"*vc)
print("w"*wc)
print("x"*xc)
print("y"*yc)
print("z"*zc)




