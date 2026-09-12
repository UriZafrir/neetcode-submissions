import "slices"
func buyChoco(prices []int, money int) int {
	slices.Sort(prices)
	totalCost := prices[0]+prices[1]
	if totalCost > money {
		return money
	}
	return money-totalCost
}

/*
need to pick smallest numbers
prices.sort()
total_cost=prices[0]+prices[1]
if total_cost > money:
	return money
if total_cost <= money:
	result=money-total_cost
	return result
*/