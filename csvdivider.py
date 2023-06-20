# Program to separate csv into diff csv

#Import all libraries
import numpy as np
import pandas as pd
import os
import glob

os.chdir("/Users/nezim/PycharmProjects/percentile_calculator/archivos_2")
file_extension = '.csv'
all_filenames = [p for p in glob.glob(f"*{file_extension}")]
print(f"These are all of the filenames ending in .csv {all_filenames}.")

for l in all_filenames:
    print(l)

    dfk = pd.read_csv(l)

    # upload data csv document
#number of  data
    cou = dfk.shape[0]
    print(cou)
    headers = dfk.keys()
    #print(headers)
    # get the number of lines of the csv file to be read
    number_lines = cou

    # size of rows of data to write to the csv,
    # you can change the row size according to your need
    rowsize =6

    # start looping through data writing it to a new file for each set
    co = 0
    for i in range(1, number_lines, rowsize):

        dfr = pd.read_csv(l, header=None,nrows=rowsize, skiprows=i)  # skip rows that have been read

        dfr.columns = headers
        filename3 = str(i) + '_' + l
     #exporta tpdps los data frames por ciclo for

        path = 'C:/Users/nezim/PycharmProjects/percentile_calculator/results_splitter2'

        output_file3 = os.path.join(path, filename3)
        dfr.to_csv(output_file3, index=False, mode='a', chunksize=rowsize)