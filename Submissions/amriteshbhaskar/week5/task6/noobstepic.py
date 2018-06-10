from PIL import Image
im = Image.open('/home/amritesh/Downloads/universe.png')
pix_val = list(im.getdata())

hi=[]
bin=''
msg=''
for i in range(len(pix_val)):
    for j in range(3):
        hi.append(pix_val[i][j])

for i in range(len(hi)):
    if((i+1)%9 != 0):
        # print(hi[i])
        if(hi[i]%2==0):
            bin+='0'
        else:
            bin+='1'
    elif((i+1)%9 == 0):
        if(hi[i]%2 != 0):
            break

while(bin!=''):
    i=chr(int(bin[:8], 2))
    msg+=i
    bin=bin[8:]

with open('answer', 'wb') as f:
    for i in msg:
        f.write(i)
