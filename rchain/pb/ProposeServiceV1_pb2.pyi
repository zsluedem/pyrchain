# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from .ServiceError_pb2 import (
    ServiceError as ServiceError_pb2___ServiceError,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ProposeResponse(google___protobuf___message___Message):
    result = ... # type: typing___Text

    @property
    def error(self) -> ServiceError_pb2___ServiceError: ...

    def __init__(self,
        *,
        error : typing___Optional[ServiceError_pb2___ServiceError] = None,
        result : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ProposeResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error",u"message",u"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",u"message",u"result"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"error",b"error",u"message",b"message",u"result",b"result"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"message",b"message"]) -> typing_extensions___Literal["error","result"]: ...