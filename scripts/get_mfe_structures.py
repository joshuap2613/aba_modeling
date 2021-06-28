import sys
sys.path.insert(0, "/u/prupes/ViennaRNA/lib/python2.7/site-packages")
import RNA
import pandas as pd
import h5py


def parse_data(filepath):
    f = h5py.File(filepath,'r')
    a_group_key = list(f.keys())[0]
    dset = f[a_group_key]
    data = dset[:]
    df = pd.DataFrame(data)
    df.sequence = df.sequence.str.decode('utf-8')
    return df



if len(sys.argv) == 1:
    print("please pass in filepath")
    sys.exit()

filepath= sys.argv[1]
df = parse_data(filepath)
print(df.head())


structures = []
mfes = []
for elt in df.sequence:
    print(elt)
    elt = elt.replace("T", "U")
    print(elt)
    (ss, mfe) = RNA.fold(str(elt))
    #print(ss)
    mfes.append(mfe)
    structures.append(ss)
df['mfe'] = mfes
df['structure'] = structures

df.to_csv("{}_mfe_structures.csv".format(filepath), index=False)
