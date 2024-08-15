'''
https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15
860. Lemonade Change
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = {5: 0, 10: 0}
        for i in bills:
            if i == 5:
                wallet[5] += 1  
            elif i == 10:
                if wallet[5] > 0:
                    wallet[5] -= 1  
                    wallet[10] += 1  
                else:
                    return False  
            elif i == 20:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1  
                    wallet[5] -= 1   
                elif wallet[5] >= 3:
                    wallet[5] -= 3  
                else:
                    return False  

        return True  

