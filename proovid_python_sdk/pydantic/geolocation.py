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


class Geolocation(BaseModel):
    host: typing.Optional[typing.Optional[str]] = Field(None, alias='host')

    ip: typing.Optional[typing.Optional[str]] = Field(None, alias='ip')

    rdns: typing.Optional[typing.Optional[str]] = Field(None, alias='rdns')

    asn: typing.Optional[typing.Optional[str]] = Field(None, alias='asn')

    isp: typing.Optional[typing.Optional[str]] = Field(None, alias='isp')

    country_name: typing.Optional[typing.Optional[str]] = Field(None, alias='countryName')

    country_code: typing.Optional[typing.Optional[str]] = Field(None, alias='countryCode')

    region_name: typing.Optional[typing.Optional[str]] = Field(None, alias='regionName')

    region_code: typing.Optional[typing.Optional[str]] = Field(None, alias='regionCode')

    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    postal_code: typing.Optional[typing.Optional[str]] = Field(None, alias='postalCode')

    continent_name: typing.Optional[typing.Optional[str]] = Field(None, alias='continentName')

    continent_code: typing.Optional[typing.Optional[str]] = Field(None, alias='continentCode')

    latitude: typing.Optional[typing.Optional[str]] = Field(None, alias='latitude')

    longitude: typing.Optional[typing.Optional[str]] = Field(None, alias='longitude')

    metro_code: typing.Optional[typing.Optional[str]] = Field(None, alias='metroCode')

    timezone: typing.Optional[typing.Optional[str]] = Field(None, alias='timezone')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
