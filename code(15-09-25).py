#Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        count=0
        words=text.split(' ')
        for word in words:
            wrong=False
            for j in brokenLetters:
                if j in word:
                    wrong=True
                    break
            if not wrong:
                count+=1
        print(count)
text=input("Enter text: ")
brokenLetters=input("Enter brokenLetters: ")
sol=Solution()
sol.canBeTypedWords(text,brokenLetters)    