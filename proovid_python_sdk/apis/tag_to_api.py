import typing_extensions

from proovid_python_sdk.apis.tags import TagValues
from proovid_python_sdk.apis.tags.natural_person_api import NaturalPersonApi
from proovid_python_sdk.apis.tags.address_api import AddressApi
from proovid_python_sdk.apis.tags.document_api import DocumentApi
from proovid_python_sdk.apis.tags.screening_api import ScreeningApi
from proovid_python_sdk.apis.tags.health_api import HealthApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.NATURAL_PERSON: NaturalPersonApi,
        TagValues.ADDRESS: AddressApi,
        TagValues.DOCUMENT: DocumentApi,
        TagValues.SCREENING: ScreeningApi,
        TagValues.HEALTH: HealthApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.NATURAL_PERSON: NaturalPersonApi,
        TagValues.ADDRESS: AddressApi,
        TagValues.DOCUMENT: DocumentApi,
        TagValues.SCREENING: ScreeningApi,
        TagValues.HEALTH: HealthApi,
    }
)
