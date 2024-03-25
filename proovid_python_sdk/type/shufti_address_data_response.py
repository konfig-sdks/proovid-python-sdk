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

from proovid_python_sdk.type.error import Error
from proovid_python_sdk.type.info import Info
from proovid_python_sdk.type.shufti_address_data_response_declined_codes import ShuftiAddressDataResponseDeclinedCodes
from proovid_python_sdk.type.verification_data import VerificationData
from proovid_python_sdk.type.verification_result import VerificationResult

class RequiredShuftiAddressDataResponse(TypedDict):
    pass

class OptionalShuftiAddressDataResponse(TypedDict, total=False):
    info: Info

    reference: typing.Optional[str]

    event: typing.Optional[str]

    error: Error

    email: typing.Optional[str]

    country: typing.Optional[str]

    verificationData: VerificationData

    verificationResult: VerificationResult

    declinedReason: typing.Optional[str]

    declinedCodes: typing.Optional[ShuftiAddressDataResponseDeclinedCodes]

class ShuftiAddressDataResponse(RequiredShuftiAddressDataResponse, OptionalShuftiAddressDataResponse):
    pass
