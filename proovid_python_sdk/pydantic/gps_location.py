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


class GpsLocation(BaseModel):
    latitude: typing.Optional[typing.Union[int, float]] = Field(None, alias='latitude')

    longitude: typing.Optional[typing.Union[int, float]] = Field(None, alias='longitude')

    accuracy: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='accuracy')

    altitude: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='altitude')

    altitude_accuracy: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='altitudeAccuracy')

    heading: typing.Optional[typing.Optional[str]] = Field(None, alias='heading')

    speed: typing.Optional[typing.Optional[str]] = Field(None, alias='speed')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
