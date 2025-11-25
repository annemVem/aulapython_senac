import pandas as pd
#criar lista de dados
dados =[10, 20, 30, 40]
#criar série
serie = pd.Series (dados, index=['A','B', 'C', 'D'])
print(serie)