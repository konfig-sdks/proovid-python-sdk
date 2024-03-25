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

from proovid_python_sdk.pydantic.level_declined_codes import LevelDeclinedCodes
from proovid_python_sdk.pydantic.level_errors import LevelErrors
from proovid_python_sdk.pydantic.level_steps import LevelSteps

class Level(BaseModel):
    id: typing.Optional[typing.Optional[int]] = Field(None, alias='id')

    status: typing.Optional[typing.Optional[int]] = Field(None, alias='status')

    status_description: typing.Optional[typing.Optional[str]] = Field(None, alias='statusDescription')

    steps: typing.Optional[LevelSteps] = Field(None, alias='steps')

    errors: typing.Optional[LevelErrors] = Field(None, alias='errors')

    declined_codes: typing.Optional[LevelDeclinedCodes] = Field(None, alias='declinedCodes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
