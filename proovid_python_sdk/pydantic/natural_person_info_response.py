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
from proovid_python_sdk.pydantic.e_status import EStatus
from proovid_python_sdk.pydantic.natural_person_address_verification_response import NaturalPersonAddressVerificationResponse
from proovid_python_sdk.pydantic.natural_person_aml_verification_response import NaturalPersonAmlVerificationResponse
from proovid_python_sdk.pydantic.natural_person_document_verification_response import NaturalPersonDocumentVerificationResponse
from proovid_python_sdk.pydantic.natural_person_economic_profile_response import NaturalPersonEconomicProfileResponse
from proovid_python_sdk.pydantic.natural_person_face_verification_response import NaturalPersonFaceVerificationResponse
from proovid_python_sdk.pydantic.natural_person_occupation_response import NaturalPersonOccupationResponse
from proovid_python_sdk.pydantic.natural_person_other_source_of_income_response import NaturalPersonOtherSourceOfIncomeResponse
from proovid_python_sdk.pydantic.natural_person_other_source_of_wealth_response import NaturalPersonOtherSourceOfWealthResponse
from proovid_python_sdk.pydantic.reject_label_type import RejectLabelType

class NaturalPersonInfoResponse(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    client_reference_id: typing.Optional[typing.Optional[str]] = Field(None, alias='clientReferenceId')

    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    last_updated_date: typing.Optional[datetime] = Field(None, alias='lastUpdatedDate')

    deletion_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='deletionDate')

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

    status: typing.Optional[EStatus] = Field(None, alias='status')

    reject_labels: typing.Optional[typing.Optional[typing.List[RejectLabelType]]] = Field(None, alias='rejectLabels')

    is_flagged: typing.Optional[bool] = Field(None, alias='isFlagged')

    comments: typing.Optional[typing.Optional[str]] = Field(None, alias='comments')

    economic_profile: typing.Optional[NaturalPersonEconomicProfileResponse] = Field(None, alias='economicProfile')

    document_verification: typing.Optional[NaturalPersonDocumentVerificationResponse] = Field(None, alias='documentVerification')

    address_verification: typing.Optional[NaturalPersonAddressVerificationResponse] = Field(None, alias='addressVerification')

    face_verification: typing.Optional[NaturalPersonFaceVerificationResponse] = Field(None, alias='faceVerification')

    screening_verification: typing.Optional[NaturalPersonAmlVerificationResponse] = Field(None, alias='screeningVerification')

    other_sources_of_income: typing.Optional[typing.Optional[typing.List[NaturalPersonOtherSourceOfIncomeResponse]]] = Field(None, alias='otherSourcesOfIncome')

    other_sources_of_wealth: typing.Optional[typing.Optional[typing.List[NaturalPersonOtherSourceOfWealthResponse]]] = Field(None, alias='otherSourcesOfWealth')

    industries: typing.Optional[typing.Optional[typing.List[NaturalPersonOccupationResponse]]] = Field(None, alias='industries')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
