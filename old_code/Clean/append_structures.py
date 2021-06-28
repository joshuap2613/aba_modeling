import pandas as pd
import RNA

ENERGIES_PATH = "../subopt_attributes4.csv"
energies = pd.read_csv(ENERGIES_PATH)

structs = []
sequence = energies.Sequence.str.slice(29, -32).str.replace("U", "T")
for seq in list(sequence):
    seq = seq.replace("T","U")
    ss, mfe = RNA.fold(seq)
    structs.append(ss)
energies['structure'] = structs

energies.to_csv("subopt_attributes4_with_structure.csv", index=False)
