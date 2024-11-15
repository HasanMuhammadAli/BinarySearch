import math
def minimumRateToEatBananas(piles,h):
    l,r=1,max(piles)
    # here we set l and r 
    res=r
    while l <= r:
        k=(l+r)//2
        # k is the rate of eating bananas
        hours=0
        for p in piles:
            hours += math.ceil(p/k)
            # we get hours by dividing number of bananas and speed of eating bananas
        if hours <= h:
            res = min(res,k)
            r=k-1
        else:
            l=k+1
    return res

piles = [30,11,23,4,20] 
h = 5
answer = minimumRateToEatBananas(piles , h)
print(answer)