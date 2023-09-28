#Problem 6
def count(l):
    l=list(enumerate(l))
    #print (l)
    c=0
    for x in l:
        if(x[0]==x[1]):
            c+=1
    print(c)  

count([0,2,2,1,5,5,6,10])

#prob 5
def d_list(l):
    d={}
    a=list(enumerate(l))
    #print(a)
    for x in a:
        d[x[1]]=x[0]
    print(d)

d_list(['a','b','c'])

#prob4
def concatenate(L1 , L2 , connector):
    z=list(zip(L1,L2))
    ans=[x[0]+connector+x[1] for x in z]
    print(ans)
concatenate(['A','B'],['a','b'],'-')

#prob1
def lenth(phrase):

    return list(map(len,phrase.split()))

lst=lenth('How long are the words in this phrase')
print(lst)

#prob3
def filter_words(word_list,letter):
    ans= list(filter(lambda x: x.startswith(letter), word_list))
    print(ans)

filter_words(["Hello","Hi","Wow"],"H")

#prob2
from functools import reduce

def digits_to_num(digits):
    
    return reduce(lambda x,y: 10*x+y, digits)
a=digits_to_num([3,4,3,2,1])
print(a)




#prob3
"""def filter_words(word_list, letter):
    
    return filter(lambda x: x[0] == letter,  word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
n=list(filter_words(l,'H'))
print(n)"""
