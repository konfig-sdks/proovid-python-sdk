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

from proovid_python_sdk.pydantic.e_gender import EGender
from proovid_python_sdk.pydantic.e_score import EScore
from proovid_python_sdk.pydantic.update_natural_person_economic_profile_request import UpdateNaturalPersonEconomicProfileRequest

class UpdateNaturalPersonInfoRequest(BaseModel):
    client_reference_id: typing.Optional[typing.Optional[str]] = Field(None, alias='clientReferenceId')

    tax_id: typing.Optional[typing.Optional[str]] = Field(None, alias='taxId')

    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='firstName')

    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='lastName')

    middle_name: typing.Optional[typing.Optional[str]] = Field(None, alias='middleName')

    legal_name: typing.Optional[typing.Optional[str]] = Field(None, alias='legalName')

    date_of_birth: typing.Optional[typing.Optional[datetime]] = Field(None, alias='dateOfBirth')

    gender: typing.Optional[EGender] = Field(None, alias='gender')

    country_birth: typing.Optional[typing.Optional[str]] = Field(None, alias='countryBirth')

    country_residence: typing.Optional[typing.Optional[str]] = Field(None, alias='countryResidence')

    country_main_business: typing.Optional[typing.Optional[str]] = Field(None, alias='countryMainBusiness')

    nationality: typing.Optional[typing.Optional[str]] = Field(None, alias='nationality')

    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    email_two: typing.Optional[typing.Optional[str]] = Field(None, alias='emailTwo')

    mobile_phone: typing.Optional[typing.Optional[str]] = Field(None, alias='mobilePhone')

    mobile_phone_two: typing.Optional[typing.Optional[str]] = Field(None, alias='mobilePhoneTwo')

    automatically_update_n_p_risk: typing.Optional[typing.Optional[bool]] = Field(None, alias='automaticallyUpdateNPRisk')

    risk_level: typing.Optional[EScore] = Field(None, alias='riskLevel')

    risk_level_justification: typing.Optional[typing.Optional[str]] = Field(None, alias='riskLevelJustification')

    is_flagged: typing.Optional[bool] = Field(None, alias='isFlagged')

    comments: typing.Optional[typing.Optional[str]] = Field(None, alias='comments')

    economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = Field(None, alias='economicProfile')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
