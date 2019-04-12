'''
This script covers all the exercises listed in the paper:

Mendel, Jerry M., and RI Bob John. "Type-2 fuzzy sets made simple." 
IEEE Transactions on fuzzy systems 10.2 (2002): 117-127.

Link: https://ieeexplore.ieee.org/abstract/document/995115

Are implemented here to demonstrate the capabilities of the
type2fuzzylogic library
'''
import numpy as np
import type2fuzzy
from type2fuzzy import GeneralType2FuzzySet

print(f'version: {type2fuzzy.__version__}')


'''
Example 1 : definition of the general type-2 fuzzy set
'''
  
gt2fs_rep =   ''' (0.9/0 + 0.8/0.2+ 0.7/0.4 + 0.6/0.6 + 0.5/0.8)/1
                    +(0.5/0 + 0.35/0.2 + 0.35/0.4 + 0.2/0.6 + 0.5/0.8)/2
                    +(0.35/0.6 + 0.35/0.8)/3
                    +(0.1/0 + 0.35/0.2 + 0.5/0.4 + 0.1/0.6 + 0.35/0.8)/4
                    +(0.35/0 + 0.5/0.2 + 0.1/0.4 + 0.2/0.6 + 0.2/0.8)/5'''

# create set
print('\nSet representation:')
gt2fs = GeneralType2FuzzySet.from_representation(gt2fs_rep)
print(gt2fs)

# get a vertical slice
# example 1
print('\nVertical Slices:')
for x_k in gt2fs.primary_domain():
    print('mu_a_tilde(',x_k,')= ', gt2fs.vertical_slice(x_k))

# get the primary memberships of the set
# example 1 (continued)
print('\nPrimary Membership:')
for x_k in gt2fs.primary_domain():
    print('J_',x_k, ' : ',  gt2fs.primary_membership(x_k)) 

# get the secondary grade of some values
# example 1 (continued)
print('\nSecondary grade of some points:')
print('mu(1,0.2)=',  gt2fs.secondary_grade(1, 0.2), '--> should be 0.8') 
print('mu(2,0)=',  gt2fs.secondary_grade(2, 0), '--> should be 0.5') 
print('mu(3,0.8)=',  gt2fs.secondary_grade(3, 0.8), '--> should be 0.35') 
print('mu(4,0.4)=',  gt2fs.secondary_grade(4, 0.4), '--> should be 0.5') 

# get the footprint of uncertainty for the set
footprint = gt2fs.footprint_of_uncertainty()
print('\nFootprint of uncertainty: ', footprint)

# number of embedded sets
print('\nNumber of embedded type-2 sets: ', gt2fs.embedded_type2_sets_count())

# Example 2
# list all embedded sets
count = 0
print('\nShowing first 10 embedded sets:')
for embedded_set in gt2fs.embedded_type2_sets():
    print(embedded_set)
    count = count+1
    if count > 10:
        break

gt2fs_2_rep = ''' (0.5/0.9)/1 + (0.2/0.7)/1 + (0.9/0.2)/1 + (0.6/0.6)/2 + (0.1/0.4)/2'''

gt2fs_2 = GeneralType2FuzzySet.from_representation(gt2fs_2_rep)

# Example 3
print('\nEmbedded set listing for general type-2 fuzzy set')
print(str(gt2fs_2))
for embedded_set in gt2fs_2.embedded_type2_sets():
        print(embedded_set)