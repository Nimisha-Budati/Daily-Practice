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

        
        