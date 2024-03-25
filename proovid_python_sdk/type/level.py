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

from proovid_python_sdk.type.level_declined_codes import LevelDeclinedCodes
from proovid_python_sdk.type.level_errors import LevelErrors
from proovid_python_sdk.type.level_steps import LevelSteps

class RequiredLevel(TypedDict):
    pass

class OptionalLevel(TypedDict, total=False):
    id: typing.Optional[int]

    status: typing.Optional[int]

    statusDescription: typing.Optional[str]

    steps: typing.Optional[LevelSteps]

    errors: typing.Optional[LevelErrors]

    declinedCodes: typing.Optional[LevelDeclinedCodes]

class Level(RequiredLevel, OptionalLevel):
    pass
