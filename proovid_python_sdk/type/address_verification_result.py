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

from proovid_python_sdk.type.address_document_verification_result import AddressDocumentVerificationResult
from proovid_python_sdk.type.description_levels import DescriptionLevels

class RequiredAddressVerificationResult(TypedDict):
    pass

class OptionalAddressVerificationResult(TypedDict, total=False):
    id: int

    reference: typing.Optional[str]

    status: int

    verificationLevel: int

    levels: DescriptionLevels

    documentVerification: AddressDocumentVerificationResult

    userVerificationUrl: typing.Optional[str]

    qrCode: typing.Optional[str]

    creationTime: datetime

    error: typing.Optional[str]

class AddressVerificationResult(RequiredAddressVerificationResult, OptionalAddressVerificationResult):
    pass
