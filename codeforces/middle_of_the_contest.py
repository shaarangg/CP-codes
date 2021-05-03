h1,m1 = map(int, input().split(":"))
h2,m2 = map(int, input().split(":"))
t1 = h1*60 + m1
t2 = h2*60 + m2
t = (t2-t1)//2
m1+=t
h1+=(m1//60)%23
m1=m1%60
if(h1<10):
    h1='0'+str(h1)
if(m1<10):
    m1='0'+str(m1)
print("{}:{}".format(h1,m1))