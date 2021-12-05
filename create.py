import plotly.express as px
import pandas as pd
import random
import sys
import csv
import os

rand_x = 0
rand_y = 0
point = ''
add_ind = []
x_list = []
y_list = []

loop_amount = int(input("rep"))

def create_points():
    for take in range(0,1000):
      rand_x = random.randint(0,496)
      rand_y = random.randint(0,496)

      x_list.append(rand_x)
      y_list.append(rand_y)
       
      point = str(rand_x)+','+str(rand_y)
      add_ind.append(point)
      
    if os.path.isfile("data.csv") == False:
      data = {
        "x":x_list,
        "y":y_list
      }
      df = pd.DataFrame(data)
      df.to_csv("data.csv", index = False)
    else:
      
      if loop_amount == 1:

        df = pd.read_csv("data.csv")

        os.remove("data.csv")

        data1 = {
            "x":x_list,
            "y":y_list
        }

        df2 = pd.DataFrame(data1)

        df = df.append(df2, ignore_index=True, sort = False)
        df.to_csv("data.csv", index = False)
      elif loop_amount != 1 and loop_amount != 0:
        
        os.remove("data.csv")

        data1 = {
            "x":x_list,
            "y":y_list
        }

        df = pd.DataFrame(data1)
        df.to_csv("data.csv", index = False)


def render():
  fig = px.scatter(x=x_list, y=y_list)
  fig.show()
  x_list.clear()
  y_list.clear()



def final():
    create_points()
    render()

for i in range(0,loop_amount):
    cont = input("continue?")

    if cont.lower() == "y":
        final()
        print("numbers generated")
    elif cont.lower() == "n":
        sys.exit()
    else:
        sys.exit()



