import string as st 
import random as rd 
import os

def gen(min, max):
    chars = st.ascii_letters + st.digits + st.punctuation
    leng = rd.randint(min, max)
    passw = ''.join(rd.choice(chars) for i in range(leng))

    return passw

poss = 94**64 #<- Possibilities

with open('passwords.txt', 'w') as file:
    for i in range(poss):
        passw = gen(8, 64)
        file.write(f'{passw}\n')
        
        size = os.path.getsize(file)
        size_gb = size/(1024 ** 3)
        if size_gb >= 400: #<- File size (Greather than 400GB)
             break

print('Finished process!')