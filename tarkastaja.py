def testaa(syote):
    if len(syote) < 5:
        return False
    if syote.isalpha()==True:
        return False
    elif syote.isdigit()==True:
        return False 
    else:
        return True