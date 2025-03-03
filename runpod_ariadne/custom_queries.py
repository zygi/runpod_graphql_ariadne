# Generated by ariadne-codegen

from typing import Any, Dict, Optional

from .custom_fields import CpuTypeFields, GpuTypeFields, PodFields, UserFields
from .input_types import GpuTypeFilter, PodFilter


class Query:
    @classmethod
    def cpu_types(cls) -> CpuTypeFields:
        return CpuTypeFields(field_name="cpuTypes")

    @classmethod
    def gpu_types(cls, *, input: Optional[GpuTypeFilter] = None) -> GpuTypeFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "GpuTypeFilter", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return GpuTypeFields(field_name="gpuTypes", arguments=cleared_arguments)

    @classmethod
    def myself(cls) -> UserFields:
        return UserFields(field_name="myself")

    @classmethod
    def pod(cls, *, input: Optional[PodFilter] = None) -> PodFields:
        arguments: Dict[str, Dict[str, Any]] = {
            "input": {"type": "PodFilter", "value": input}
        }
        cleared_arguments = {
            key: value for key, value in arguments.items() if value["value"] is not None
        }
        return PodFields(field_name="pod", arguments=cleared_arguments)
