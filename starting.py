__author__ = 'nuna'
import pandas as pd
import numpy as np
from generate_company_config import *
from util.convenience import slurpify, decrypt
from util.phi_enforcer import is_aes_encrypted
from PHICleaner import readers
import os
def stream_to_df(company, file):
        try:
            config = generate_company_config(company)
        except:
           print "not a company"
        if os.path.isfile(file):
            df = slurpify(readers.encrypted_streaming_reader(file, config))
        else:
            print "file not found"
        try:
            for i in df.columns:
                if i.startswith('hashed'):
                    pass
                else:
                    if is_aes_encrypted(df[i]):
                        df[i] = df[i].apply(lambda x: decrypt(x, config))
                    else:
                        pass
            return df
        except:
            print "failed to decrypt"

class CleanerMedical:
    def __init__(self, company, file):
        self.company = company
        self.file = file
        self.dataframe = stream_to_df(company, file)








def to_string(f):
    str(f)
