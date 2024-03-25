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

from proovid_python_sdk.pydantic.sum_sub_aml_verification_response import SumSubAmlVerificationResponse
from proovid_python_sdk.pydantic.sum_sub_document_verification_verification_response import SumSubDocumentVerificationVerificationResponse

class SumSubVerificationResponse(BaseModel):
    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    screening: typing.Optional[SumSubAmlVerificationResponse] = Field(None, alias='screening')

    id_document: typing.Optional[SumSubDocumentVerificationVerificationResponse] = Field(None, alias='idDocument')

    face: typing.Optional[SumSubDocumentVerificationVerificationResponse] = Field(None, alias='face')

    address_document: typing.Optional[SumSubDocumentVerificationVerificationResponse] = Field(None, alias='addressDocument')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
