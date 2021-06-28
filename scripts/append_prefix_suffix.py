import sys
import h5py
import os
import pandas as pd

# Get the current working
# directory (CWD)
cwd = os.getcwd()
print("Current Directory:", cwd)

# Get the directory of
# script
script = os.path.realpath(__file__)
print("SCript path:", script)

def parse_data(filepath):
    f = h5py.File(filepath,'r')
    a_group_key = list(f.keys())[0]
    dset = f[a_group_key]
    data = dset[:]
    df = pd.DataFrame(data)
    df.sequence = df.sequence.str.decode('utf-8')
    return df

df = parse_data(format(sys.argv[1]))
df.sequence = sys.argv[2] + df.sequence + sys.argv[3]
df.to_csv('{}_FULL.csv'.format(sys.argv[1]), index=False)
print(df.head())
