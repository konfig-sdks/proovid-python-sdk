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


class NaturalPersonELVRequest(BaseModel):
    natural_person_index_id: typing.Optional[int] = Field(None, alias='naturalPersonIndexId')

    street: typing.Optional[typing.Optional[str]] = Field(None, alias='street')

    street_number: typing.Optional[typing.Optional[str]] = Field(None, alias='streetNumber')

    unit: typing.Optional[typing.Optional[str]] = Field(None, alias='unit')

    zip_code: typing.Optional[typing.Optional[str]] = Field(None, alias='zipCode')

    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    district: typing.Optional[typing.Optional[str]] = Field(None, alias='district')

    region: typing.Optional[typing.Optional[str]] = Field(None, alias='region')

    country: typing.Optional[typing.Optional[str]] = Field(None, alias='country')

    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    mobile: typing.Optional[typing.Optional[str]] = Field(None, alias='mobile')

    full_address: typing.Optional[typing.Optional[str]] = Field(None, alias='fullAddress')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
