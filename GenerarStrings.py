import string
import random
import pandas as pd
import xlsxwriter
import os

random.seed(1)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    a = ''
    for i in range(stringLength):
        a += random.choice(letters)
    return a.capitalize()

# borramos el fichero xlsx antes si existe
if os.path.exists("demo.xlsx"):
    os.remove("demo.xlsx")

# creamos el dataframe
df = pd.DataFrame(columns=['Name','Age'])


for i in range(10000): # Generamos 10000 registros
    df.loc[i] = (randomString(10), random.randint(1,100)) # Añadimos un registro al DataFrame

# creamos el xlsx
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1', index=True) # Con el index controlamos si escribe la key
# Close the Pandas Excel writer and output the Excel file.
writer.save()



# print ("Random String is ", randomString() )
# print ("Random String is ", randomString(10) )
# print ("Random String is ", randomString(10) )
