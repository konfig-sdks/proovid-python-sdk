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


class RequiredShuftiAddressResultResponse(TypedDict):
    pass

class OptionalShuftiAddressResultResponse(TypedDict, total=False):
    issueDate: typing.Optional[bool]

    selectedType: typing.Optional[bool]

    addressDocumentCountry: typing.Optional[bool]

    addressDocumentMustNotBeExpired: typing.Optional[bool]

    fullAddress: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    name: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    addressDocumentVisibility: typing.Optional[bool]

    addressDocument: typing.Optional[bool]

    addressDocumentProof: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class ShuftiAddressResultResponse(RequiredShuftiAddressResultResponse, OptionalShuftiAddressResultResponse):
    pass
