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
from proovid_python_sdk.type.e_status import EStatus
from proovid_python_sdk.type.natural_person_address_verification_response import NaturalPersonAddressVerificationResponse
from proovid_python_sdk.type.natural_person_aml_verification_response import NaturalPersonAmlVerificationResponse
from proovid_python_sdk.type.natural_person_document_verification_response import NaturalPersonDocumentVerificationResponse
from proovid_python_sdk.type.natural_person_economic_profile_response import NaturalPersonEconomicProfileResponse
from proovid_python_sdk.type.natural_person_face_verification_response import NaturalPersonFaceVerificationResponse
from proovid_python_sdk.type.natural_person_occupation_response import NaturalPersonOccupationResponse
from proovid_python_sdk.type.natural_person_other_source_of_income_response import NaturalPersonOtherSourceOfIncomeResponse
from proovid_python_sdk.type.natural_person_other_source_of_wealth_response import NaturalPersonOtherSourceOfWealthResponse
from proovid_python_sdk.type.reject_label_type import RejectLabelType

class RequiredNaturalPersonInfoResponse(TypedDict):
    pass

class OptionalNaturalPersonInfoResponse(TypedDict, total=False):
    id: int

    clientReferenceId: typing.Optional[str]

    creationDate: datetime

    lastUpdatedDate: datetime

    deletionDate: typing.Optional[datetime]

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

    status: EStatus

    rejectLabels: typing.Optional[typing.List[RejectLabelType]]

    isFlagged: bool

    comments: typing.Optional[str]

    economicProfile: NaturalPersonEconomicProfileResponse

    documentVerification: NaturalPersonDocumentVerificationResponse

    addressVerification: NaturalPersonAddressVerificationResponse

    faceVerification: NaturalPersonFaceVerificationResponse

    screeningVerification: NaturalPersonAmlVerificationResponse

    otherSourcesOfIncome: typing.Optional[typing.List[NaturalPersonOtherSourceOfIncomeResponse]]

    otherSourcesOfWealth: typing.Optional[typing.List[NaturalPersonOtherSourceOfWealthResponse]]

    industries: typing.Optional[typing.List[NaturalPersonOccupationResponse]]

class NaturalPersonInfoResponse(RequiredNaturalPersonInfoResponse, OptionalNaturalPersonInfoResponse):
    pass
