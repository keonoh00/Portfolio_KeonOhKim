class Solution:
    def reverse(self, x: int) -> int:
        if x > abs(2**31) or x == 0:
            return 0
        if x < 0:
            neg = 1
            string = str(x)[1:]
        else:
            neg = 0
            string = str(x)
        reverse = ""
        for i in range(1, len(string)+1):
            char = string[-i]
            reverse += char
        final = reverse
        for j in range(len(reverse)):
            if reverse[j] == "0":
                final = reverse[j+1:]
            else:
                break
        if neg == 1:
            final = "-" + final
        if int(final) >= 2**31-1 or int(final) <= (-2**31):
            return 0
        return final