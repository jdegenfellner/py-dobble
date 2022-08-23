# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
import openpyxl
import pandas as pd
import random

# create new cards with dobble-algo.py

# reading game matrix
wb_obj = openpyxl.load_workbook('Cards_Symbols.xlsx')
sheet = wb_obj.active
df = pd.DataFrame(sheet.values)
df = df.fillna(0)
df = df.set_index(0)
df = df.iloc[1:, :]

# checking
#df.head(10)
# row names
#list(df.index.values.tolist())
# col names
#for col in df.columns:
#   print(col)


# update...Pseudo-code for game:

# Set counter player 1 and player 2 = 0
# while counter < number of rounds played:
# do:
# 1) Draw 2 distinct columns from columns of df
# 2) Show them either
# done---a) in console with "symbols.." or
# b) visually, beautifully with Dobble-pictures.
#    - define 57 symbols
#    - choose 2 random columns
#    - resize symbols on each card randomly
#    - put them equidistantly (approximately) on each card
#    - show cards next to each other

count_player_1 = 0
count_player_2 = 0

i = 1
while i < 6:
    i += 1
    random_cols = random.sample(range(1, 58), 2)  # draw random columns
    two_cards = df[random_cols]  # choose cards
    two_cards.columns = ['card1', 'card2']
    card1 = two_cards.loc[:, ['card1']]
    card1 = card1.loc[two_cards['card1'] == 1]
    card2 = two_cards.loc[:, ['card2']]
    card2 = card2.loc[two_cards['card2'] == 1]

    symbols_card1 = card1.index.values.tolist()
    symbols_card2 = card2.index.values.tolist()

    random.shuffle(symbols_card1)
    random.shuffle(symbols_card2)

    print(symbols_card1)
    print(symbols_card2)
    name = input('Which player was faster?\n')
    if name == "k":
        count_player_1 += 1
    elif name == "j":
        count_player_2 += 1
    if i == 6:
        break

print("player 1 = " + repr(count_player_1))
print("player 2 = " + repr(count_player_2))
if count_player_1 > count_player_2:
    print("Result: Player 1 is the winner")
elif count_player_2 > count_player_1:
    print("Result: Player 2 is the winner")
else:
    print("Result: draw")

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()