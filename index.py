# Raphael Kinoti Mburugu
# kinoti.raphs@gmail.com
# 254 728 668 206
# This is a program to find the row with the maximum spread in the weather.dat file and  print the day of the month and spread to standard output.

import pandas as pd

def controller():
    with open('weather.dat','r') as f:
        next(f) # skip first row
        #Load Data in data frame
        df = pd.DataFrame(l.rstrip().split() for l in f)
        #Remove row with None value
        df = df.ix[1:]
        df = df.replace('\*', '', regex=True)
        #Subtract values and get result
        df["final"] = (df[1].astype(float) - df[2].astype(float))
        #Drop extra columns
        df.drop(df.columns[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]], axis=1, inplace=True)
        #Get max value
        sub_val = df['final'].max()
        #Get row we want
        finalval = df[df['final'] == sub_val]
        #Print output
        print finalval.to_string(index=False, header=None)

if __name__ == '__main__':
    controller()