#Create captcha : combination of letters and digits
import string as s
import random as r
st1= s.ascii_lowercase + s.ascii_uppercase+s.digits
print("print lowercase and uppercase and digits:",st1)#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
str2=""
for i in range(0,5,1): #(start,stop,step) (0,1,2,3,4)
    i= r.randrange(0,63)#here our st1 length is 62 so index is always -1
    str2=str2+st1[i]
print("capcha is:",str2)#TOufe
