"""
Input:  
   buyer_name  close_date seller_name  transaction_id
0      Julia  2012-08-01        Lara               1
1        Joe  2012-08-02       Julia               2
2       Jake  2012-08-03     Barbara               3
3      Jamie  2012-08-04       Emily               4
4     Jackie  2012-08-04       Mason               5

	transaction_id_x	close_date_x	buyer_name_x	seller_name_x	transaction_id_y	close_date_y	buyer_name_y	seller_name_y
0	          1	        2012-08-01	Julia	              Lara	      2	              2012-08-02	    Joe	        Julia

"""

import pandas as pd

data = {'transaction_id': [1, 2, 3, 4, 5], 
        'close_date': ["2012-08-01", "2012-08-02", "2012-08-03", "2012-08-04", "2012-08-04"], 
        'buyer_name': ["Julia", "Joe", "Jake", "Jamie", "Jackie"],
       'seller_name': ["Lara", "Julia", "Barbara", "Emily", "Mason"]
       }
df = pd.DataFrame(data)
print(df)

df2 = df.merge(right=df, left_on='buyer_name', right_on='seller_name')
print(df2)
