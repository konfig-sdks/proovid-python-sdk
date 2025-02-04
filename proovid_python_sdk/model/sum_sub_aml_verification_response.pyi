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


class SumSubAmlVerificationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def status() -> typing.Type['EStatus']:
                return EStatus
        
            @staticmethod
            def categories() -> typing.Type['SumSubAmlVerificationResponseCategories']:
                return SumSubAmlVerificationResponseCategories
        
            @staticmethod
            def hasSanctions() -> typing.Type['ESanctionAnswers']:
                return ESanctionAnswers
        
            @staticmethod
            def isPep() -> typing.Type['EPepAnswers']:
                return EPepAnswers
        
            @staticmethod
            def hasNegativeReputation() -> typing.Type['ENegativeReputationAnswers']:
                return ENegativeReputationAnswers
            creationDate = schemas.DateTimeSchema
            
            
            class hits(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SumSubAmlVerificationHitResponse']:
                        return SumSubAmlVerificationHitResponse
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hits':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "status": status,
                "categories": categories,
                "hasSanctions": hasSanctions,
                "isPep": isPep,
                "hasNegativeReputation": hasNegativeReputation,
                "creationDate": creationDate,
                "hits": hits,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'EStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categories"]) -> 'SumSubAmlVerificationResponseCategories': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasSanctions"]) -> 'ESanctionAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPep"]) -> 'EPepAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasNegativeReputation"]) -> 'ENegativeReputationAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creationDate"]) -> MetaOapg.properties.creationDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hits"]) -> MetaOapg.properties.hits: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "categories", "hasSanctions", "isPep", "hasNegativeReputation", "creationDate", "hits", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['EStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categories"]) -> typing.Union['SumSubAmlVerificationResponseCategories', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasSanctions"]) -> typing.Union['ESanctionAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPep"]) -> typing.Union['EPepAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasNegativeReputation"]) -> typing.Union['ENegativeReputationAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creationDate"]) -> typing.Union[MetaOapg.properties.creationDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hits"]) -> typing.Union[MetaOapg.properties.hits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "categories", "hasSanctions", "isPep", "hasNegativeReputation", "creationDate", "hits", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union['EStatus', schemas.Unset] = schemas.unset,
        categories: typing.Union['SumSubAmlVerificationResponseCategories', schemas.Unset] = schemas.unset,
        hasSanctions: typing.Union['ESanctionAnswers', schemas.Unset] = schemas.unset,
        isPep: typing.Union['EPepAnswers', schemas.Unset] = schemas.unset,
        hasNegativeReputation: typing.Union['ENegativeReputationAnswers', schemas.Unset] = schemas.unset,
        creationDate: typing.Union[MetaOapg.properties.creationDate, str, datetime, schemas.Unset] = schemas.unset,
        hits: typing.Union[MetaOapg.properties.hits, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SumSubAmlVerificationResponse':
        return super().__new__(
            cls,
            *args,
            status=status,
            categories=categories,
            hasSanctions=hasSanctions,
            isPep=isPep,
            hasNegativeReputation=hasNegativeReputation,
            creationDate=creationDate,
            hits=hits,
            _configuration=_configuration,
            **kwargs,
        )

from proovid_python_sdk.model.e_negative_reputation_answers import ENegativeReputationAnswers
from proovid_python_sdk.model.e_pep_answers import EPepAnswers
from proovid_python_sdk.model.e_sanction_answers import ESanctionAnswers
from proovid_python_sdk.model.e_status import EStatus
from proovid_python_sdk.model.sum_sub_aml_verification_hit_response import SumSubAmlVerificationHitResponse
from proovid_python_sdk.model.sum_sub_aml_verification_response_categories import SumSubAmlVerificationResponseCategories
