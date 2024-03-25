# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from proovid_python_sdk import schemas  # noqa: F401


class SumSubAmlVerificationHitResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class dataSourceName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dataSourceName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def categories() -> typing.Type['SumSubAmlVerificationHitResponseCategories']:
                return SumSubAmlVerificationHitResponseCategories
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class country(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'country':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def politicalPositions() -> typing.Type['SumSubAmlVerificationHitResponsePoliticalPositions']:
                return SumSubAmlVerificationHitResponsePoliticalPositions
        
            @staticmethod
            def relatedUrls() -> typing.Type['SumSubAmlVerificationHitResponseRelatedUrls']:
                return SumSubAmlVerificationHitResponseRelatedUrls
        
            @staticmethod
            def birthDates() -> typing.Type['SumSubAmlVerificationHitResponseBirthDates']:
                return SumSubAmlVerificationHitResponseBirthDates
        
            @staticmethod
            def matchTypes() -> typing.Type['SumSubAmlVerificationHitResponseMatchTypes']:
                return SumSubAmlVerificationHitResponseMatchTypes
            
            
            class matchStatus(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchStatus':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "dataSourceName": dataSourceName,
                "categories": categories,
                "name": name,
                "country": country,
                "politicalPositions": politicalPositions,
                "relatedUrls": relatedUrls,
                "birthDates": birthDates,
                "matchTypes": matchTypes,
                "matchStatus": matchStatus,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSourceName"]) -> MetaOapg.properties.dataSourceName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categories"]) -> 'SumSubAmlVerificationHitResponseCategories': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["politicalPositions"]) -> 'SumSubAmlVerificationHitResponsePoliticalPositions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relatedUrls"]) -> 'SumSubAmlVerificationHitResponseRelatedUrls': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birthDates"]) -> 'SumSubAmlVerificationHitResponseBirthDates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchTypes"]) -> 'SumSubAmlVerificationHitResponseMatchTypes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchStatus"]) -> MetaOapg.properties.matchStatus: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dataSourceName", "categories", "name", "country", "politicalPositions", "relatedUrls", "birthDates", "matchTypes", "matchStatus", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSourceName"]) -> typing.Union[MetaOapg.properties.dataSourceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categories"]) -> typing.Union['SumSubAmlVerificationHitResponseCategories', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["politicalPositions"]) -> typing.Union['SumSubAmlVerificationHitResponsePoliticalPositions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relatedUrls"]) -> typing.Union['SumSubAmlVerificationHitResponseRelatedUrls', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birthDates"]) -> typing.Union['SumSubAmlVerificationHitResponseBirthDates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchTypes"]) -> typing.Union['SumSubAmlVerificationHitResponseMatchTypes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchStatus"]) -> typing.Union[MetaOapg.properties.matchStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dataSourceName", "categories", "name", "country", "politicalPositions", "relatedUrls", "birthDates", "matchTypes", "matchStatus", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dataSourceName: typing.Union[MetaOapg.properties.dataSourceName, None, str, schemas.Unset] = schemas.unset,
        categories: typing.Union['SumSubAmlVerificationHitResponseCategories', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, None, str, schemas.Unset] = schemas.unset,
        politicalPositions: typing.Union['SumSubAmlVerificationHitResponsePoliticalPositions', schemas.Unset] = schemas.unset,
        relatedUrls: typing.Union['SumSubAmlVerificationHitResponseRelatedUrls', schemas.Unset] = schemas.unset,
        birthDates: typing.Union['SumSubAmlVerificationHitResponseBirthDates', schemas.Unset] = schemas.unset,
        matchTypes: typing.Union['SumSubAmlVerificationHitResponseMatchTypes', schemas.Unset] = schemas.unset,
        matchStatus: typing.Union[MetaOapg.properties.matchStatus, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SumSubAmlVerificationHitResponse':
        return super().__new__(
            cls,
            *args,
            dataSourceName=dataSourceName,
            categories=categories,
            name=name,
            country=country,
            politicalPositions=politicalPositions,
            relatedUrls=relatedUrls,
            birthDates=birthDates,
            matchTypes=matchTypes,
            matchStatus=matchStatus,
            _configuration=_configuration,
            **kwargs,
        )

from proovid_python_sdk.model.sum_sub_aml_verification_hit_response_birth_dates import SumSubAmlVerificationHitResponseBirthDates
from proovid_python_sdk.model.sum_sub_aml_verification_hit_response_categories import SumSubAmlVerificationHitResponseCategories
from proovid_python_sdk.model.sum_sub_aml_verification_hit_response_match_types import SumSubAmlVerificationHitResponseMatchTypes
from proovid_python_sdk.model.sum_sub_aml_verification_hit_response_political_positions import SumSubAmlVerificationHitResponsePoliticalPositions
from proovid_python_sdk.model.sum_sub_aml_verification_hit_response_related_urls import SumSubAmlVerificationHitResponseRelatedUrls
