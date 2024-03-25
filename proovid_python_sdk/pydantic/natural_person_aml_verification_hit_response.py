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

from proovid_python_sdk.pydantic.natural_person_aml_verification_hit_response_birth_dates import NaturalPersonAmlVerificationHitResponseBirthDates
from proovid_python_sdk.pydantic.natural_person_aml_verification_hit_response_categories import NaturalPersonAmlVerificationHitResponseCategories
from proovid_python_sdk.pydantic.natural_person_aml_verification_hit_response_match_types import NaturalPersonAmlVerificationHitResponseMatchTypes
from proovid_python_sdk.pydantic.natural_person_aml_verification_hit_response_political_positions import NaturalPersonAmlVerificationHitResponsePoliticalPositions
from proovid_python_sdk.pydantic.natural_person_aml_verification_hit_response_related_urls import NaturalPersonAmlVerificationHitResponseRelatedUrls

class NaturalPersonAmlVerificationHitResponse(BaseModel):
    data_source_name: typing.Optional[typing.Optional[str]] = Field(None, alias='dataSourceName')

    categories: typing.Optional[NaturalPersonAmlVerificationHitResponseCategories] = Field(None, alias='categories')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    country: typing.Optional[typing.Optional[str]] = Field(None, alias='country')

    political_positions: typing.Optional[NaturalPersonAmlVerificationHitResponsePoliticalPositions] = Field(None, alias='politicalPositions')

    related_urls: typing.Optional[NaturalPersonAmlVerificationHitResponseRelatedUrls] = Field(None, alias='relatedUrls')

    birth_dates: typing.Optional[NaturalPersonAmlVerificationHitResponseBirthDates] = Field(None, alias='birthDates')

    match_types: typing.Optional[NaturalPersonAmlVerificationHitResponseMatchTypes] = Field(None, alias='matchTypes')

    match_status: typing.Optional[typing.Optional[str]] = Field(None, alias='matchStatus')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
