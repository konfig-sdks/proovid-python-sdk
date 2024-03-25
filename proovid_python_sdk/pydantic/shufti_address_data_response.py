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

from proovid_python_sdk.pydantic.error import Error
from proovid_python_sdk.pydantic.info import Info
from proovid_python_sdk.pydantic.shufti_address_data_response_declined_codes import ShuftiAddressDataResponseDeclinedCodes
from proovid_python_sdk.pydantic.verification_data import VerificationData
from proovid_python_sdk.pydantic.verification_result import VerificationResult

class ShuftiAddressDataResponse(BaseModel):
    info: typing.Optional[Info] = Field(None, alias='info')

    reference: typing.Optional[typing.Optional[str]] = Field(None, alias='reference')

    event: typing.Optional[typing.Optional[str]] = Field(None, alias='event')

    error: typing.Optional[Error] = Field(None, alias='error')

    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    country: typing.Optional[typing.Optional[str]] = Field(None, alias='country')

    verification_data: typing.Optional[VerificationData] = Field(None, alias='verificationData')

    verification_result: typing.Optional[VerificationResult] = Field(None, alias='verificationResult')

    declined_reason: typing.Optional[typing.Optional[str]] = Field(None, alias='declinedReason')

    declined_codes: typing.Optional[ShuftiAddressDataResponseDeclinedCodes] = Field(None, alias='declinedCodes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
