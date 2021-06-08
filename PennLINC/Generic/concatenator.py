#!/usr/bin/env python

# concatenator for audit 
import pandas as pd 
from pathlib import Path 
import numpy as np 
import subprocess

csv_dir = '/cbica/projects/RBC/production/PNC/fmriprep-audit/merge_ds/csvs/'

columns = ["SubjectID", "HasOutput", "HasHTML", "NoErrorsToReport", "HasFuncDir", "HasBold", "ProducedFuncDir", "RanSurfBold", "RanVolBold", "HasErrorFile", "RuntimeErrorDescription", "OSErrorDescription", "CommandErrorDescription", "HadScratchSpace", "HadRAMSpace", "HadDiskSpace", "FinishedSuccessfully"]

df = pd.DataFrame(np.nan, index=range(0,1), columns=columns, dtype="string")

for csv_path in Path(csv_dir).rglob('*.csv'):
    #subprocess.run(['datalad', 'get', csv_path])
    sub_df = pd.read_csv(str(csv_path))
    df = pd.concat([df, sub_df])

df.to_csv('/cbica/projects/RBC/Curation/RBC/PennLINC/PNC_BIDS_Fix/PNC_CSVs/00_Ordered/mount/PNC_BOOTSTRAP_AUDIT_2.csv', index=False)
                    
# THEN RUN THIS THROUGH THE SUMMARY REPORT SCRIPTS! 
