'''
https://leetcode.com/problems/display-the-first-three-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
2879. Display the First Three Rows
'''
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return (employees.head(3))
    
