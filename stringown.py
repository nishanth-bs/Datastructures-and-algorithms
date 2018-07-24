"""
Baps was a highly motivated student. Once Baps decided to develop his own language which he called as plusequals language. + and = are his favorite symbols. So he decided that for any string in his language, it must only be composed of + and = symbols with optional several letters between them.
Also for any string to satisfy the rules of the language, each letter must be surrounded by a + symbol. He now wants a program which can indentify if any given string is a word in his language and if not return the first position the letter which violates the rules of the language.
Help him develop a language classifier for the same.

Sample input 1:
+d+=3=+s+
Sample output 1:
YES

Sample input 2:
f++d+
Sample output 2:
1
1st letter is not surrounded by + on either side of it, thereby violating the language rules

Sample input 3:
+f+a+b=
Sample output 3:
6
6th letter is not surrounded by + on either side of it

"""
def check1(s):
    s = list(s)
    prev,cur = s[0],s[0]
    for k,i in enumerate(s):
        cur = i
        #print(cur,prev,k)
        if cur.isalpha():
            if prev != '+' or (k== len(s)-1  or s[k+1] != '+'):
                return k
            
        prev = i
    return "YES"


print(check1("55"))
