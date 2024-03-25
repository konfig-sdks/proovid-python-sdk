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

from proovid_python_sdk.pydantic.e_negative_reputation_answers import ENegativeReputationAnswers
from proovid_python_sdk.pydantic.e_pep_answers import EPepAnswers
from proovid_python_sdk.pydantic.e_sanction_answers import ESanctionAnswers
from proovid_python_sdk.pydantic.e_status import EStatus
from proovid_python_sdk.pydantic.natural_person_aml_verification_hit_response import NaturalPersonAmlVerificationHitResponse
from proovid_python_sdk.pydantic.natural_person_aml_verification_response_categories import NaturalPersonAmlVerificationResponseCategories

class NaturalPersonAmlVerificationResponse(BaseModel):
    status: typing.Optional[EStatus] = Field(None, alias='status')

    comment: typing.Optional[typing.Optional[str]] = Field(None, alias='comment')

    categories: typing.Optional[NaturalPersonAmlVerificationResponseCategories] = Field(None, alias='categories')

    has_sanctions: typing.Optional[ESanctionAnswers] = Field(None, alias='hasSanctions')

    is_pep: typing.Optional[EPepAnswers] = Field(None, alias='isPep')

    has_negative_reputation: typing.Optional[ENegativeReputationAnswers] = Field(None, alias='hasNegativeReputation')

    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    last_updated_date: typing.Optional[datetime] = Field(None, alias='lastUpdatedDate')

    hits: typing.Optional[typing.Optional[typing.List[NaturalPersonAmlVerificationHitResponse]]] = Field(None, alias='hits')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
