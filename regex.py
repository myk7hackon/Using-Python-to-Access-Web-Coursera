import re

'''
^ :- starts with
. :- any character
* :- any number of repetition of any character
\S :- non white space character
+ :- one or more
[] :- represents one character
Greedy matching
? :- not greedy
() :- what to extract
[^ ] :- represents non blank character
\ :- escape character
'''

test_string = "nsdbamhbdhbq  nbmnfind"
test_email =  "From : mayank.parmar@gmail.com"
print(re.search("find",test_string))

print(re.search("^find",test_string))

print(re.search("find*",test_string))

print(re.search(r"bq\S+n",test_string))

print(re.findall(r"[a-c]+\S+",test_string))

print(re.findall("^n.",test_string))

print(re.search(r"bq.+?",test_string))

print(re.findall(r"From : (\S+@\S+)",test_email))

print(re.findall(r"From : \S+@(\S+)",test_email))




