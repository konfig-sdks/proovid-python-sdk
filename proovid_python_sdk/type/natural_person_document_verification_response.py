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

from proovid_python_sdk.type.e_gender import EGender
from proovid_python_sdk.type.e_status import EStatus
from proovid_python_sdk.type.reject_label_type import RejectLabelType

class RequiredNaturalPersonDocumentVerificationResponse(TypedDict):
    pass

class OptionalNaturalPersonDocumentVerificationResponse(TypedDict, total=False):
    status: EStatus

    comment: typing.Optional[str]

    rejectLabels: typing.Optional[typing.List[RejectLabelType]]

    firstName: typing.Optional[str]

    lastName: typing.Optional[str]

    dateOfBirth: typing.Optional[datetime]

    gender: EGender

    country: typing.Optional[str]

    issuedDate: typing.Optional[datetime]

    issueAuthority: typing.Optional[str]

    firstIssuedDate: typing.Optional[datetime]

    validUntil: typing.Optional[datetime]

    number: typing.Optional[str]

    additionalNumber: typing.Optional[str]

    mrzLine1: typing.Optional[str]

    mrzLine2: typing.Optional[str]

    mrzLine3: typing.Optional[str]

    imageId: typing.Optional[str]

    additionalImageId: typing.Optional[str]

    creationDate: datetime

    lastUpdatedDate: datetime

class NaturalPersonDocumentVerificationResponse(RequiredNaturalPersonDocumentVerificationResponse, OptionalNaturalPersonDocumentVerificationResponse):
    pass
