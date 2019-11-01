#!/usr/bin/env python
import pandas as pd
import glob

def main():
    filelist=glob.glob('./*filtered.cons')
    with pd.ExcelWriter('merged.xlsx') as writer:
        for filename in sorted(filelist):
            samplename=filename.split('/')[-1].replace('filtered.cons','')
            if len(samplename) > 30:
                samplename=samplename[0:30]
            x=pd.read_csv(filename,delimiter='\t')
            x.to_excel(writer, sheet_name=samplename, index=False)

if __name__=='__main__':
    main()
