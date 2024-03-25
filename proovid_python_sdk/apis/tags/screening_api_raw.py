# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from proovid_python_sdk.paths.api_screening_aml_report_reference.get import GetAmlReportRaw
from proovid_python_sdk.paths.api_screening_natural_person_id.get import GetNaturalPersonByIdRaw
from proovid_python_sdk.paths.api_screening_natural_person_id.delete import RemoveNaturalPersonRaw
from proovid_python_sdk.paths.api_screening_natural_person.post import SubmitNaturalPersonScreeningRaw


class ScreeningApiRaw(
    GetAmlReportRaw,
    GetNaturalPersonByIdRaw,
    RemoveNaturalPersonRaw,
    SubmitNaturalPersonScreeningRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
