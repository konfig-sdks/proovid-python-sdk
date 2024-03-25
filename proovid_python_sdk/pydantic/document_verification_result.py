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


class DocumentVerificationResult(BaseModel):
    document_validity: typing.Optional[typing.Optional[bool]] = Field(None, alias='documentValidity')

    document_visibility: typing.Optional[typing.Optional[bool]] = Field(None, alias='documentVisibility')

    must_not_be_expired: typing.Optional[typing.Optional[bool]] = Field(None, alias='mustNotBeExpired')

    document_number: typing.Optional[typing.Optional[bool]] = Field(None, alias='documentNumber')

    issue_date: typing.Optional[typing.Optional[bool]] = Field(None, alias='issueDate')

    expired_date: typing.Optional[typing.Optional[bool]] = Field(None, alias='expiredDate')

    dob: typing.Optional[typing.Optional[bool]] = Field(None, alias='dob')

    name: typing.Optional[typing.Optional[bool]] = Field(None, alias='name')

    document_country: typing.Optional[typing.Optional[bool]] = Field(None, alias='documentCountry')

    selected_type: typing.Optional[typing.Optional[bool]] = Field(None, alias='selectedType')

    face_on_document_matched: typing.Optional[typing.Optional[bool]] = Field(None, alias='faceOnDocumentMatched')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
