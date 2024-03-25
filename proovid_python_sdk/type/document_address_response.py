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


class RequiredDocumentAddressResponse(TypedDict):
    pass

class OptionalDocumentAddressResponse(TypedDict, total=False):
    street: typing.Optional[str]

    streetNumber: typing.Optional[str]

    buildingName: typing.Optional[str]

    buildingNumber: typing.Optional[str]

    flatNumber: typing.Optional[str]

    city: typing.Optional[str]

    state: typing.Optional[str]

    zipCode: typing.Optional[str]

    country: typing.Optional[str]

class DocumentAddressResponse(RequiredDocumentAddressResponse, OptionalDocumentAddressResponse):
    pass
