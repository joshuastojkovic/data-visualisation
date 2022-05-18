import pandas as pd
import matplotlib.pyplot as plt



def option_1(choice):

    df = pd.read_csv('data.csv')

    df.plot(kind = 'line', x = 'Date', y = choice)

    plt.show()



def data_selection():

    choice = input("please choose a conversion rate too view, GBP - EUR, EUR - GBP, GBP - AUD, AUD - GBP, GBP - JPY, JPY - GBP: ")
    if choice != int:
        option_1(choice)
    else:
        print('invalid input(make sure there is a space between each side of the hyphen eg: xxx - xxx, try again')


data_selection()
