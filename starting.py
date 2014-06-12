__author__ = 'nuna'
import pandas as pd
import numpy as np
from generate_company_config import *
from util.convenience import slurpify, decrypt
from util.phi_enforcer import is_aes_encrypted
from PHICleaner import readers
import os

def decrypt_with_unique_id(company, path):
        try:
            config = generate_company_config(company)
        except:
           print "not a company"
        if os.path.isfile(path):
            df = slurpify(readers.encrypted_streaming_reader(path, config))
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

            df['unique_identifier'] = df.ssn.map(str) + '_' + df.date_of_birth.map(str) + '_' + df.first_name

            return df

        except:
            print "failed to decrypt"

class EnrollmentCleaner:
    def __init__(self, company, file):
        self.company = company
        self.file = file
        self.dataframe = decrypt_with_unique_id(company, file)
        #TODO create list of people with necessary static features from enrollment



class MedicalCleaner:
    def __init__(self, company, file):
        self.company = company
        self.file = file
        self.dataframe = decrypt_with_unique_id(company, file)









def to_string(f):
    str(f)
