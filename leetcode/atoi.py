class Solution(object):
   def myAtoi(self, str):
       n, ind, sign = 0, 0, 1
       if len(str) == 0: return 0
       while ord(str[ind]) == 32: ind += 1
       if str[ind] == "-": sign = -1
       if str[ind] in "-+": ind += 1
       while ind < len(str) and str[ind].isdigit():
           n = n * 10 + (ord(str[ind]) - ord("0")) * sign
           ind += 1
           if sign == 1 and n >= 2147483647: return 2147483647
           elif sign == -1 and n <= -2147483648: return -2147483648
       return n
