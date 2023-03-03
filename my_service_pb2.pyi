from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Anime(_message.Message):
    __slots__ = ["date", "score", "sfw", "title"]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SFW_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    date: str
    score: float
    sfw: bool
    title: str
    def __init__(self, title: _Optional[str] = ..., score: _Optional[float] = ..., sfw: bool = ..., date: _Optional[str] = ...) -> None: ...

class AnimeTitle(_message.Message):
    __slots__ = ["title"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class MathRequest(_message.Message):
    __slots__ = ["op", "x", "y"]
    OP_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    op: str
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., op: _Optional[str] = ...) -> None: ...

class MathResponse(_message.Message):
    __slots__ = ["ans"]
    ANS_FIELD_NUMBER: _ClassVar[int]
    ans: str
    def __init__(self, ans: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["date", "msg", "to"]
    DATE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    date: str
    msg: str
    to: str
    def __init__(self, to: _Optional[str] = ..., msg: _Optional[str] = ..., date: _Optional[str] = ..., **kwargs) -> None: ...

class Number(_message.Message):
    __slots__ = ["x"]
    X_FIELD_NUMBER: _ClassVar[int]
    x: int
    def __init__(self, x: _Optional[int] = ...) -> None: ...
