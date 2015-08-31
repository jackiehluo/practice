class Solution(object):
    def isNumber(self, s):
        if re.compile('^[-+]?(\d+\.?\d*|\.\d+)([Ee][+-]?\d+)?$').match(s.strip()): return True
        else: return False