from typing import NamedTuple
from datetime import datetime


class Messages(NamedTuple):
    id_: int
    from_: str
    title: str
    message_: str
    when_send: datetime


class SendMessage:
    def send(self,  message: Messages) -> None:
        raise NotImplementedError


class SendMessageEmail(SendMessage):
    def send(self,  message: Messages) -> None:
        pass
