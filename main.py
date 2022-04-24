import calendar
from datetime import datetime
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
dates=["13.4.2022","14.4.2022","15.4.2022","16.4.2022", "17.4.2022"," 18.4.2022","19.4.2022","20.4.2022","21.4.2022", "22.4.2022"," 23.4.2022"]
nastr=["1","4","3","4", "3", "5","4","5","4", "2", "5"]

root = Tk()
root.title("Запись настроения")
root.geometry("550x250")


def clickedStats():
    n=[]
    logn = open(r"log_nastr.txt")
    for i in logn.readline():
        if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "." or i == "0":
            n.append(i)
    logn.close()
    labels = ["Ужас", "Плохо", "Нормально", "Хорошо", "Отлично"]
    values = [n.count("1"), n.count("2"), n.count("3"), n.count("4"), n.count("5")]
    colors = ["#EB0000", "#FFA500", "#E9FF00", "#0077FF", "#008E43"]
    plt.pie(values, labels=labels, colors=colors)
    plt.title("Статистика")
    plt.axis("equal")
    plt.show()



f = open(r"log_date.txt")
q=[]
for i in f.readline():
    if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="." or i=="0":
        q.append(i)
e = ""

y = 0
for i in range(len(q)):
    e+=q[i]
    y+=1
    if y==9:
        e+=" "
        y = 0
f.close()

def clicked():
    lbl.configure(text=str(selected.get())+"-ка "+"Да?")
    text0 = Label(text="Я понял какое", font="Arial 10")
    text1 = Label(text="у тебя сегодня", font="Arial 10")
    text2 = Label(text="настроение", font="Arial 10")
    text0.grid(column=0, row=4)
    text1.grid(column=1, row=4)
    text2.grid(column=2, row=4)
    lbl.grid(column=3, row=4)
    logd = open("log_date.txt", "w+", encoding="utf-16")
    logn = open("log_nastr.txt", "w+", encoding="utf-16")
    dates.append(date)
    nastr.append(selected.get())
    for i in range(len(dates)):
        logd.write(dates[i]+" ")
        logn.write(str(nastr[i])+" ")
    logd.close()
    logn.close()



def clicked2():
    root.destroy()

def clicked3():

    hist = Tk()
    hist.geometry("550x250")
    w=0
    for i in range(len(dates)):

        lbh0 = Label(hist, text = dates[i])
        lbh1 = Label(hist, text = nastr[i])


        if i < len(nastr)//2:
            lbh0.grid(column=i, row=0)
            lbh1.grid(column=i, row=1)
            m=i
        else:
            lbh0.grid(column=i-m, row=4)
            lbh1.grid(column=i-m, row=5)

    lgh = Label(hist, text="...................", font="Arial 10")
    lbt = Label(hist, text="Где цифры:", font="Arial 10")
    lbt1 = Label(hist, text = "1-Ужас", font="Arial 10")
    lbt2 = Label(hist, text = "2-Плохо", font="Arial 10")
    lbt3 = Label(hist, text = "3-Нормально", font="Arial 10")
    lbt4 = Label(hist, text = "4-Хорошо")
    lbt5 = Label(hist, text = "5-Отлично", font="Arial 10")
    lgh.grid(column=0, row=6)
    lbt.grid(column=0,row=7)
    lbt1.grid(column=1, row=7)
    lbt2.grid(column=2, row=7)
    lbt3.grid(column=3, row=7)
    lbt4.grid(column=4, row=7)
    lbt5.grid(column=5, row=7)


cor_time = datetime.now()
date = ""


date = str(cor_time.day) + "." + str(cor_time.month) + "." + str(cor_time.year)

if date in e:
    txten0 = Label(root, text="Извините, но Вы уже отметили свое настроение. Попробуйте завтра еще раз", font="Arial 10")
    txten1 = Label(root, text="..................................................................................")
    txtenn = Label(root, text="..................................................................................")
    txten2 = Label(root, text="Если Вы хотите, то можете посмотреть на статистику или на историю отметок", font="Arial 10")
    txten3 = Label(root, text="Ну или можете просто выйти из приложения", font="Arial 10")
    btns0 = Button(root, text="Статистика", command=clickedStats, font="Arial 10")
    btns1 = Button(root, text="История", command=clicked3, font="Arial 10")
    btns2 = Button(root, text="Закрыть", command=clicked2, font="Arial 10")
    txten0.grid(column=0, row=0)
    txtenn.grid(column=0, row=1)
    txten2.grid(column=0, row=3)
    txten3.grid(column=0, row=9)
    btns0.grid(column=0, row=6)
    btns1.grid(column=0, row=7)
    txten1.grid(column=0, row=8)
    btns2.grid(column=0, row=10)



else:
    lgh = Label(root, text="...................")
    lblto = Label(root, text="Сегодня", font="Arial 10")
    lblday = Label(root, text=date)
    lblto.grid(column=0, row=0)
    lblday.grid(column=1,row=0)

    lblo = Label(root, text = "Оцени ", font="Arial 10")
    lblc = Label(root, text = "свое ", font="Arial 10")
    lbln = Label(root, text = "настрение: ", font="Arial 10")


    lblo.grid(column=0, row= 2)
    lblc.grid(column=1, row=2)
    lbln.grid(column=2, row=2)


    selected = IntVar()
    rad1 = Radiobutton(root, text='Ужас', value=1, variable=selected, command=clicked, font="Arial 10")
    rad2 = Radiobutton(root, text='Плохо', value=2, variable=selected, command=clicked, font="Arial 10")
    rad3 = Radiobutton(root, text='Нормально', value=3, variable=selected, command=clicked, font="Arial 10")
    rad4 = Radiobutton(root, text='Хорошо', value=4, variable=selected, command=clicked, font="Arial 10")
    rad5 = Radiobutton(root, text='Отлично', value=5, variable=selected, command=clicked, font="Arial 10")
    btn = Button(root, text = "Закрыть", command=clicked2, font="Arial 10")
    lbl = Label(root)
    rad1.grid(column=0, row=3)
    rad2.grid(column=1, row=3)
    rad3.grid(column=2, row=3)
    rad4.grid(column=3, row=3)
    rad5.grid(column=4, row=3)
    btn.grid(column=4, row=4)
    vb=Label(root,text="У меня", font="Arial 10")
    vb1=Label(root, text="и история", font="Arial 10")
    vb2=Label(root, text="отметок", font="Arial 10")
    vb3=Label(root, text="есть", font="Arial 10")
    btvb=Button(root, text="История", command=clicked3, font="Arial 10")
    txt0 = Label(root, text="Что ж,", font="Arial 10")
    txt1 = Label(root, text="я готов", font="Arial 10")
    txt2 = Label(root, text="сообщить", font="Arial 10")
    txt3 = Label(root, text="результаты", font="Arial 10")
    txt4 = Label(root, text="Нажли сюда", font="Arial 10")
    btn_ne = Button(root, text="Статистика", command=clickedStats, font="Arial 10")
    lgh.grid(column=0, row=5)
    txt0.grid(column=0, row=6)
    txt1.grid(column=1, row=6)
    txt2.grid(column=2, row=6)
    txt3.grid(column=3, row=6)
    btn_ne.grid(column=4, row=6)
    vb.grid(column=0, row=7)
    vb1.grid(column=1, row=7)
    vb2.grid(column=2, row=7)
    vb3.grid(column=3, row=7)
    btvb.grid(column=4, row=7)

root.mainloop()

