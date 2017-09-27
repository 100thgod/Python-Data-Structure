def to_str(n,base):
    convert_string = "0123456789ABCDEF"
    if n <base:
        return convert_string[n]
    else:
        return to_str(n//base , base) + convert_string[n%base]
def reverse(n):
    if len(n) == 1:
        return n
    else:
        return n[-1]+reverse(n[:-1])

def palindrome(n):
    is_palindrome = False
    if len(n) == 1 or len(n) == 0:
        return True
    else:
        is_palindrome=(n[0]==n[-1])
        return is_palindrome and palindrome(n[1:-1])

print(to_str(1453,16))
print(to_str(10,2))
print(reverse("saurabh"))
print(palindrome("SauuaS"))
