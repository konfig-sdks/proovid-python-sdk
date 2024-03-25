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

from proovid_python_sdk.model.add_natural_person_request import AddNaturalPersonRequest as AddNaturalPersonRequestSchema
from proovid_python_sdk.model.add_natural_person_response_base_response import AddNaturalPersonResponseBaseResponse as AddNaturalPersonResponseBaseResponseSchema
from proovid_python_sdk.model.natural_person_documents_request import NaturalPersonDocumentsRequest as NaturalPersonDocumentsRequestSchema
from proovid_python_sdk.model.base_response import BaseResponse as BaseResponseSchema
from proovid_python_sdk.model.add_natural_person_info_request import AddNaturalPersonInfoRequest as AddNaturalPersonInfoRequestSchema

from proovid_python_sdk.type.base_response import BaseResponse
from proovid_python_sdk.type.add_natural_person_response_base_response import AddNaturalPersonResponseBaseResponse
from proovid_python_sdk.type.natural_person_documents_request import NaturalPersonDocumentsRequest
from proovid_python_sdk.type.add_natural_person_request import AddNaturalPersonRequest
from proovid_python_sdk.type.add_natural_person_info_request import AddNaturalPersonInfoRequest

from ...api_client import Dictionary
from proovid_python_sdk.pydantic.base_response import BaseResponse as BaseResponsePydantic
from proovid_python_sdk.pydantic.add_natural_person_response_base_response import AddNaturalPersonResponseBaseResponse as AddNaturalPersonResponseBaseResponsePydantic
from proovid_python_sdk.pydantic.add_natural_person_info_request import AddNaturalPersonInfoRequest as AddNaturalPersonInfoRequestPydantic
from proovid_python_sdk.pydantic.natural_person_documents_request import NaturalPersonDocumentsRequest as NaturalPersonDocumentsRequestPydantic
from proovid_python_sdk.pydantic.add_natural_person_request import AddNaturalPersonRequest as AddNaturalPersonRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = AddNaturalPersonRequestSchema
SchemaForRequestBodyTextJson = AddNaturalPersonRequestSchema
SchemaForRequestBodyApplicationJsonPatchjson = AddNaturalPersonRequestSchema
SchemaForRequestBodyApplicationJson = AddNaturalPersonRequestSchema


request_body_add_natural_person_request = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = AddNaturalPersonResponseBaseResponseSchema
SchemaFor200ResponseBodyTextJson = AddNaturalPersonResponseBaseResponseSchema
SchemaFor200ResponseBodyTextPlain = AddNaturalPersonResponseBaseResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AddNaturalPersonResponseBaseResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AddNaturalPersonResponseBaseResponse


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
SchemaFor400ResponseBodyApplicationJson = BaseResponseSchema
SchemaFor400ResponseBodyTextJson = BaseResponseSchema
SchemaFor400ResponseBodyTextPlain = BaseResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: BaseResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: BaseResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextPlain),
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
    '400': _response_for_400,
    '401': _response_for_401,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
    'text/plain',
)


class BaseApi(api_client.Api):

    def _create_or_update_mapped_args(
        self,
        info: typing.Optional[AddNaturalPersonInfoRequest] = None,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        documents: typing.Optional[NaturalPersonDocumentsRequest] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if info is not None:
            _body["info"] = info
        if client_reference_id is not None:
            _body["clientReferenceId"] = client_reference_id
        if documents is not None:
            _body["documents"] = documents
        args.body = _body
        return args

    async def _acreate_or_update_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
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
            path_template='/api/NaturalPerson',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_add_natural_person_request.serialize(body, content_type)
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


    def _create_or_update_oapg(
        self,
        body: typing.Any = None,
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
        used_path = path.value
    
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
            path_template='/api/NaturalPerson',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_add_natural_person_request.serialize(body, content_type)
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


class CreateOrUpdateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_or_update(
        self,
        info: typing.Optional[AddNaturalPersonInfoRequest] = None,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        documents: typing.Optional[NaturalPersonDocumentsRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_or_update_mapped_args(
            info=info,
            client_reference_id=client_reference_id,
            documents=documents,
        )
        return await self._acreate_or_update_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_or_update(
        self,
        info: typing.Optional[AddNaturalPersonInfoRequest] = None,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        documents: typing.Optional[NaturalPersonDocumentsRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_or_update_mapped_args(
            info=info,
            client_reference_id=client_reference_id,
            documents=documents,
        )
        return self._create_or_update_oapg(
            body=args.body,
        )

class CreateOrUpdate(BaseApi):

    async def acreate_or_update(
        self,
        info: typing.Optional[AddNaturalPersonInfoRequest] = None,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        documents: typing.Optional[NaturalPersonDocumentsRequest] = None,
        validate: bool = False,
        **kwargs,
    ) -> AddNaturalPersonResponseBaseResponsePydantic:
        raw_response = await self.raw.acreate_or_update(
            info=info,
            client_reference_id=client_reference_id,
            documents=documents,
            **kwargs,
        )
        if validate:
            return AddNaturalPersonResponseBaseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AddNaturalPersonResponseBaseResponsePydantic, raw_response.body)
    
    
    def create_or_update(
        self,
        info: typing.Optional[AddNaturalPersonInfoRequest] = None,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        documents: typing.Optional[NaturalPersonDocumentsRequest] = None,
        validate: bool = False,
    ) -> AddNaturalPersonResponseBaseResponsePydantic:
        raw_response = self.raw.create_or_update(
            info=info,
            client_reference_id=client_reference_id,
            documents=documents,
        )
        if validate:
            return AddNaturalPersonResponseBaseResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AddNaturalPersonResponseBaseResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        info: typing.Optional[AddNaturalPersonInfoRequest] = None,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        documents: typing.Optional[NaturalPersonDocumentsRequest] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_or_update_mapped_args(
            info=info,
            client_reference_id=client_reference_id,
            documents=documents,
        )
        return await self._acreate_or_update_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        info: typing.Optional[AddNaturalPersonInfoRequest] = None,
        client_reference_id: typing.Optional[typing.Optional[str]] = None,
        documents: typing.Optional[NaturalPersonDocumentsRequest] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_or_update_mapped_args(
            info=info,
            client_reference_id=client_reference_id,
            documents=documents,
        )
        return self._create_or_update_oapg(
            body=args.body,
        )

