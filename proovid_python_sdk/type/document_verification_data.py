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


class RequiredDocumentVerificationData(TypedDict):
    pass

class OptionalDocumentVerificationData(TypedDict, total=False):
    firstName: typing.Optional[str]

    lastName: typing.Optional[str]

    middleName: typing.Optional[str]

    fullName: typing.Optional[str]

    documentNumber: typing.Optional[str]

    issueDate: typing.Optional[datetime]

    expiredDate: typing.Optional[datetime]

    dob: typing.Optional[datetime]

    documentType: typing.Optional[str]

    countryBirth: typing.Optional[str]

    countryDocument: typing.Optional[str]

    faceMatchConfidence: typing.Optional[int]

class DocumentVerificationData(RequiredDocumentVerificationData, OptionalDocumentVerificationData):
    pass
