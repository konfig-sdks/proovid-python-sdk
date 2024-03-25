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

from proovid_python_sdk.type.e_negative_reputation_answers import ENegativeReputationAnswers
from proovid_python_sdk.type.e_pep_answers import EPepAnswers
from proovid_python_sdk.type.e_sanction_answers import ESanctionAnswers
from proovid_python_sdk.type.e_status import EStatus
from proovid_python_sdk.type.sum_sub_aml_verification_hit_response import SumSubAmlVerificationHitResponse
from proovid_python_sdk.type.sum_sub_aml_verification_response_categories import SumSubAmlVerificationResponseCategories

class RequiredSumSubAmlVerificationResponse(TypedDict):
    pass

class OptionalSumSubAmlVerificationResponse(TypedDict, total=False):
    status: EStatus

    categories: typing.Optional[SumSubAmlVerificationResponseCategories]

    hasSanctions: ESanctionAnswers

    isPep: EPepAnswers

    hasNegativeReputation: ENegativeReputationAnswers

    creationDate: datetime

    hits: typing.Optional[typing.List[SumSubAmlVerificationHitResponse]]

class SumSubAmlVerificationResponse(RequiredSumSubAmlVerificationResponse, OptionalSumSubAmlVerificationResponse):
    pass
