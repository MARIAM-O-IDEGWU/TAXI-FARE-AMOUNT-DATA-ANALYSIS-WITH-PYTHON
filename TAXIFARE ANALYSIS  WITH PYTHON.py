import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Ensure you add your url were you have your csv files

def passengerrecurrence():
     nap = pd.read_csv(r'C:/Users/PyCharmCE2018.2/config/scratches/train.csv')
     nap.dropna(inplace=True)
     nap.drop(nap[nap['passenger_count'] == 208].index, axis=0, inplace=True)
     nap.drop(nap[nap['passenger_count'] > 5].index, axis=0, inplace=True)
     nap = nap.loc[nap['passenger_count']]
     fig, ax = plt.subplots()
     mycount = nap.passenger_count.value_counts()
     mycount.plot(kind='barh', ax=ax)
     ax.set_title('Category distribution of passenger_count')
     ax.set_ylabel('Recurrence of a Passenger')
     plt.show()

def category():
    df = pd.read_csv(r'C:/Users/PyCharmCE2018.2/config/scratches/train.csv')
    df.dropna(inplace=True)
    df = df.loc[df['passenger_count'] <= 5]
    totals = df.groupby("passenger_count")["passenger_count"].sum().sort_values()
    totals.plot(kind="pie", fontsize=4)
    plt.show()


def LinearReg():#add your path or url were you have your csv file
 df = pd.read_csv (r'C:/Users/PyCharmCE2018.2/config/scratches/train.csv')
 dftest = pd.read_csv (r'C:/Users/PyCharmCE2018.2/config/scratches/test.csv')
 dfsub = pd.read_csv(r'C:/Users/PyCharmCE2018.2/config/scratches/sample_submission.csv')
 df.dropna(inplace=True)
 dftest.dropna(inplace=True)
 dfsub.dropna(inplace=True)
 obj = LinearRegression()

 obj.fit(X=df[['pickup_longitude' , 'pickup_latitude' , 'dropoff_longitude' , 'dropoff_latitude','passenger_count' ]],
        y= df['fare_amount'])

 fieldsdata = ['pickup_longitude' , 'pickup_latitude' , 'dropoff_longitude' , 'dropoff_latitude','passenger_count' ]

 dftest['fare_amount'] = obj.predict(dftest[fieldsdata])
 nap = dfsub[['key','fare_amount']]

 submit= dftest[['key','fare_amount']]
 submit.to_csv('Result.csv' , index=False)
 submit.plot(x=["key"], y=["fare_amount"])
 plt.show()


#test. CSV

def predict_file():
 df = pd.read_csv (r'C:/Users/Mariam Idegwu/.PyCharmCE2018.2/config/scratches/test.csv')
 df.dropna(inplace=True)#droping empty values
 df = df.loc[df['pickup_latitude'].between(40, 42)]
 df = df.loc[df['pickup_longitude'].between(-75, -72)]
 df = df.loc[df['dropoff_latitude'].between(40, 42)]
 df = df.loc[df['dropoff_longitude'].between(-75, -72)]
 df.plot(x="dropoff_longitude", y="dropoff_latitude", kind="scatter")
 df.plot(x="pickup_longitude", y="pickup_latitude", kind="scatter")
 plt.show()


def testcategory():
     df = pd.read_csv(r'C:/Users/PyCharmCE2018.2/config/scratches/test.csv')
     df.dropna(inplace=True)
     df = df.loc[df['passenger_count'] <= 4]
     totals = df.groupby("passenger_count")["passenger_count"].sum().sort_values()
     totals.plot(kind="pie", fontsize=4)
     plt.show()

#sample_submission CSV

def KeyAmount():
    df = pd.read_csv(r'C:/Users/PyCharmCE2018.2/config/scratches/sample_submission.csv')
    df.dropna(inplace=True)
    df.plot(x=["key"], y=["fare_amount"])
    plt.show()

def Fare():
    df = pd.read_csv(r'C:/Users/PyCharmCE2018.2/config/scratches/sample_submission.csv')
    df.dropna(inplace=True)
    df.fare_amount.hist(bins=30, alpha=0.5)
    plt.show()


root = tk.Tk()
root.geometry("600x600+700+100")
root.configure(bg='grey')
root.title('TAXI-FARE-AMOUNT DATA ANALYSIS WITH PYTHON')

label_0 =tk.Label(root, text="TAXI FARE AMOUNT DATA ANALYSIS",fg='green', font=('broadway 20 bold'))
label_0.place(x=0, y=0)
label_05 =tk.Label(root, text="TRAIN.CSV ANALYSIS",fg='green', font=('broadway 20 bold'))
label_05.place(x=0, y=89)
label_2 = tk.Label(root, text="Passenger Recurrence:", anchor="w",width=20, font=('bold', 11))
label_2.place(x=9, y=140)
label_3 = tk.Label(root, text="Categories of Passengers:", anchor="w",width=20, font=('bold', 11))
label_3.place(x=9, y=170)
label_4 = tk.Label(root, text="Regression Process:", anchor="w",width=20, font=('bold', 11))
label_4.place(x=9, y=200)

#Analysis for Test.csv
label_005 =tk.Label(root, text="TEST.CSV ANALYSIS",fg='green', font=('broadway 20 bold'))
label_005.place(x=0, y=290)
label_1 =tk.Label(root, text="Pick-Up and Drop-Off Periods:", width=25,anchor="w",font=('bold', 10))
label_1. place(x=9, y=340)
label_2 = tk.Label(root, text="Passenger Category:", anchor="w",width=20, font=('bold', 11))
label_2.place(x=9, y=368)

#Analysis for Sample_Submission.csv
label_sub =tk.Label(root, text="SAMPLE_SUBMISSION.CSV ANALYSIS",fg='green', font=('broadway 20 bold'))
label_sub.place(x=0, y=420)
label_sam =tk.Label(root, text="Key and FareAmount:", width=25,anchor="w",font=('bold', 10))
label_sam. place(x=9, y=469)
label_NUT = tk.Label(root, text="FareAmount:", anchor="w",width=20, font=('bold', 11))
label_NUT.place(x=9, y=495)

#Buttons for Train.CSV
button1 = tk.Button(root, text="Show Graph",width=20, height=1, bg='green', fg='white',command= passengerrecurrence)
button2 = tk.Button(root, text="Show Graph",width=20, height=1, bg='green', fg='white',command= category)
button3 = tk.Button(root, text="Show Graph",width=20, height=1, bg='green', fg='white',command= LinearReg)


button1.place(x=200, y=140)
button2.place(x=200, y=170)
button3.place(x=200, y=200)


#Buttons for Test.CSV
buttontest = tk.Button(root, text="Show Graph",width=20, height=1, bg='green', fg='white',command=predict_file)
button1test = tk.Button(root, text="Show Graph",width=20, height=1, bg='green', fg='white',command= testcategory)
buttontest.place(x=200, y=340)
button1test.place(x=200, y=368)

#Buttons for SAMPLE SUBMISSION.CSV
buttontSUB = tk.Button(root, text="Show Graph",width=20, height=1, bg='green', fg='white',command=KeyAmount)
button1SAM = tk.Button(root, text="Show Graph",width=20, height=1, bg='green', fg='white',command= Fare)
buttontSUB.place(x=200, y=469)
button1SAM.place(x=200, y=495)



root.mainloop()