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

from proovid_python_sdk.pydantic.e_money_range import EMoneyRange
from proovid_python_sdk.pydantic.e_score import EScore
from proovid_python_sdk.pydantic.e_source_of_income_answers import ESourceOfIncomeAnswers
from proovid_python_sdk.pydantic.e_source_of_wealth_answers import ESourceOfWealthAnswers
from proovid_python_sdk.pydantic.e_wealth_range import EWealthRange

class NaturalPersonEconomicProfileResponse(BaseModel):
    main_business_activities: typing.Optional[typing.Optional[str]] = Field(None, alias='mainBusinessActivities')

    size_of_annual_income: typing.Optional[EMoneyRange] = Field(None, alias='sizeOfAnnualIncome')

    size_of_annual_income_min: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='sizeOfAnnualIncomeMin')

    size_of_annual_income_max: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='sizeOfAnnualIncomeMax')

    main_source_of_income: typing.Optional[ESourceOfIncomeAnswers] = Field(None, alias='mainSourceOfIncome')

    size_of_wealth: typing.Optional[EWealthRange] = Field(None, alias='sizeOfWealth')

    size_of_wealth_min: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='sizeOfWealthMin')

    size_of_wealth_max: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='sizeOfWealthMax')

    is_hnwi: typing.Optional[bool] = Field(None, alias='isHnwi')

    source_of_wealth: typing.Optional[ESourceOfWealthAnswers] = Field(None, alias='sourceOfWealth')

    expected_origin_of_outgoing_funds: typing.Optional[typing.Optional[str]] = Field(None, alias='expectedOriginOfOutgoingFunds')

    expected_origin_of_incoming_funds: typing.Optional[typing.Optional[str]] = Field(None, alias='expectedOriginOfIncomingFunds')

    nature_of_transaction: typing.Optional[typing.Optional[str]] = Field(None, alias='natureOfTransaction')

    anticipated_account_turn_over: typing.Optional[EMoneyRange] = Field(None, alias='anticipatedAccountTurnOver')

    anticipated_account_turn_over_min: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='anticipatedAccountTurnOverMin')

    anticipated_account_turn_over_max: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='anticipatedAccountTurnOverMax')

    purpose_of_business_relationship: typing.Optional[typing.Optional[str]] = Field(None, alias='purposeOfBusinessRelationship')

    industry_name_of_highest_risk: typing.Optional[typing.Optional[str]] = Field(None, alias='industryNameOfHighestRisk')

    industry_risk_of_highest_risk: typing.Optional[EScore] = Field(None, alias='industryRiskOfHighestRisk')

    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    last_updated_date: typing.Optional[datetime] = Field(None, alias='lastUpdatedDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
