# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from proovid_python_sdk.type.base_response import BaseResponse
from proovid_python_sdk.type.string_base_response import StringBaseResponse

class RequiredAddNaturalPersonDataSaveResult(TypedDict):
    pass

class OptionalAddNaturalPersonDataSaveResult(TypedDict, total=False):
    naturalPersonAdded: BaseResponse

    idDocumentSaved: BaseResponse

    livenessCheckURL: StringBaseResponse

    faceSaved: BaseResponse

    addressDocumentSaved: BaseResponse

    verificationStarted: BaseResponse

    allSucceeded: bool

class AddNaturalPersonDataSaveResult(RequiredAddNaturalPersonDataSaveResult, OptionalAddNaturalPersonDataSaveResult):
    pass
