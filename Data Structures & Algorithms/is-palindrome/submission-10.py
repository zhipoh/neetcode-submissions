class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use ord(x)
        def checkalnum(char):
            if ord('0') <= ord(char) <= ord('9') or ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z'):
                return True
            return False
        
        res = ""
        for char in s:
            if checkalnum(char):
                res+=char.lower()
        print(res)
        print(res[::-1])
        return res == res[::-1]

    
    