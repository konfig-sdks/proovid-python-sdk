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

from proovid_python_sdk.pydantic.aml_record_alternative_names import AmlRecordAlternativeNames
from proovid_python_sdk.pydantic.aml_record_associates import AmlRecordAssociates
from proovid_python_sdk.pydantic.aml_record_categories import AmlRecordCategories
from proovid_python_sdk.pydantic.aml_record_fields import AmlRecordFields
from proovid_python_sdk.pydantic.aml_record_filters import AmlRecordFilters
from proovid_python_sdk.pydantic.aml_record_id_numbers import AmlRecordIdNumbers
from proovid_python_sdk.pydantic.aml_record_images import AmlRecordImages
from proovid_python_sdk.pydantic.aml_record_importan_dates import AmlRecordImportanDates
from proovid_python_sdk.pydantic.aml_record_match_types import AmlRecordMatchTypes
from proovid_python_sdk.pydantic.aml_record_official_lists import AmlRecordOfficialLists
from proovid_python_sdk.pydantic.aml_record_other_names import AmlRecordOtherNames
from proovid_python_sdk.pydantic.aml_record_sanctions_references import AmlRecordSanctionsReferences
from proovid_python_sdk.pydantic.aml_record_source_notes import AmlRecordSourceNotes
from proovid_python_sdk.pydantic.aml_record_sources import AmlRecordSources
from proovid_python_sdk.pydantic.aml_record_types import AmlRecordTypes
from proovid_python_sdk.pydantic.asset import Asset
from proovid_python_sdk.pydantic.associate import Associate
from proovid_python_sdk.pydantic.media import Media

class AmlRecord(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    source: typing.Optional[typing.Optional[str]] = Field(None, alias='source')

    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='firstName')

    middle_name: typing.Optional[typing.Optional[str]] = Field(None, alias='middleName')

    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='lastName')

    gender: typing.Optional[typing.Optional[str]] = Field(None, alias='gender')

    status: typing.Optional[int] = Field(None, alias='status')

    is_death: typing.Optional[typing.Optional[bool]] = Field(None, alias='isDeath')

    date_of_birth: typing.Optional[typing.Optional[datetime]] = Field(None, alias='dateOfBirth')

    place_of_birth: typing.Optional[typing.Optional[str]] = Field(None, alias='placeOfBirth')

    url_report: typing.Optional[typing.Optional[str]] = Field(None, alias='urlReport')

    categories: typing.Optional[AmlRecordCategories] = Field(None, alias='categories')

    notes: typing.Optional[typing.Optional[str]] = Field(None, alias='notes')

    sanctions_references: typing.Optional[AmlRecordSanctionsReferences] = Field(None, alias='sanctionsReferences')

    official_lists: typing.Optional[AmlRecordOfficialLists] = Field(None, alias='officialLists')

    importan_dates: typing.Optional[AmlRecordImportanDates] = Field(None, alias='importanDates')

    other_names: typing.Optional[AmlRecordOtherNames] = Field(None, alias='otherNames')

    id_numbers: typing.Optional[AmlRecordIdNumbers] = Field(None, alias='idNumbers')

    associates: typing.Optional[AmlRecordAssociates] = Field(None, alias='associates')

    images: typing.Optional[AmlRecordImages] = Field(None, alias='images')

    related_persons: typing.Optional[typing.Optional[typing.List[Associate]]] = Field(None, alias='relatedPersons')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    score: typing.Optional[typing.Union[int, float]] = Field(None, alias='score')

    entity_type: typing.Optional[typing.Optional[str]] = Field(None, alias='entityType')

    filters: typing.Optional[AmlRecordFilters] = Field(None, alias='filters')

    match_types: typing.Optional[AmlRecordMatchTypes] = Field(None, alias='matchTypes')

    alternative_names: typing.Optional[AmlRecordAlternativeNames] = Field(None, alias='alternativeNames')

    sources: typing.Optional[AmlRecordSources] = Field(None, alias='sources')

    types: typing.Optional[AmlRecordTypes] = Field(None, alias='types')

    assets: typing.Optional[typing.Optional[typing.List[Asset]]] = Field(None, alias='assets')

    media: typing.Optional[typing.Optional[typing.List[Media]]] = Field(None, alias='media')

    fields: typing.Optional[AmlRecordFields] = Field(None, alias='fields')

    source_notes: typing.Optional[AmlRecordSourceNotes] = Field(None, alias='sourceNotes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
