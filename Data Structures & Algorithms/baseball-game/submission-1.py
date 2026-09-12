class Solution:
    def is_int(self, s: string)->bool:
        try:
            int(s)
            return True
        except ValueError:
            return False
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i in operations:
            if self.is_int(i):
                record.append(int(i))
            elif i == "C":
                record.pop()
            elif i == "D":
                record.append(record[-1]*2)
            elif i == "+":
                record.append(record[-2]+record[-1])
        return sum(record)