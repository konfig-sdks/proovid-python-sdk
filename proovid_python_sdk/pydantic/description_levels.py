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

from proovid_python_sdk.pydantic.level import Level

class DescriptionLevels(BaseModel):
    level1: typing.Optional[Level] = Field(None, alias='level1')

    level2: typing.Optional[Level] = Field(None, alias='level2')

    level3: typing.Optional[Level] = Field(None, alias='level3')

    level4: typing.Optional[Level] = Field(None, alias='level4')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
