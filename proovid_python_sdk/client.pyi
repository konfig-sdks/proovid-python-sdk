# coding: utf-8
"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

import typing
import inspect
from datetime import date, datetime
from proovid_python_sdk.client_custom import ClientCustom
from proovid_python_sdk.configuration import Configuration
from proovid_python_sdk.api_client import ApiClient
from proovid_python_sdk.type_util import copy_signature
from proovid_python_sdk.apis.tags.address_api import AddressApi
from proovid_python_sdk.apis.tags.document_api import DocumentApi
from proovid_python_sdk.apis.tags.health_api import HealthApi
from proovid_python_sdk.apis.tags.natural_person_api import NaturalPersonApi
from proovid_python_sdk.apis.tags.screening_api import ScreeningApi



class ProoViD(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.address: AddressApi = AddressApi(api_client)
        self.document: DocumentApi = DocumentApi(api_client)
        self.health: HealthApi = HealthApi(api_client)
        self.natural_person: NaturalPersonApi = NaturalPersonApi(api_client)
        self.screening: ScreeningApi = ScreeningApi(api_client)
