import os
import glob
import pandas as pd
os.chdir("C:/Users/MARCELODEOLIVEIRA/Desktop/COB-NOV/receitas")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, error_bad_lines=False, engine= 'python') for f in all_filenames ])
print(all_filenames)
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')