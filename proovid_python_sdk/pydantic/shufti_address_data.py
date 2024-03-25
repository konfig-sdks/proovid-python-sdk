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

from proovid_python_sdk.pydantic.name import Name
from proovid_python_sdk.pydantic.shufti_address_data_selected_type import ShuftiAddressDataSelectedType
from proovid_python_sdk.pydantic.shufti_address_data_supported_types import ShuftiAddressDataSupportedTypes

class ShuftiAddressData(BaseModel):
    issue_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='issueDate')

    full_address: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='fullAddress')

    name: typing.Optional[Name] = Field(None, alias='name')

    selected_type: typing.Optional[ShuftiAddressDataSelectedType] = Field(None, alias='selectedType')

    supported_types: typing.Optional[ShuftiAddressDataSupportedTypes] = Field(None, alias='supportedTypes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
