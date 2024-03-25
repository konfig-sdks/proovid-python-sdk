# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

import unittest
from unittest.mock import patch

import urllib3

import proovid_python_sdk
from proovid_python_sdk.paths.api_natural_person_verify import post
from proovid_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiNaturalPersonVerify(ApiTestMixin, unittest.TestCase):
    """
    ApiNaturalPersonVerify unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()
