class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = _standardize(s)
        s = s.lower()
        l = 0
        r = len(s)-1;

        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

def _standardize(s: str) -> str:
        s = s.replace(" ", "")
        s = s.replace("!", "")
        s = s.replace("?", "")
        s = s.replace("@", "")
        s = s.replace("#", "")
        s = s.replace("$", "")
        s = s.replace("%", "")
        s = s.replace("^", "")
        s = s.replace("&", "")
        s = s.replace("*", "")
        s = s.replace("(", "")
        s = s.replace(")", "")
        s = s.replace("-", "")
        s = s.replace("_", "")
        s = s.replace("=", "")
        s = s.replace("+", "")
        s = s.replace("/", "")
        s = s.replace(".", "")
        s = s.replace(",", "")
        s = s.replace("<", "")
        s = s.replace(">", "")
        s = s.replace("\\", "")
        s = s.replace("|", "")
        s = s.replace("]", "")
        s = s.replace("[", "")
        s = s.replace("}", "")
        s = s.replace("{", "")
        s = s.replace(";", "")
        s = s.replace(":", "")
        s = s.replace("/", "")
        s = s.replace("`", "")
        s = s.replace("~", "")
        s = s.replace("'", "")
        s = s.replace(" ", "")
        s = s.lower()

        return s
        

        