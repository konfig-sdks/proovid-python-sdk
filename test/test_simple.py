# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

import unittest

import os
from pprint import pprint
from proovid_python_sdk import ProoViD

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        proovid = ProoViD(
        
                        bearer = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(proovid)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
