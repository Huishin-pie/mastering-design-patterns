from application.telecom import Telecom
from command.command import Command


class Disconnect(Command):

    def __init__(self, telecom: Telecom):
        super().__init__()
        self.telecom = telecom

    def __str__(self):
        return "DisconnectTelecom"

    def execute(self):
        self.telecom.disconnect()

    def undo(self):
        self.telecom.connect()