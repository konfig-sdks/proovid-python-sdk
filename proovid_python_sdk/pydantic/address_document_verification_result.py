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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from proovid_python_sdk.pydantic.shufti_address_data_response import ShuftiAddressDataResponse

class AddressDocumentVerificationResult(BaseModel):
    reference: typing.Optional[typing.Optional[str]] = Field(None, alias='reference')

    document_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='documentDate')

    document_status: typing.Optional[int] = Field(None, alias='documentStatus')

    document_result: typing.Optional[typing.Optional[str]] = Field(None, alias='documentResult')

    validity_period: typing.Optional[int] = Field(None, alias='validityPeriod')

    error: typing.Optional[typing.Optional[str]] = Field(None, alias='error')

    additional_info: typing.Optional[ShuftiAddressDataResponse] = Field(None, alias='additionalInfo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
