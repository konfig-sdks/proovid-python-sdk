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


class RequiredGeolocation(TypedDict):
    pass

class OptionalGeolocation(TypedDict, total=False):
    host: typing.Optional[str]

    ip: typing.Optional[str]

    rdns: typing.Optional[str]

    asn: typing.Optional[str]

    isp: typing.Optional[str]

    countryName: typing.Optional[str]

    countryCode: typing.Optional[str]

    regionName: typing.Optional[str]

    regionCode: typing.Optional[str]

    city: typing.Optional[str]

    postalCode: typing.Optional[str]

    continentName: typing.Optional[str]

    continentCode: typing.Optional[str]

    latitude: typing.Optional[str]

    longitude: typing.Optional[str]

    metroCode: typing.Optional[str]

    timezone: typing.Optional[str]

class Geolocation(RequiredGeolocation, OptionalGeolocation):
    pass
