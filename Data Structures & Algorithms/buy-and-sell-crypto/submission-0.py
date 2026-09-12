class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell_price=prices[len(prices)-1]
        current_profit=0
        for i in range(len(prices)-1,0,-1):
            current_buy_price = prices[i-1]
            potential_profit=max_sell_price-current_buy_price
            if potential_profit > current_profit:
                current_profit = potential_profit
            if current_buy_price > max_sell_price:
                max_sell_price = current_buy_price
        return current_profit

"""
let's rethink this




largest=prices[len(prices)-1]
smallest=prices[len(prices)-1]
for i in range(len(prices)-1, 0,-1):
    #compare previous to largest, if it's bigger and it's index number smaller, replace largest.
    if prices[i-1]>largest and prices.index(smallest)<prices.index(prices[i-1]):
        largest=prices[i-1]
    if prices[i-1]<=smallest:
        smallest=prices[i-1]
profit = largest-smallest
if profit > 0:
    return profit
return 0


#we can start off with largest and smallest undefined.
largest=prices[len(prices)-1]
smallest=prices[len(prices)-1]
for i in range(len(prices)-1, 0,-1):
    if prices[i-1]>largest:
        largest=prices[i-1]
    if prices[i-1]<smallest:
        smallest=prices[i-1]
profit = largest-smallest
if profit > 0:
    return profit
return 0

let's rethink
#we can start off with largest and smallest undefined.
largest=None
smallest=None
#compare the last (i-1) to it's previous i-2.
for i in range(len(prices)-1, -1,-1)
    if prices[i-2]>prices[i-1]:
        largest=prices[i-2]
    if prices[i-1]<prices[i-2]:
        smallest=prices[i-1]

#if previous is bigger, largest=previous, smallest = last,  if previous is smaller, i-=1,
compare the largest (previous) to  i, if previous is bigger, largest=previous, if previous is smaller, if previous is smaller than smallest, previous=smallest,


#the largest will initially be the last.
largest=prices[len(prices)-1]
smallest=prices[len(prices)-2]
#need to also remember the smallest so need another loop which remembers that
#for each item starting from the last to the first
for i in (len(i-1), 0,-1)
    #if the previous from the last is bigger than the last,
    if prices[i-2] > prices.index(largest):
        #the largest is the previous one
        largest= prices[i-2]
        
then check if any of it's previous items are smaller
if so, need to pick the smallest of them

prices will be i-1 for the first, but for the second it could be i-1 


for first compare 4 to 5
for second compare 3 to 4
for third compare 2 to 4

so we can assume the largest is the last, then i just goes down
for first compare i-1 and i
for second we compare i-1 and i
for third we compare i-2 and i
"""