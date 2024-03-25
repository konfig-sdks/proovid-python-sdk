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


class AddressRequest(BaseModel):
    reference_id: typing.Optional[typing.Optional[str]] = Field(None, alias='referenceId')

    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    natural_person_id: typing.Optional[typing.Optional[int]] = Field(None, alias='naturalPersonId')

    natural_person_index_id: typing.Optional[typing.Optional[int]] = Field(None, alias='naturalPersonIndexId')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    surname: typing.Optional[typing.Optional[str]] = Field(None, alias='surname')

    mobile_phone: typing.Optional[typing.Optional[str]] = Field(None, alias='mobilePhone')

    language: typing.Optional[typing.Optional[str]] = Field(None, alias='language')

    verification_level: typing.Optional[int] = Field(None, alias='verificationLevel')

    document: typing.Optional[typing.Optional[str]] = Field(None, alias='document')

    street: typing.Optional[typing.Optional[str]] = Field(None, alias='street')

    street_number: typing.Optional[typing.Optional[str]] = Field(None, alias='streetNumber')

    unit: typing.Optional[typing.Optional[str]] = Field(None, alias='unit')

    district: typing.Optional[typing.Optional[str]] = Field(None, alias='district')

    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    region: typing.Optional[typing.Optional[str]] = Field(None, alias='region')

    zip_code: typing.Optional[typing.Optional[str]] = Field(None, alias='zipCode')

    country: typing.Optional[typing.Optional[str]] = Field(None, alias='country')

    full_address: typing.Optional[typing.Optional[str]] = Field(None, alias='fullAddress')

    skip_document_comparison: typing.Optional[bool] = Field(None, alias='skipDocumentComparison')

    validity_period: typing.Optional[int] = Field(None, alias='validityPeriod')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
