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

from proovid_python_sdk.pydantic.address_document_verification_result import AddressDocumentVerificationResult
from proovid_python_sdk.pydantic.description_levels import DescriptionLevels

class AddressVerificationResult(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    reference: typing.Optional[typing.Optional[str]] = Field(None, alias='reference')

    status: typing.Optional[int] = Field(None, alias='status')

    verification_level: typing.Optional[int] = Field(None, alias='verificationLevel')

    levels: typing.Optional[DescriptionLevels] = Field(None, alias='levels')

    document_verification: typing.Optional[AddressDocumentVerificationResult] = Field(None, alias='documentVerification')

    user_verification_url: typing.Optional[typing.Optional[str]] = Field(None, alias='userVerificationUrl')

    qr_code: typing.Optional[typing.Optional[str]] = Field(None, alias='qrCode')

    creation_time: typing.Optional[datetime] = Field(None, alias='creationTime')

    error: typing.Optional[typing.Optional[str]] = Field(None, alias='error')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
