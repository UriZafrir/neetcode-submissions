class Solution:
    def countBits(self, n: int) -> List[int]:
        answer=[]
        def ones_in_number(m: int) -> int:
            count=0
            while m > 0:
                if m % 2 == 1:
                    count+=1
                m = m // 2
            return count
        for i in range(n+1):
            answer.append(ones_in_number(i))
        return answer
