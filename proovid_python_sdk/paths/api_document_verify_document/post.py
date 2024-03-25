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

from proovid_python_sdk.model.document_verification_response import DocumentVerificationResponse as DocumentVerificationResponseSchema
from proovid_python_sdk.model.document_verification_request import DocumentVerificationRequest as DocumentVerificationRequestSchema

from proovid_python_sdk.type.document_verification_request import DocumentVerificationRequest
from proovid_python_sdk.type.document_verification_response import DocumentVerificationResponse

from ...api_client import Dictionary
from proovid_python_sdk.pydantic.document_verification_request import DocumentVerificationRequest as DocumentVerificationRequestPydantic
from proovid_python_sdk.pydantic.document_verification_response import DocumentVerificationResponse as DocumentVerificationResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = DocumentVerificationRequestSchema
SchemaForRequestBodyTextJson = DocumentVerificationRequestSchema
SchemaForRequestBodyApplicationJsonPatchjson = DocumentVerificationRequestSchema
SchemaForRequestBodyApplicationJson = DocumentVerificationRequestSchema


request_body_document_verification_request = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = DocumentVerificationResponseSchema
SchemaFor200ResponseBodyTextJson = DocumentVerificationResponseSchema
SchemaFor200ResponseBodyTextPlain = DocumentVerificationResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DocumentVerificationResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DocumentVerificationResponse


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
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
    'text/json',
    'text/plain',
)


class BaseApi(api_client.Api):

    def _verify_status_0_mapped_args(
        self,
        email: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        document: typing.Optional[typing.Optional[str]] = None,
        additional_document: typing.Optional[typing.Optional[str]] = None,
        face: typing.Optional[typing.Optional[str]] = None,
        document_type: typing.Optional[typing.Optional[str]] = None,
        natural_person_id: typing.Optional[typing.Optional[int]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if email is not None:
            _body["email"] = email
        if country is not None:
            _body["country"] = country
        if document is not None:
            _body["document"] = document
        if additional_document is not None:
            _body["additionalDocument"] = additional_document
        if face is not None:
            _body["face"] = face
        if document_type is not None:
            _body["documentType"] = document_type
        if natural_person_id is not None:
            _body["naturalPersonId"] = natural_person_id
        args.body = _body
        return args

    async def _averify_status_0_oapg(
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
            path_template='/api/Document/VerifyDocument',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_document_verification_request.serialize(body, content_type)
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


    def _verify_status_0_oapg(
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
            path_template='/api/Document/VerifyDocument',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_document_verification_request.serialize(body, content_type)
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


class VerifyStatus0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def averify_status_0(
        self,
        email: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        document: typing.Optional[typing.Optional[str]] = None,
        additional_document: typing.Optional[typing.Optional[str]] = None,
        face: typing.Optional[typing.Optional[str]] = None,
        document_type: typing.Optional[typing.Optional[str]] = None,
        natural_person_id: typing.Optional[typing.Optional[int]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verify_status_0_mapped_args(
            email=email,
            country=country,
            document=document,
            additional_document=additional_document,
            face=face,
            document_type=document_type,
            natural_person_id=natural_person_id,
        )
        return await self._averify_status_0_oapg(
            body=args.body,
            **kwargs,
        )
    
    def verify_status_0(
        self,
        email: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        document: typing.Optional[typing.Optional[str]] = None,
        additional_document: typing.Optional[typing.Optional[str]] = None,
        face: typing.Optional[typing.Optional[str]] = None,
        document_type: typing.Optional[typing.Optional[str]] = None,
        natural_person_id: typing.Optional[typing.Optional[int]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verify_status_0_mapped_args(
            email=email,
            country=country,
            document=document,
            additional_document=additional_document,
            face=face,
            document_type=document_type,
            natural_person_id=natural_person_id,
        )
        return self._verify_status_0_oapg(
            body=args.body,
        )

class VerifyStatus0(BaseApi):

    async def averify_status_0(
        self,
        email: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        document: typing.Optional[typing.Optional[str]] = None,
        additional_document: typing.Optional[typing.Optional[str]] = None,
        face: typing.Optional[typing.Optional[str]] = None,
        document_type: typing.Optional[typing.Optional[str]] = None,
        natural_person_id: typing.Optional[typing.Optional[int]] = None,
        validate: bool = False,
        **kwargs,
    ) -> DocumentVerificationResponsePydantic:
        raw_response = await self.raw.averify_status_0(
            email=email,
            country=country,
            document=document,
            additional_document=additional_document,
            face=face,
            document_type=document_type,
            natural_person_id=natural_person_id,
            **kwargs,
        )
        if validate:
            return DocumentVerificationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DocumentVerificationResponsePydantic, raw_response.body)
    
    
    def verify_status_0(
        self,
        email: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        document: typing.Optional[typing.Optional[str]] = None,
        additional_document: typing.Optional[typing.Optional[str]] = None,
        face: typing.Optional[typing.Optional[str]] = None,
        document_type: typing.Optional[typing.Optional[str]] = None,
        natural_person_id: typing.Optional[typing.Optional[int]] = None,
        validate: bool = False,
    ) -> DocumentVerificationResponsePydantic:
        raw_response = self.raw.verify_status_0(
            email=email,
            country=country,
            document=document,
            additional_document=additional_document,
            face=face,
            document_type=document_type,
            natural_person_id=natural_person_id,
        )
        if validate:
            return DocumentVerificationResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DocumentVerificationResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        email: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        document: typing.Optional[typing.Optional[str]] = None,
        additional_document: typing.Optional[typing.Optional[str]] = None,
        face: typing.Optional[typing.Optional[str]] = None,
        document_type: typing.Optional[typing.Optional[str]] = None,
        natural_person_id: typing.Optional[typing.Optional[int]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verify_status_0_mapped_args(
            email=email,
            country=country,
            document=document,
            additional_document=additional_document,
            face=face,
            document_type=document_type,
            natural_person_id=natural_person_id,
        )
        return await self._averify_status_0_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        email: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        document: typing.Optional[typing.Optional[str]] = None,
        additional_document: typing.Optional[typing.Optional[str]] = None,
        face: typing.Optional[typing.Optional[str]] = None,
        document_type: typing.Optional[typing.Optional[str]] = None,
        natural_person_id: typing.Optional[typing.Optional[int]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verify_status_0_mapped_args(
            email=email,
            country=country,
            document=document,
            additional_document=additional_document,
            face=face,
            document_type=document_type,
            natural_person_id=natural_person_id,
        )
        return self._verify_status_0_oapg(
            body=args.body,
        )

