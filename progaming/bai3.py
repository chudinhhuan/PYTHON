
s='aaabbb'

# kiem tra xem neu nhu a lien nhau thi tra ve True con khong thi tra ve False
# vd: s= 'aaaabbb' -> True
# con s='aaabaaa' -> False
def problem_2(s):
    if len(s) == 1:
        return True
    # len(s) > 1
    new_s = s[0:len(s)-1]
    if problem_2(new_s) == False:
        return False
    if problem_2(new_s) == True:
        last_value = new_s[-1]
        if last_value == 'a':
            return True
        if last_value == 'b':
            if s[-1] == 'b':
             return True
            else:
                return False
print(problem_2(s))