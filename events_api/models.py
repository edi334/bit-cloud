from pydantic import BaseModel


class Time(BaseModel):
    a: int
    m: int


class Device(BaseModel):
    id: str
    os: str


class File(BaseModel):
    file_hash: str
    file_path: str
    time: Time


class LastAccess(BaseModel):
    hash: str
    path: str
    pid: str


class Event(BaseModel):
    device: Device
    file: File
    last_access: LastAccess


class BaseResponse(BaseModel):
    hash: str
    risk_level: int


class Response(BaseModel):
    file: BaseResponse
    process: BaseResponse
