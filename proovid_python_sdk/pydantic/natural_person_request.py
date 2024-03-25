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


class NaturalPersonRequest(BaseModel):
    natural_person_id: typing.Optional[typing.Optional[int]] = Field(None, alias='naturalPersonId')

    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='firstName')

    middle_name: typing.Optional[typing.Optional[str]] = Field(None, alias='middleName')

    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='lastName')

    dob: typing.Optional[datetime] = Field(None, alias='dob')

    partial_match: typing.Optional[typing.Optional[str]] = Field(None, alias='partialMatch')

    document: typing.Optional[typing.Optional[str]] = Field(None, alias='document')

    document_type: typing.Optional[typing.Optional[str]] = Field(None, alias='documentType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
