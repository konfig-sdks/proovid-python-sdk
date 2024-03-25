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


class ShuftiAddressResultResponse(BaseModel):
    issue_date: typing.Optional[typing.Optional[bool]] = Field(None, alias='issueDate')

    selected_type: typing.Optional[typing.Optional[bool]] = Field(None, alias='selectedType')

    address_document_country: typing.Optional[typing.Optional[bool]] = Field(None, alias='addressDocumentCountry')

    address_document_must_not_be_expired: typing.Optional[typing.Optional[bool]] = Field(None, alias='addressDocumentMustNotBeExpired')

    full_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='fullAddress')

    name: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='name')

    address_document_visibility: typing.Optional[typing.Optional[bool]] = Field(None, alias='addressDocumentVisibility')

    address_document: typing.Optional[typing.Optional[bool]] = Field(None, alias='addressDocument')

    address_document_proof: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='addressDocumentProof')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
