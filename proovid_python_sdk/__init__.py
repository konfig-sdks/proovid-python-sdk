# coding: utf-8

# flake8: noqa

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

__version__ = "v1"

# import ApiClient
from proovid_python_sdk.api_client import ApiClient

# import Configuration
from proovid_python_sdk.configuration import Configuration

# import exceptions
from proovid_python_sdk.exceptions import OpenApiException
from proovid_python_sdk.exceptions import ApiAttributeError
from proovid_python_sdk.exceptions import ApiTypeError
from proovid_python_sdk.exceptions import ApiValueError
from proovid_python_sdk.exceptions import ApiKeyError
from proovid_python_sdk.exceptions import ApiException

from proovid_python_sdk.client import ProoViD
