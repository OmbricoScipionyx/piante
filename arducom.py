import serial
import datetime
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://carbonara:guanciale@localhost/plants?charset=utf8")

# initializing the last insert in database variable
last_insert = datetime.datetime.now() - datetime.timedelta(seconds=60)

# saving the port where arduino is connected
ser = serial.Serial('/dev/ttyACM0',9600)

#establishing a connection to database
with engine.connect() as conn:

    while True:

        if (datetime.datetime.now()-last_insert).seconds >= 60:

            # acquiring current date and time
            date = str(datetime.datetime.now())
            date = date.split(".")
            date = date[0]

            #reading data from arduino
            read_serial = ser.readline()
            read_serial = read_serial.decode()
            monstera, bean = read_serial.split()
            monstera = int(monstera)
            bean = int(bean)

            #inserting observations in the database
            conn.execute(text(f"insert into monstera values ('{date}',{monstera});"))
            conn.execute(text(f"insert into bean values('{date}',{bean});"))

            #updating last insert
            last_insert = datetime.datetime.now()
