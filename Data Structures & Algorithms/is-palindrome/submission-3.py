class Solution:
    def isPalindrome(self, s: str):
        clean=[]
        for word in s:
            if word!=' ' and word.isalnum():
                letter=word.lower()
                clean.append(letter)
        n=len(clean)
        f=[None]*n
        v=0
        for letter in range(n-1,-1,-1):
            f[letter]=clean[v]
            v=v+1

        return clean==f