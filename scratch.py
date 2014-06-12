__author__ = 'nuna'

import pandas as pd

claims_path = 'short_clean_medical_claims.csv'
claims = pd.read_csv(claims_path)


enrollment_path = 'enrollment_unique_dependent_id.csv'
enrollment = pd.read_csv(enrollment_path)


unique_claims = claims.drop_duplicates('employee_id', take_last=True)

enrollment['unique_identifier'] = enrollment.ssn.map(str) + '_' + enrollment.date_of_birth.map(str) + '_' + enrollment.first_name

claims['unique_identifier'] = claims.ssn.map(str) + '_' + claims.date_of_birth.map(str) + '_' + claims.first_name

