from tkinter import *
from tkinter import ttk
import tkinter
import requests
import json

def get_data_currency():
    data_currency = requests.get('https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_KnzU7VUioFndgDLhbOFBeSQmcl2rWXgSa90m10Qv').json()
    # print(data_currency['data'])
    list_of_currency = {key:value for (key,value) in data_currency['data'].items()}
    return list(list_of_currency),data_currency['data']


def convert():
    quantity=float(InputQuantity.get())
    data_currency = get_data_currency()[1]
    key_currency = CurrencyComboBox_for_convert.get()
    currency = list({value for (key,value) in data_currency.items() if key == key_currency})
    result = quantity / currency[0]
    ResultLabel.config(text=f"{quantity} {key_currency} equal $ {round(result,2)}")

root = Tk()
root.title("Currency Convert")
root.minsize(400,350)
root.maxsize(600,700)

CurrencyComboBox_label_1 = Label(text='Currency').place(x=170,y=30)
CurrencyComboBox_for_convert = ttk.Combobox(values = get_data_currency()[0])
CurrencyComboBox_for_convert.place(x=100,y=50)

CurrencyComboBox_label_2 = Label(root,text='USD').place(x=170,y=90)
CurrencyComboBox_for_currency = ttk.Combobox(values = 'USD').place(x=100,y=115)

CurrencyLabelInput = Label(root,text = "Enter quatity").place(x=170,y=160)
InputQuantity = Entry(root)
InputQuantity.place(x=110,y=190)

ButtonConvert = Button(root,text='Convert',command=convert).place(x=160,y=240)
ResultLabel = Label(root,text = '')
ResultLabel.place(x=140,y=280)





root.mainloop()