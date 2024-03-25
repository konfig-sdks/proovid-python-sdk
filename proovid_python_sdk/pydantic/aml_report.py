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

from proovid_python_sdk.pydantic.aml_record import AmlRecord
from proovid_python_sdk.pydantic.natural_person import NaturalPerson

class AmlReport(BaseModel):
    creation_time: typing.Optional[typing.Optional[datetime]] = Field(None, alias='creationTime')

    reviewed_verification_status: typing.Optional[typing.Optional[str]] = Field(None, alias='reviewedVerificationStatus')

    number_of_records: typing.Optional[int] = Field(None, alias='numberOfRecords')

    natural_person: typing.Optional[NaturalPerson] = Field(None, alias='naturalPerson')

    aml_records: typing.Optional[typing.Optional[typing.List[AmlRecord]]] = Field(None, alias='amlRecords')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
