# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from proovid_python_sdk.paths.api_health_version.get import GetVersion
from proovid_python_sdk.paths.api_health_status.get import StatusCheck
from proovid_python_sdk.apis.tags.health_api_raw import HealthApiRaw


class HealthApi(
    GetVersion,
    StatusCheck,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: HealthApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = HealthApiRaw(api_client)
