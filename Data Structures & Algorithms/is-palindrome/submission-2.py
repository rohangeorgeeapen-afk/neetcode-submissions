class Solution:
    def isPalindrome(self, s: str):
        clean=[]
        clean2=[]
        for word in s:
            clean.append(word)
        for word in clean:
            if word!=' ' and word.isalnum():
                clean2.append(word)
        c="".join(clean2)
        d=c.lower()
        e=[]
        for letter in d:
            e.append(letter)
        n=len(e)
        f=[None]*n
        v=0
        for letter in range(n-1,-1,-1):
            f[letter]=e[v]
            v=v+1

        return e==f