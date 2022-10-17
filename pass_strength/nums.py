
def num_str(pwd):
    nums=0
    nums+=pwd.count("1")
    nums+=pwd.count("2")
    nums+=pwd.count("3")
    nums+=pwd.count("4")
    nums+=pwd.count("5")
    nums+=pwd.count("6")
    nums+=pwd.count("7")
    nums+=pwd.count("8")
    nums+=pwd.count("9")
    nums+=pwd.count("0")

    if nums>4:
        num_score=20
    if nums<=4 and nums>2:
        num_score=15
    if nums>=2 and nums>0:
        num_score=10
    if nums==0:
        num_score=0



    return num_score