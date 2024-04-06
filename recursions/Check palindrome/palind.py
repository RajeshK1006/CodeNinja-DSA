def isPalindrome(string: str) -> bool:
    if len(string)<=1:
        return True
    if string[0]==string[-1]:
        return isPalindrome(string[1:-1])
    return False

# def palin(t):
#     if t==t[::-1]:
#         return True
#     else:
#         return False
#   def palin(t,,result=[]):
