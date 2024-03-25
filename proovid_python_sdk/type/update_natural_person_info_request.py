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

from proovid_python_sdk.type.e_gender import EGender
from proovid_python_sdk.type.e_score import EScore
from proovid_python_sdk.type.update_natural_person_economic_profile_request import UpdateNaturalPersonEconomicProfileRequest

class RequiredUpdateNaturalPersonInfoRequest(TypedDict):
    pass

class OptionalUpdateNaturalPersonInfoRequest(TypedDict, total=False):
    clientReferenceId: typing.Optional[str]

    taxId: typing.Optional[str]

    firstName: typing.Optional[str]

    lastName: typing.Optional[str]

    middleName: typing.Optional[str]

    legalName: typing.Optional[str]

    dateOfBirth: typing.Optional[datetime]

    gender: EGender

    countryBirth: typing.Optional[str]

    countryResidence: typing.Optional[str]

    countryMainBusiness: typing.Optional[str]

    nationality: typing.Optional[str]

    email: typing.Optional[str]

    emailTwo: typing.Optional[str]

    mobilePhone: typing.Optional[str]

    mobilePhoneTwo: typing.Optional[str]

    automaticallyUpdateNPRisk: typing.Optional[bool]

    riskLevel: EScore

    riskLevelJustification: typing.Optional[str]

    isFlagged: bool

    comments: typing.Optional[str]

    economicProfile: UpdateNaturalPersonEconomicProfileRequest

class UpdateNaturalPersonInfoRequest(RequiredUpdateNaturalPersonInfoRequest, OptionalUpdateNaturalPersonInfoRequest):
    pass
