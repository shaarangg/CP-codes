n = int(input())
a = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
b = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
if(n<20):
    print(a[n])
else:
    t = n//10
    u = n%10
    if(u==0):
        print(b[t])
    else:
        print("{}-{}".format(b[t],a[u]))