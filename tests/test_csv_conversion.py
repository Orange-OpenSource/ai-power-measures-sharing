#################################
# AI Power Measure Sharing      #
# Creative Commons 4.0          #
# Orange/INNOV/DATA-AI          #
#################################
#!/usr/bin/python

import unittest
import json
import os
import pandas as pd
from services.object_flattener import ObjectFlattener

class FlatteningAndConversionTest(unittest.TestCase):

    # tests the conversion to CSV of a JSON report
    def testFlattenSimpleObject(self):
        test = False
        csv_path = os.sep.join([ '.', 'tests', 'data', 'energy-report-format.csv' ])
        instance1 = os.sep.join([ '.', 'tests', 'data', 'energy-report-instance1.json' ])
        instance2 = os.sep.join([ '.', 'tests', 'data', 'energy-report-instance2.json' ])

        if os.path.isfile(csv_path):
            os.remove(csv_path)

        try:
            with open(instance1) as fp1:
                with open(instance2) as fp2:
                    of = ObjectFlattener()
                    df = pd.DataFrame([ 
                        of.flatten(json.load(fp1)),
                        of.flatten(json.load(fp2))
                    ])
                    df.to_csv(csv_path, index=False, header=True)
        except Exception as err:  
            print('CSV conversion raised: {}'.format(str(err)))
        
        if os.path.isfile(csv_path):
            test = True
            os.remove(csv_path)

        self.assertEqual(test, True)

