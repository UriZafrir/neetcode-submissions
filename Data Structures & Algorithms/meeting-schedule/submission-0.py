class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        array=[]
        for j in intervals:
            array.append([j.start,j.end]) 
        array.sort() 
        for i in range(1,len(array)):
            if array[i][0] < array[i-1][1]:    
                return False
        return True
