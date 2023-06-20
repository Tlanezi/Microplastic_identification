# Program to calculate statistics percentile and export percentiles cvs files in result folder

#Import all libraries
import numpy as np
import pandas as pd
import os
import glob

os.chdir("/Users/nezim/PycharmProjects/percentile_calculator/results_splitter2")
file_extension = '.csv'
all_filenames = [p for p in glob.glob(f"*{file_extension}")]
print(f"These are all of the filenames ending in .csv {all_filenames}.")

for l in all_filenames:
    print (l)

    #upload data csv document
    dfi = pd.read_csv(l)
    df = dfi.filter(items=['Label', 'Channel', 'Mean1'], axis=1)

    #name of data frame
    Labels= (df.loc[0, 'Label'])

    #number of R, G, B data
    n = pd.Series(df["Channel"].value_counts())
    k = n.iloc[-1]
    t = 3 #checar si al borrar pasa algo creo no sive para nada
    #extraction of  blue; green, red channel
    for i in range(k+1):
        new_dfB = df[0:i]
        new_dfG = df[k:2*k]
        new_dfR = df[2*k:3*k]
    #print(new_dfR)
    #obtencion de percentiles 10, 50, 90th Blue channel
    blue_percentile_10th = np.percentile(new_dfB.Mean1, 10)
    blue_percentile_50th = np.percentile(new_dfB.Mean1, 50)
    blue_percentile_90th = np.percentile(new_dfB.Mean1, 90)
    blu = [['Blue', Labels, blue_percentile_10th, blue_percentile_50th, blue_percentile_90th]]
    blue = pd.DataFrame(blu)
    blue.columns=["Channel", "Label","percentil 10th", "percentile 50th", "percentile 90th"]

    #obtencion de percentiles 10, 50, 90th Green channel
    green_percentile_10th = np.percentile(new_dfG.Mean1, 10)
    green_percentile_50th = np.percentile(new_dfG.Mean1, 50)
    green_percentile_90th = np.percentile(new_dfG.Mean1, 90)
    gree = [['Green', Labels, green_percentile_10th, green_percentile_50th, green_percentile_90th]]
    green = pd.DataFrame(gree)
    green.columns=["Channel", "Label", "percentil 10th", "percentile 50th", "percentile 90th"]

    #obtencion de percentiles 10, 50, 90th Red channel
    Red_percentile_10th = np.percentile(new_dfR.Mean1, 10)
    Red_percentile_50th = np.percentile(new_dfR.Mean1, 50)
    Red_percentile_90th = np.percentile(new_dfR.Mean1, 90)
    re = [['Red', Labels, Red_percentile_10th, Red_percentile_50th, Red_percentile_90th]]
    red = pd.DataFrame(re)
    red.columns=["Channel", "Label", "percentil 10th", "percentile 50th", "percentile 90th"]
    #saving dta
#naming of output files
    filename1 ='Red_Channel'+ '_' + l
    filename2 = 'Blue_Channel' + '_' + l
    filename3 = 'Green_Channel' + '_' + l
    #exporta tpdps los data frames por ciclo for

    path = 'C:/Users/nezim/PycharmProjects/percentile_calculator/results'
    output_file1 = os.path.join(path, filename1)
    output_file2 = os.path.join(path, filename2)
    output_file3 = os.path.join(path, filename3)
    red.to_csv(output_file1, index=False)
    blue.to_csv(output_file2, index=False)
    green.to_csv(output_file3, index=False)
