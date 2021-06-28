import sys
sys.path.insert(0, "/u/prupes/ViennaRNA/lib/python2.7/site-packages")
import RNA
import pandas as pd
import h5py




if len(sys.argv) == 1:
    print("please pass in filepath")
    sys.exit()

filepath= sys.argv[1]
df = pd.read_csv(filepath)
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
