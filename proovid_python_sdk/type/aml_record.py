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

from proovid_python_sdk.type.aml_record_alternative_names import AmlRecordAlternativeNames
from proovid_python_sdk.type.aml_record_associates import AmlRecordAssociates
from proovid_python_sdk.type.aml_record_categories import AmlRecordCategories
from proovid_python_sdk.type.aml_record_fields import AmlRecordFields
from proovid_python_sdk.type.aml_record_filters import AmlRecordFilters
from proovid_python_sdk.type.aml_record_id_numbers import AmlRecordIdNumbers
from proovid_python_sdk.type.aml_record_images import AmlRecordImages
from proovid_python_sdk.type.aml_record_importan_dates import AmlRecordImportanDates
from proovid_python_sdk.type.aml_record_match_types import AmlRecordMatchTypes
from proovid_python_sdk.type.aml_record_official_lists import AmlRecordOfficialLists
from proovid_python_sdk.type.aml_record_other_names import AmlRecordOtherNames
from proovid_python_sdk.type.aml_record_sanctions_references import AmlRecordSanctionsReferences
from proovid_python_sdk.type.aml_record_source_notes import AmlRecordSourceNotes
from proovid_python_sdk.type.aml_record_sources import AmlRecordSources
from proovid_python_sdk.type.aml_record_types import AmlRecordTypes
from proovid_python_sdk.type.asset import Asset
from proovid_python_sdk.type.associate import Associate
from proovid_python_sdk.type.media import Media

class RequiredAmlRecord(TypedDict):
    pass

class OptionalAmlRecord(TypedDict, total=False):
    id: int

    source: typing.Optional[str]

    firstName: typing.Optional[str]

    middleName: typing.Optional[str]

    lastName: typing.Optional[str]

    gender: typing.Optional[str]

    status: int

    isDeath: typing.Optional[bool]

    dateOfBirth: typing.Optional[datetime]

    placeOfBirth: typing.Optional[str]

    urlReport: typing.Optional[str]

    categories: typing.Optional[AmlRecordCategories]

    notes: typing.Optional[str]

    sanctionsReferences: typing.Optional[AmlRecordSanctionsReferences]

    officialLists: typing.Optional[AmlRecordOfficialLists]

    importanDates: typing.Optional[AmlRecordImportanDates]

    otherNames: typing.Optional[AmlRecordOtherNames]

    idNumbers: typing.Optional[AmlRecordIdNumbers]

    associates: typing.Optional[AmlRecordAssociates]

    images: typing.Optional[AmlRecordImages]

    relatedPersons: typing.Optional[typing.List[Associate]]

    name: typing.Optional[str]

    score: typing.Union[int, float]

    entityType: typing.Optional[str]

    filters: typing.Optional[AmlRecordFilters]

    matchTypes: typing.Optional[AmlRecordMatchTypes]

    alternativeNames: typing.Optional[AmlRecordAlternativeNames]

    sources: typing.Optional[AmlRecordSources]

    types: typing.Optional[AmlRecordTypes]

    assets: typing.Optional[typing.List[Asset]]

    media: typing.Optional[typing.List[Media]]

    fields: typing.Optional[AmlRecordFields]

    sourceNotes: typing.Optional[AmlRecordSourceNotes]

class AmlRecord(RequiredAmlRecord, OptionalAmlRecord):
    pass
