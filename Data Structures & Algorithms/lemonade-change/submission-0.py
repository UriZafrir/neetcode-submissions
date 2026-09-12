class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bills = 0
        ten_bills = 0
        
        for i in bills:
            if i == 5:
                five_bills += 1
            elif i == 10:  # Changed to elif for cleaner execution flow
                if five_bills >= 1:
                    five_bills -= 1
                    ten_bills += 1
                else:
                    return False
            elif i == 20:  # Changed to elif to safely handle the fallback logic
                if ten_bills >= 1 and five_bills >= 1:
                    ten_bills -= 1
                    five_bills -= 1
                elif five_bills >= 3:  # Simplified by removing the redundant check
                    five_bills -= 3
                else:
                    return False
                    
        return True  # Crucial fix: returns True if all customers are served