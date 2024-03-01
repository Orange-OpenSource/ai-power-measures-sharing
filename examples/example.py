#################################
# AI Power Measure Sharing      #
# Creative Commons 4.0          #
# Orange/INNOV/DATA-AI          #
#################################
#!/usr/bin/python

import json
import pandas as pd
from object_flattener import ObjectFlattener

if __name__ == '__main__':
    of = ObjectFlattener(separator='_')

    print('Test 1 - OK')
    print(str(of.flatten({
        'prop': 'value',
        'figure': 1,
        'empty': {},
        'nested': {
            'sub': 5,
            'renested': {
                'grandson': 'Hello World!',
                'null': None
            }
        }
    })))

    print('Test 2 - KO')
    try:
        print(str(of.flatten({
            'prop': 'value',
            'figure': 1,
            'empty': {},
            'nested': {
                'sub': 5,
                'renested': {
                    'grandson': 'Hello World!',
                    'null': None
                }
            },
            'nested_renested_grandson': 'ambiguous'
        })))
    except:
        print('The dict has ambiguous columns. Failed to flatten.')

    print('Test 3 - Complete conversion from json to csv')
    with open('energy-report-instance1.json') as fp1:
        with open('energy-report-instance2.json') as fp2:
            df = pd.DataFrame([ 
                of.flatten(json.load(fp1)),
                of.flatten(json.load(fp2))
            ])
            df.to_csv('energy-report-format.csv', index=False, header=True)
