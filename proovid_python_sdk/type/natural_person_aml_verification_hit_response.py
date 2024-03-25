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

from proovid_python_sdk.type.natural_person_aml_verification_hit_response_birth_dates import NaturalPersonAmlVerificationHitResponseBirthDates
from proovid_python_sdk.type.natural_person_aml_verification_hit_response_categories import NaturalPersonAmlVerificationHitResponseCategories
from proovid_python_sdk.type.natural_person_aml_verification_hit_response_match_types import NaturalPersonAmlVerificationHitResponseMatchTypes
from proovid_python_sdk.type.natural_person_aml_verification_hit_response_political_positions import NaturalPersonAmlVerificationHitResponsePoliticalPositions
from proovid_python_sdk.type.natural_person_aml_verification_hit_response_related_urls import NaturalPersonAmlVerificationHitResponseRelatedUrls

class RequiredNaturalPersonAmlVerificationHitResponse(TypedDict):
    pass

class OptionalNaturalPersonAmlVerificationHitResponse(TypedDict, total=False):
    dataSourceName: typing.Optional[str]

    categories: typing.Optional[NaturalPersonAmlVerificationHitResponseCategories]

    name: typing.Optional[str]

    country: typing.Optional[str]

    politicalPositions: typing.Optional[NaturalPersonAmlVerificationHitResponsePoliticalPositions]

    relatedUrls: typing.Optional[NaturalPersonAmlVerificationHitResponseRelatedUrls]

    birthDates: typing.Optional[NaturalPersonAmlVerificationHitResponseBirthDates]

    matchTypes: typing.Optional[NaturalPersonAmlVerificationHitResponseMatchTypes]

    matchStatus: typing.Optional[str]

class NaturalPersonAmlVerificationHitResponse(RequiredNaturalPersonAmlVerificationHitResponse, OptionalNaturalPersonAmlVerificationHitResponse):
    pass
