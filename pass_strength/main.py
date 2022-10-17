import random
import common_passwords as cp
import chars as chr
import nums as ns
import length as ln
password=input("Enter your password ")
score=0 #password strength score


#defining strength based on length
score+=ln.lengt_str(password)


#defining score on numbers
score+=ns.num_str(password)


#defining score on characters
score+=chr.char_str(password)








#defining score on common passwords
if password in cp.common_passwords:
    print("This Is a Very Common Password , Please Change it!!")
else:
    if score>=30:
        print("Strong password!")
    if score<30 and score>=20:
        print("Could be better")
    if score<20 and score>10:
        print("Weak password!")
    if score<=10:   
        print("Risky!!")

