# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from proovid_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from proovid_python_sdk.api_response import AsyncGeneratorResponse
from proovid_python_sdk import api_client, exceptions
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

from proovid_python_sdk.model.update_natural_person_info_request import UpdateNaturalPersonInfoRequest as UpdateNaturalPersonInfoRequestSchema
from proovid_python_sdk.model.natural_person_info_response_base_response import NaturalPersonInfoResponseBaseResponse as NaturalPersonInfoResponseBaseResponseSchema
from proovid_python_sdk.model.e_gender import EGender as EGenderSchema
from proovid_python_sdk.model.base_response import BaseResponse as BaseResponseSchema
from proovid_python_sdk.model.update_natural_person_economic_profile_request import UpdateNaturalPersonEconomicProfileRequest as UpdateNaturalPersonEconomicProfileRequestSchema
from proovid_python_sdk.model.e_score import EScore as EScoreSchema

from proovid_python_sdk.type.base_response import BaseResponse
from proovid_python_sdk.type.update_natural_person_info_request import UpdateNaturalPersonInfoRequest
from proovid_python_sdk.type.update_natural_person_economic_profile_request import UpdateNaturalPersonEconomicProfileRequest
from proovid_python_sdk.type.e_gender import EGender
from proovid_python_sdk.type.e_score import EScore
from proovid_python_sdk.type.natural_person_info_response_base_response import NaturalPersonInfoResponseBaseResponse

from ...api_client import Dictionary
from proovid_python_sdk.pydantic.base_response import BaseResponse as BaseResponsePydantic
from proovid_python_sdk.pydantic.update_natural_person_info_request import UpdateNaturalPersonInfoRequest as UpdateNaturalPersonInfoRequestPydantic
from proovid_python_sdk.pydantic.update_natural_person_economic_profile_request import UpdateNaturalPersonEconomicProfileRequest as UpdateNaturalPersonEconomicProfileRequestPydantic
from proovid_python_sdk.pydantic.e_score import EScore as EScorePydantic
from proovid_python_sdk.pydantic.natural_person_info_response_base_response import NaturalPersonInfoResponseBaseResponse as NaturalPersonInfoResponseBaseResponsePydantic
from proovid_python_sdk.pydantic.e_gender import EGender as EGenderPydantic

from . import path

# Path params
NaturalPersonIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'naturalPersonId': typing.Union[NaturalPersonIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_natural_person_id = api_client.PathParameter(
    name="naturalPersonId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NaturalPersonIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateNaturalPersonInfoRequestSchema
SchemaForRequestBodyTextJson = UpdateNaturalPersonInfoRequestSchema
SchemaForRequestBodyApplicationJsonPatchjson = UpdateNaturalPersonInfoRequestSchema
SchemaForRequestBodyApplicationJson = UpdateNaturalPersonInfoRequestSchema


request_body_update_natural_person_info_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Bearer',
]
SchemaFor200ResponseBodyApplicationJson = NaturalPersonInfoResponseBaseResponseSchema
SchemaFor200ResponseBodyTextJson = NaturalPersonInfoResponseBaseResponseSchema
SchemaFor200ResponseBodyTextPlain = NaturalPersonInfoResponseBaseResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: NaturalPersonInfoResponseBaseResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: NaturalPersonInfoResponseBaseResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
    },
)
SchemaFor401ResponseBodyApplicationJson = BaseResponseSchema
SchemaFor401ResponseBodyTextJson = BaseResponseSchema
SchemaFor401ResponseBodyTextPlain = BaseResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: BaseResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: BaseResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyTextJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor401ResponseBodyTextPlain),
    },
)
SchemaFor404ResponseBodyApplicationJson = BaseResponseSchema
SchemaFor404ResponseBodyTextJson = BaseResponseSchema
SchemaFor404ResponseBodyTextPlain = BaseResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: BaseResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: BaseResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextPlain),
    },
)
SchemaFor500ResponseBodyApplicationJson = BaseResponseSchema
SchemaFor500ResponseBodyTextJson = BaseResponseSchema
SchemaFor500ResponseBodyTextPlain = BaseResponseSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: BaseResponse


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: BaseResponse


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextPlain),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '401': _response_for_401,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
    'text/plain',
)


class BaseApi(api_client.Api):

    def _update_information_mapped_args(
        self,
        natural_person_id: int,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        tax_id: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        middle_name: typing.Optional[typing.Optional[str]] = None,
        legal_name: typing.Optional[typing.Optional[str]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[EGender] = None,
        country_birth: typing.Optional[typing.Optional[str]] = None,
        country_residence: typing.Optional[typing.Optional[str]] = None,
        country_main_business: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        email_two: typing.Optional[typing.Optional[str]] = None,
        mobile_phone: typing.Optional[typing.Optional[str]] = None,
        mobile_phone_two: typing.Optional[typing.Optional[str]] = None,
        automatically_update_np_risk: typing.Optional[typing.Optional[bool]] = None,
        risk_level: typing.Optional[EScore] = None,
        risk_level_justification: typing.Optional[typing.Optional[str]] = None,
        is_flagged: typing.Optional[bool] = None,
        comments: typing.Optional[typing.Optional[str]] = None,
        economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if client_reference_id is not None:
            _body["clientReferenceId"] = client_reference_id
        if tax_id is not None:
            _body["taxId"] = tax_id
        if first_name is not None:
            _body["firstName"] = first_name
        if last_name is not None:
            _body["lastName"] = last_name
        if middle_name is not None:
            _body["middleName"] = middle_name
        if legal_name is not None:
            _body["legalName"] = legal_name
        if date_of_birth is not None:
            _body["dateOfBirth"] = date_of_birth
        if gender is not None:
            _body["gender"] = gender
        if country_birth is not None:
            _body["countryBirth"] = country_birth
        if country_residence is not None:
            _body["countryResidence"] = country_residence
        if country_main_business is not None:
            _body["countryMainBusiness"] = country_main_business
        if nationality is not None:
            _body["nationality"] = nationality
        if email is not None:
            _body["email"] = email
        if email_two is not None:
            _body["emailTwo"] = email_two
        if mobile_phone is not None:
            _body["mobilePhone"] = mobile_phone
        if mobile_phone_two is not None:
            _body["mobilePhoneTwo"] = mobile_phone_two
        if automatically_update_np_risk is not None:
            _body["automaticallyUpdateNPRisk"] = automatically_update_np_risk
        if risk_level is not None:
            _body["riskLevel"] = risk_level
        if risk_level_justification is not None:
            _body["riskLevelJustification"] = risk_level_justification
        if is_flagged is not None:
            _body["isFlagged"] = is_flagged
        if comments is not None:
            _body["comments"] = comments
        if economic_profile is not None:
            _body["economicProfile"] = economic_profile
        args.body = _body
        if natural_person_id is not None:
            _path_params["naturalPersonId"] = natural_person_id
        args.path = _path_params
        return args

    async def _aupdate_information_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_natural_person_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/NaturalPerson/{naturalPersonId}/updateInfo',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_natural_person_info_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_information_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_natural_person_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/NaturalPerson/{naturalPersonId}/updateInfo',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_natural_person_info_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateInformationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_information(
        self,
        natural_person_id: int,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        tax_id: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        middle_name: typing.Optional[typing.Optional[str]] = None,
        legal_name: typing.Optional[typing.Optional[str]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[EGender] = None,
        country_birth: typing.Optional[typing.Optional[str]] = None,
        country_residence: typing.Optional[typing.Optional[str]] = None,
        country_main_business: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        email_two: typing.Optional[typing.Optional[str]] = None,
        mobile_phone: typing.Optional[typing.Optional[str]] = None,
        mobile_phone_two: typing.Optional[typing.Optional[str]] = None,
        automatically_update_np_risk: typing.Optional[typing.Optional[bool]] = None,
        risk_level: typing.Optional[EScore] = None,
        risk_level_justification: typing.Optional[typing.Optional[str]] = None,
        is_flagged: typing.Optional[bool] = None,
        comments: typing.Optional[typing.Optional[str]] = None,
        economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_information_mapped_args(
            natural_person_id=natural_person_id,
            client_reference_id=client_reference_id,
            tax_id=tax_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            legal_name=legal_name,
            date_of_birth=date_of_birth,
            gender=gender,
            country_birth=country_birth,
            country_residence=country_residence,
            country_main_business=country_main_business,
            nationality=nationality,
            email=email,
            email_two=email_two,
            mobile_phone=mobile_phone,
            mobile_phone_two=mobile_phone_two,
            automatically_update_np_risk=automatically_update_np_risk,
            risk_level=risk_level,
            risk_level_justification=risk_level_justification,
            is_flagged=is_flagged,
            comments=comments,
            economic_profile=economic_profile,
        )
        return await self._aupdate_information_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_information(
        self,
        natural_person_id: int,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        tax_id: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        middle_name: typing.Optional[typing.Optional[str]] = None,
        legal_name: typing.Optional[typing.Optional[str]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[EGender] = None,
        country_birth: typing.Optional[typing.Optional[str]] = None,
        country_residence: typing.Optional[typing.Optional[str]] = None,
        country_main_business: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        email_two: typing.Optional[typing.Optional[str]] = None,
        mobile_phone: typing.Optional[typing.Optional[str]] = None,
        mobile_phone_two: typing.Optional[typing.Optional[str]] = None,
        automatically_update_np_risk: typing.Optional[typing.Optional[bool]] = None,
        risk_level: typing.Optional[EScore] = None,
        risk_level_justification: typing.Optional[typing.Optional[str]] = None,
        is_flagged: typing.Optional[bool] = None,
        comments: typing.Optional[typing.Optional[str]] = None,
        economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_information_mapped_args(
            natural_person_id=natural_person_id,
            client_reference_id=client_reference_id,
            tax_id=tax_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            legal_name=legal_name,
            date_of_birth=date_of_birth,
            gender=gender,
            country_birth=country_birth,
            country_residence=country_residence,
            country_main_business=country_main_business,
            nationality=nationality,
            email=email,
            email_two=email_two,
            mobile_phone=mobile_phone,
            mobile_phone_two=mobile_phone_two,
            automatically_update_np_risk=automatically_update_np_risk,
            risk_level=risk_level,
            risk_level_justification=risk_level_justification,
            is_flagged=is_flagged,
            comments=comments,
            economic_profile=economic_profile,
        )
        return self._update_information_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateInformation(BaseApi):

    async def aupdate_information(
        self,
        natural_person_id: int,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        tax_id: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        middle_name: typing.Optional[typing.Optional[str]] = None,
        legal_name: typing.Optional[typing.Optional[str]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[EGender] = None,
        country_birth: typing.Optional[typing.Optional[str]] = None,
        country_residence: typing.Optional[typing.Optional[str]] = None,
        country_main_business: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        email_two: typing.Optional[typing.Optional[str]] = None,
        mobile_phone: typing.Optional[typing.Optional[str]] = None,
        mobile_phone_two: typing.Optional[typing.Optional[str]] = None,
        automatically_update_np_risk: typing.Optional[typing.Optional[bool]] = None,
        risk_level: typing.Optional[EScore] = None,
        risk_level_justification: typing.Optional[typing.Optional[str]] = None,
        is_flagged: typing.Optional[bool] = None,
        comments: typing.Optional[typing.Optional[str]] = None,
        economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = None,
        validate: bool = False,
        **kwargs,
    ) -> NaturalPersonInfoResponseBaseResponsePydantic:
        raw_response = await self.raw.aupdate_information(
            natural_person_id=natural_person_id,
            client_reference_id=client_reference_id,
            tax_id=tax_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            legal_name=legal_name,
            date_of_birth=date_of_birth,
            gender=gender,
            country_birth=country_birth,
            country_residence=country_residence,
            country_main_business=country_main_business,
            nationality=nationality,
            email=email,
            email_two=email_two,
            mobile_phone=mobile_phone,
            mobile_phone_two=mobile_phone_two,
            automatically_update_np_risk=automatically_update_np_risk,
            risk_level=risk_level,
            risk_level_justification=risk_level_justification,
            is_flagged=is_flagged,
            comments=comments,
            economic_profile=economic_profile,
            **kwargs,
        )
        if validate:
            return NaturalPersonInfoResponseBaseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(NaturalPersonInfoResponseBaseResponsePydantic, raw_response.body)
    
    
    def update_information(
        self,
        natural_person_id: int,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        tax_id: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        middle_name: typing.Optional[typing.Optional[str]] = None,
        legal_name: typing.Optional[typing.Optional[str]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[EGender] = None,
        country_birth: typing.Optional[typing.Optional[str]] = None,
        country_residence: typing.Optional[typing.Optional[str]] = None,
        country_main_business: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        email_two: typing.Optional[typing.Optional[str]] = None,
        mobile_phone: typing.Optional[typing.Optional[str]] = None,
        mobile_phone_two: typing.Optional[typing.Optional[str]] = None,
        automatically_update_np_risk: typing.Optional[typing.Optional[bool]] = None,
        risk_level: typing.Optional[EScore] = None,
        risk_level_justification: typing.Optional[typing.Optional[str]] = None,
        is_flagged: typing.Optional[bool] = None,
        comments: typing.Optional[typing.Optional[str]] = None,
        economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = None,
        validate: bool = False,
    ) -> NaturalPersonInfoResponseBaseResponsePydantic:
        raw_response = self.raw.update_information(
            natural_person_id=natural_person_id,
            client_reference_id=client_reference_id,
            tax_id=tax_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            legal_name=legal_name,
            date_of_birth=date_of_birth,
            gender=gender,
            country_birth=country_birth,
            country_residence=country_residence,
            country_main_business=country_main_business,
            nationality=nationality,
            email=email,
            email_two=email_two,
            mobile_phone=mobile_phone,
            mobile_phone_two=mobile_phone_two,
            automatically_update_np_risk=automatically_update_np_risk,
            risk_level=risk_level,
            risk_level_justification=risk_level_justification,
            is_flagged=is_flagged,
            comments=comments,
            economic_profile=economic_profile,
        )
        if validate:
            return NaturalPersonInfoResponseBaseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(NaturalPersonInfoResponseBaseResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        natural_person_id: int,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        tax_id: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        middle_name: typing.Optional[typing.Optional[str]] = None,
        legal_name: typing.Optional[typing.Optional[str]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[EGender] = None,
        country_birth: typing.Optional[typing.Optional[str]] = None,
        country_residence: typing.Optional[typing.Optional[str]] = None,
        country_main_business: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        email_two: typing.Optional[typing.Optional[str]] = None,
        mobile_phone: typing.Optional[typing.Optional[str]] = None,
        mobile_phone_two: typing.Optional[typing.Optional[str]] = None,
        automatically_update_np_risk: typing.Optional[typing.Optional[bool]] = None,
        risk_level: typing.Optional[EScore] = None,
        risk_level_justification: typing.Optional[typing.Optional[str]] = None,
        is_flagged: typing.Optional[bool] = None,
        comments: typing.Optional[typing.Optional[str]] = None,
        economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_information_mapped_args(
            natural_person_id=natural_person_id,
            client_reference_id=client_reference_id,
            tax_id=tax_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            legal_name=legal_name,
            date_of_birth=date_of_birth,
            gender=gender,
            country_birth=country_birth,
            country_residence=country_residence,
            country_main_business=country_main_business,
            nationality=nationality,
            email=email,
            email_two=email_two,
            mobile_phone=mobile_phone,
            mobile_phone_two=mobile_phone_two,
            automatically_update_np_risk=automatically_update_np_risk,
            risk_level=risk_level,
            risk_level_justification=risk_level_justification,
            is_flagged=is_flagged,
            comments=comments,
            economic_profile=economic_profile,
        )
        return await self._aupdate_information_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        natural_person_id: int,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        tax_id: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        middle_name: typing.Optional[typing.Optional[str]] = None,
        legal_name: typing.Optional[typing.Optional[str]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[EGender] = None,
        country_birth: typing.Optional[typing.Optional[str]] = None,
        country_residence: typing.Optional[typing.Optional[str]] = None,
        country_main_business: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        email_two: typing.Optional[typing.Optional[str]] = None,
        mobile_phone: typing.Optional[typing.Optional[str]] = None,
        mobile_phone_two: typing.Optional[typing.Optional[str]] = None,
        automatically_update_np_risk: typing.Optional[typing.Optional[bool]] = None,
        risk_level: typing.Optional[EScore] = None,
        risk_level_justification: typing.Optional[typing.Optional[str]] = None,
        is_flagged: typing.Optional[bool] = None,
        comments: typing.Optional[typing.Optional[str]] = None,
        economic_profile: typing.Optional[UpdateNaturalPersonEconomicProfileRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_information_mapped_args(
            natural_person_id=natural_person_id,
            client_reference_id=client_reference_id,
            tax_id=tax_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            legal_name=legal_name,
            date_of_birth=date_of_birth,
            gender=gender,
            country_birth=country_birth,
            country_residence=country_residence,
            country_main_business=country_main_business,
            nationality=nationality,
            email=email,
            email_two=email_two,
            mobile_phone=mobile_phone,
            mobile_phone_two=mobile_phone_two,
            automatically_update_np_risk=automatically_update_np_risk,
            risk_level=risk_level,
            risk_level_justification=risk_level_justification,
            is_flagged=is_flagged,
            comments=comments,
            economic_profile=economic_profile,
        )
        return self._update_information_oapg(
            body=args.body,
            path_params=args.path,
        )

