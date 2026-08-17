import random
def generate():
    password=''
    randed=random.randint(0,9)
    
    randed3=random.choice(['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.','/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_','`', '{', '|', '}', '~'])
    password=password+str(randed)+randed3
    for r in range(3):
        randed1=random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        randed2=random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        password=password+randed1+randed2
    return password
print(generate())
def strength(r):
    count=0
    le=len(r)
    if le>=8:
        count+=1
    if '1' in r or '2' in r or '3' in r or '4' in r or '5' in r or '6' in r or '7' in r or '8' in r or '9' in r:
        count+=1
    has_letter = any(char.isalpha() for char in r)
    if has_letter:
        count+=1
    special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    if any(char in special for char in r):
        count+=1
    #if count==4:
    print(f'password is {25*count}% strong')
strength('7xKhGdL')



 
