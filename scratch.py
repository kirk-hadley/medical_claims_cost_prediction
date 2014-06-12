__author__ = 'nuna'

import pandas as pd

claims_path = 'short_clean_medical_claims.csv'
claims = pd.read_csv(claims_path)


enrollment_path = 'enrollment_unique_dependent_id.csv'
enrollment = pd.read_csv(enrollment_path)

pd.DataFrame(enrollment.city, claims.city)


pd.concat([enrollment.city, claims.city], axis=1)


claims.columns



l = pd.DataFrame()

for i in enrollment.employee_id:
    if i in claims.employee_id.values:
        l = l.append(enrollment[enrollment['employee_id'] == i])
    else:
        print 'no'

unique_claims = claims.drop_duplicates('employee_id', take_last=True)