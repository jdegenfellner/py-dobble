# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
import openpyxl
import pandas as pd

wb_obj = openpyxl.load_workbook('Cards_Symbols.xlsx')

# Read the active sheet:
sheet = wb_obj.active
data_df = pd.DataFrame(sheet.values)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
