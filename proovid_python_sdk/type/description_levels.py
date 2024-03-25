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

from proovid_python_sdk.type.level import Level

class RequiredDescriptionLevels(TypedDict):
    pass

class OptionalDescriptionLevels(TypedDict, total=False):
    level1: Level

    level2: Level

    level3: Level

    level4: Level

class DescriptionLevels(RequiredDescriptionLevels, OptionalDescriptionLevels):
    pass
