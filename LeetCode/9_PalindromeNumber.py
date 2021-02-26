class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]


# Below has less time consuming code but looks complex
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        half_index = len(string) // 2
        for i in range(half_index):
            rev = -i-1
            if string[i] != string[rev]:
                return False
        return True
                
'''