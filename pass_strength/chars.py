def char_str(pwd):
    chars=0
    chars+=pwd.count("`")
    chars+=pwd.count("~")
    chars+=pwd.count("!")
    chars+=pwd.count("@")
    chars+=pwd.count("#")
    chars+=pwd.count("$")
    chars+=pwd.count("%")
    chars+=pwd.count("^")
    chars+=pwd.count("&")
    chars+=pwd.count("*")
    chars+=pwd.count("(")
    chars+=pwd.count(")")
    chars+=pwd.count("_")
    chars+=pwd.count("-")
    chars+=pwd.count("+")
    chars+=pwd.count("=")
    chars+=pwd.count("\\")
    chars+=pwd.count("|")
    chars+=pwd.count("}")
    chars+=pwd.count("]")
    chars+=pwd.count("{")
    chars+=pwd.count("[")
    chars+=pwd.count('"')
    chars+=pwd.count("'")
    chars+=pwd.count(":")
    chars+=pwd.count(";")
    chars+=pwd.count("?")
    chars+=pwd.count("/")
    chars+=pwd.count(">")
    chars+=pwd.count(".")
    chars+=pwd.count("<")
    chars+=pwd.count(",")


    if chars>4:
        char_score=20
    if chars<=4 and chars>2:
        char_score=15
    if chars<=2 and chars>0:
        char_score=10
    if chars==0:
        char_score=0



    return char_score

