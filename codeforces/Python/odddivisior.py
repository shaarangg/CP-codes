'''If the number x has an odd divisor, then it has an odd prime divisor. To understand this fact, 
we can consider what happens when multiplying even and odd numbers:

even ∗ even = even;
even ∗ odd = even;
odd ∗ even = even;
odd ∗ odd = odd.

There is only one even prime number — 2. So, if a number has no odd divisors, then it must be a power of two.
To check this fact, for example, you can divide n by 2 as long as it is divisible. If at the end we got 1, then n — the power of two.

Bonus: You can also use the following condition to check:
n&(n−1)=0
If the number — is a power of two, then it contains only one unit in the binary notation. 
Then (n−1) contains units in all positions except the one in which the unit in n is located. So their bitwise "AND" does not contain units.
'''
import math
t = int(input())
res=[]
for i in range(t):
    n = int(input())
    if((n & n-1)==0):
        res.append("NO")
    else:
        res.append("YES")
for i in res:
    print(i)