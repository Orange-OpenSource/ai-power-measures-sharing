# SPDX-License-Identifier: Creative Commons 4.0

 #############################################################################
# ~#~ AI Power Measure Sharing ~#~                                            #
# 'Facilitate knowledge sharing and open data in AI's power consumption'      #
# Orange/INNOV/DATA-AI, Orange Innovation Research Program 'Responsible AI'   #
 #############################################################################

#!/usr/bin/python

import unittest
from services.object_flattener import ObjectFlattener

class FlatteningTest(unittest.TestCase):

    # tests the flattening of a basic JSON object, with only nested dict
    def testFlattenSimpleObject(self):
        fobj = None
        try:
            of = ObjectFlattener(separator='_')
            obj = {
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
            }
            print('Input object is {}'.format(str(obj)))
            fobj = of.flatten(obj)
            print('Flattened object is {}'.format(str(fobj)))
        except Exception as err:
            print('testFlattenSimpleObject raised the following exception: {}'.format(str(err)))

        test = fobj == { 'prop': 'value', 'figure': 1, 'nested_sub': 5, 'nested_renested_grandson': 'Hello World!', 'nested_renested_null': None }
        self.assertEqual(test, True)

    # tests the flattening of a complex JSON object, with nested dict and lists
    def testFlattenComplexObject(self):
        fobj = None
        try:
            of = ObjectFlattener(separator='_')
            obj = {
                'colors': [
                    {
                        '$$key': 'green',
                        'foo': '#00FF00',
                        'bar': 'tree'
                    },
                    {
                        '$$key': 'red',
                        'foo': '#FF0000',
                        'bar': 'fire'
                    },
                    None
                ],
                'nested': {
                    'sub': 5,
                    'names': [ 'Alice', None, 'Bob' ],
                    'renested': {
                        'grandson': 'Hello World!',
                        'nulls': [ None, None, None ]
                    }
                }
            }
            print('Input object is {}'.format(str(obj)))
            fobj = of.flatten(obj)
            print('Flattened object is {}'.format(str(fobj)))
        except Exception as err:
            print('testFlattenSimpleObject raised the following exception: {}'.format(str(err)))

        test = fobj == { 'colors_green_foo': '#00FF00', 'colors_green_bar': 'tree', 'colors_red_foo': '#FF0000', 'colors_red_bar': 'fire', 'nested_sub': 5, 'nested_names_0': 'Alice', 'nested_names_1': None, 'nested_names_2': 'Bob', 'nested_renested_grandson': 'Hello World!', 'nested_renested_nulls_0': None, 'nested_renested_nulls_1': None, 'nested_renested_nulls_2': None }
        self.assertEqual(test, True)

    # tests the flattening of a JSON object resulting in ambiguous columns
    def testFlattenSimpleAmbiguousObject(self):
        test = False
        try:
            of = ObjectFlattener(separator='_')
            obj = of.flatten({
                'nested': {
                    'renested': {
                        'grandson': 'Hello World!',
                        'null': None
                    }
                },
                'nested_renested_grandson': 'ambiguous'
            })
            print('Input object is {}'.format(str(obj)))
            fobj = of.flatten(obj)
            print('Flattened object is {}'.format(str(fobj)))
        except Exception as err:
            print('The dict has ambiguous columns. Consider changing separator. Failed to flatten: {}'.format(err))
            test = True

        self.assertEqual(test, True)

    # tests the flattening of a complex JSON object, where lists are inconsistent
    def testFlattenComplexInconsistentObject1(self):
        test = False
        try:
            of = ObjectFlattener(separator='_')
            obj = {
                'colors': [
                    {
                        '$$key': 'green',
                        'foo': '#00FF00',
                        'bar': 'tree'
                    },
                    {
                        # missing $$key
                        'foo': '#000000',
                        'bar': 'night'
                    },
                    None
                ]
            }
            print('Input object is {}'.format(str(obj)))
            fobj = of.flatten(obj)
            print('Flattened object is {}'.format(str(fobj)))
        except Exception as err:
            print('The dict has an inconsistent list. Failed to flatten: {}'.format(err))
            test = True

        self.assertEqual(test, True)

    # tests the flattening of a complex JSON object, where lists are inconsistent
    def testFlattenComplexInconsistentObject2(self):
        test = False
        try:
            of = ObjectFlattener(separator='_')
            obj = {
                'nested': {
                    'names': [ 'Alice', None, 'Bob', { '$$key': 'heterogeneous' } ],
                }
            }
            print('Input object is {}'.format(str(obj)))
            fobj = of.flatten(obj)
            print('Flattened object is {}'.format(str(fobj)))
        except Exception as err:
            print('The dict has an inconsistent list. Failed to flatten: {}'.format(err))
            test = True

        self.assertEqual(test, True)
