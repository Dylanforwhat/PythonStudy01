import pandas as pd
import numpy as np
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a = pd.DataFrame(arr,columns = list('xyz'),index = list('123'))
print(a)