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


class RequiredAddressRequest(TypedDict):
    pass

class OptionalAddressRequest(TypedDict, total=False):
    referenceId: typing.Optional[str]

    email: typing.Optional[str]

    naturalPersonId: typing.Optional[int]

    naturalPersonIndexId: typing.Optional[int]

    name: typing.Optional[str]

    surname: typing.Optional[str]

    mobilePhone: typing.Optional[str]

    language: typing.Optional[str]

    verificationLevel: int

    document: typing.Optional[str]

    street: typing.Optional[str]

    streetNumber: typing.Optional[str]

    unit: typing.Optional[str]

    district: typing.Optional[str]

    city: typing.Optional[str]

    region: typing.Optional[str]

    zipCode: typing.Optional[str]

    country: typing.Optional[str]

    fullAddress: typing.Optional[str]

    skipDocumentComparison: bool

    validityPeriod: int

class AddressRequest(RequiredAddressRequest, OptionalAddressRequest):
    pass
