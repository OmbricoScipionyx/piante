from sqlalchemy import create_engine, text
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


engine = create_engine("mysql+pymysql://carbonara:guanciale@192.168.1.41/plants?charset=utf8")


#defining a function which returns a moving average
def moving_average(period, list):

    mean = []
    i = 0

    while i < len(list) - period + 1:
        per = list[i : i + period]
        avg = round(sum(per)/period, 2)
        mean.append(avg)

        i += 1

    return mean

def generate_images():

    #initializing variables
    xm = []
    ym = []
    xb = []
    yb = []

    #establishing a connection to database
    with engine.connect() as conn:

        #selecting data from database
        monstera = conn.execute(text(f"select * from monstera;"))
        bean = conn.execute(text(f"select * from bean;"))

        #creating lists for x and y axes and converting to local time
        for row in monstera:
            xm.append(row[0] + datetime.timedelta(hours = 2))
            ym.append(-1*row[1])

        for row in bean:
            xb.append(row[0] + datetime.timedelta(hours = 2))
            yb.append(-1*row[1])

    plt.figure(figsize=(13, 3))
    plt.title('monstera')
    #plottig the data
    plt.plot(xm, ym, linestyle='-')
    #plotting a moving average
    plt.plot(xm[19:len(xm)], moving_average(20, ym))

    plt.savefig('static/monstera.png')


    plt.figure(figsize=(13, 3))
    plt.title("Bean")
    #plottig the data
    plt.plot(xb, yb, linestyle='-')
    #plotting a moving average
    plt.plot(xb[19:len(xb)], moving_average(20, yb))

    plt.savefig('static/bean.png')


    return ["monstera.png", "bean.png"]
