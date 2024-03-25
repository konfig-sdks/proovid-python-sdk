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

from proovid_python_sdk.type.sum_sub_aml_verification_hit_response_birth_dates import SumSubAmlVerificationHitResponseBirthDates
from proovid_python_sdk.type.sum_sub_aml_verification_hit_response_categories import SumSubAmlVerificationHitResponseCategories
from proovid_python_sdk.type.sum_sub_aml_verification_hit_response_match_types import SumSubAmlVerificationHitResponseMatchTypes
from proovid_python_sdk.type.sum_sub_aml_verification_hit_response_political_positions import SumSubAmlVerificationHitResponsePoliticalPositions
from proovid_python_sdk.type.sum_sub_aml_verification_hit_response_related_urls import SumSubAmlVerificationHitResponseRelatedUrls

class RequiredSumSubAmlVerificationHitResponse(TypedDict):
    pass

class OptionalSumSubAmlVerificationHitResponse(TypedDict, total=False):
    dataSourceName: typing.Optional[str]

    categories: typing.Optional[SumSubAmlVerificationHitResponseCategories]

    name: typing.Optional[str]

    country: typing.Optional[str]

    politicalPositions: typing.Optional[SumSubAmlVerificationHitResponsePoliticalPositions]

    relatedUrls: typing.Optional[SumSubAmlVerificationHitResponseRelatedUrls]

    birthDates: typing.Optional[SumSubAmlVerificationHitResponseBirthDates]

    matchTypes: typing.Optional[SumSubAmlVerificationHitResponseMatchTypes]

    matchStatus: typing.Optional[str]

class SumSubAmlVerificationHitResponse(RequiredSumSubAmlVerificationHitResponse, OptionalSumSubAmlVerificationHitResponse):
    pass
