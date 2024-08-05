'''
https://leetcode.com/problems/select-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
2880. Select Data
'''

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    #return students.query("student_id==101")[['name', 'age']]
    a= students.loc[students['student_id']==101, ['name', 'age']]
    return a
    
