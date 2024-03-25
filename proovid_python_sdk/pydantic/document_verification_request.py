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


class DocumentVerificationRequest(BaseModel):
    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    country: typing.Optional[typing.Optional[str]] = Field(None, alias='country')

    document: typing.Optional[typing.Optional[str]] = Field(None, alias='document')

    additional_document: typing.Optional[typing.Optional[str]] = Field(None, alias='additionalDocument')

    face: typing.Optional[typing.Optional[str]] = Field(None, alias='face')

    document_type: typing.Optional[typing.Optional[str]] = Field(None, alias='documentType')

    natural_person_id: typing.Optional[typing.Optional[int]] = Field(None, alias='naturalPersonId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
