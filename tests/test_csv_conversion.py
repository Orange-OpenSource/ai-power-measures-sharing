#################################
# AI Power Measure Sharing      #
# Creative Commons 4.0          #
# Orange/INNOV/DATA-AI          #
#################################
#!/usr/bin/python

import unittest
import json
import pandas as pd
from services.object_flattener import ObjectFlattener

class FlatteningAndConversionTest(unittest.TestCase):

    # tests the conversion to CSV of a JSON report
    def testFlattenSimpleObject(self):
        test = False
        try:
            # TODO: correct paths
            with open('energy-report-instance1.json') as fp1:
                with open('energy-report-instance2.json') as fp2:
                    of = ObjectFlattener()
                    df = pd.DataFrame([ 
                        of.flatten(json.load(fp1)),
                        of.flatten(json.load(fp2))
                    ])
                    df.to_csv('energy-report-format.csv', index=False, header=True)
                    # TODO: check file presence and erase
        except Exception as err:  
            print('CSV conversion raised: {}'.format(str(err)))              

        self.assertEqual(test, True)

