'''
https://leetcode.com/problems/get-the-size-of-a-dataframe/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
2878. Get the Size of a DataFrame
'''
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    a=[players.shape[0], players.shape[1]]
    return a
    
