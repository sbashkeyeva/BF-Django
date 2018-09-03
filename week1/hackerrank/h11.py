
def swap_case(s):
    str=""
    for i in s:
        if i.isupper():
            str+=(i.lower())
        else:
            str+=(i.upper())
    return str

