# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
import openpyxl
import pandas as pd

wb_obj = openpyxl.load_workbook('Cards_Symbols.xlsx')

# Read the active sheet:
sheet = wb_obj.active
df = pd.DataFrame(sheet.values)
df = df.fillna(0)
df = df.set_index(0)
df = df.iloc[1: , :]

df.head(10)
# row names
list(df.index.values.tolist())
# col names
for col in df.columns:
    print(col)

