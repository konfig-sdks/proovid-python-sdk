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


class RequiredDocumentVerificationResult(TypedDict):
    pass

class OptionalDocumentVerificationResult(TypedDict, total=False):
    documentValidity: typing.Optional[bool]

    documentVisibility: typing.Optional[bool]

    mustNotBeExpired: typing.Optional[bool]

    documentNumber: typing.Optional[bool]

    issueDate: typing.Optional[bool]

    expiredDate: typing.Optional[bool]

    dob: typing.Optional[bool]

    name: typing.Optional[bool]

    documentCountry: typing.Optional[bool]

    selectedType: typing.Optional[bool]

    faceOnDocumentMatched: typing.Optional[bool]

class DocumentVerificationResult(RequiredDocumentVerificationResult, OptionalDocumentVerificationResult):
    pass
