# importing libraries
import pandas as pd
import glob
import os

os.chdir("/Users/nezim/PycharmProjects/percentile_calculator/results")
file_extension = '.csv'
all_results = [p for p in glob.glob(f"*{file_extension}")]
print(f"These are all of the filenames ending in .csv {all_results}.")

# Finally, the files are joined
dataset = pd.concat(map(pd.read_csv, all_results), ignore_index=True)
print(dataset)

#Exporting data set
filename ='data_set_percentiles'+ '.csv'
path = 'C:/Users/nezim/PycharmProjects/percentile_calculator/percentile_results'
output_file1 = os.path.join(path, filename)
dataset.to_csv(output_file1, index=False)