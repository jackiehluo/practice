class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry == 10:
                digits[i], carry = 0, 1
            else:
                digits[i] += carry
                carry = 0
        if carry == 1: digits.insert(0, 1)
        return digits