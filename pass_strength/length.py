
def lengt_str(pwd):
    length=len(pwd)
    if length>=14:
        score=20
    if length<14 and length>=7:
        score=15
    if length<7 and length>4:
        score=10
    if length<=4 and length>0:
        score=5
    if length==0:
        score=0    
    return score
