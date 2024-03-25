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

from proovid_python_sdk.type.e_money_range import EMoneyRange
from proovid_python_sdk.type.e_source_of_income_answers import ESourceOfIncomeAnswers
from proovid_python_sdk.type.e_source_of_wealth_answers import ESourceOfWealthAnswers
from proovid_python_sdk.type.e_wealth_range import EWealthRange

class RequiredUpdateNaturalPersonEconomicProfileRequest(TypedDict):
    pass

class OptionalUpdateNaturalPersonEconomicProfileRequest(TypedDict, total=False):
    mainBusinessActivities: typing.Optional[str]

    sizeOfAnnualIncome: EMoneyRange

    sizeOfAnnualIncomeMin: typing.Optional[typing.Union[int, float]]

    sizeOfAnnualIncomeMax: typing.Optional[typing.Union[int, float]]

    mainSourceOfIncome: ESourceOfIncomeAnswers

    sizeOfWealth: EWealthRange

    sizeOfWealthMin: typing.Optional[typing.Union[int, float]]

    sizeOfWealthMax: typing.Optional[typing.Union[int, float]]

    isHnwi: bool

    sourceOfWealth: ESourceOfWealthAnswers

    expectedOriginOfOutgoingFunds: typing.Optional[str]

    expectedOriginOfIncomingFunds: typing.Optional[str]

    natureOfTransaction: typing.Optional[str]

    anticipatedAccountTurnOver: EMoneyRange

    anticipatedAccountTurnOverMin: typing.Optional[typing.Union[int, float]]

    anticipatedAccountTurnOverMax: typing.Optional[typing.Union[int, float]]

    purposeOfBusinessRelationship: typing.Optional[str]

class UpdateNaturalPersonEconomicProfileRequest(RequiredUpdateNaturalPersonEconomicProfileRequest, OptionalUpdateNaturalPersonEconomicProfileRequest):
    pass
