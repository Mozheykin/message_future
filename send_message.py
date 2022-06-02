from email import message
from typing import NamedTuple

class Messages(NamedTuple):
    from_: str
    message: str



class SendMessage:
    def send(self,  message: Messages) -> None:
        raise NotImplementedError


class SendMessageEmail(SendMessage):
    def send(self,  message: Messages) -> None:
        pass
