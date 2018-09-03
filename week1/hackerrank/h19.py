# Complete the solve function below.
#titlesub = re.compile(r'\b[a-zA-Z]').sub  # Precompile regex and prebind method for efficiency
#def solve(s):
#    return titlesub(lambda x: x.group(0).upper(), s)
#print(' '.join((word.capitalize() for word in s.split(' ')))
#' '.join(i.capitalize() for i in string.split(' '))
def solve(s):
    #string1=s.split()
    #return ' '.join(w.capitalize for w in string1)
    return ' '.join(map(str.capitalize,s.split(' ')))