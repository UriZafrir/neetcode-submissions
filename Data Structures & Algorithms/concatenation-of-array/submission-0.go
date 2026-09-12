func getConcatenation(nums []int) []int {
    ans := nums
    for _, i := range nums {
        ans = append(ans, i)
    }
    return ans
}