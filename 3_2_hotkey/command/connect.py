from application.telecom import Telecom
from command.command import Command


class Connect(Command):

    def __init__(self, telecom: Telecom):
        super().__init__()
        self.telecom = telecom

    def __str__(self):
        return "ConnectTelecom"

    def execute(self):
        self.telecom.connect()

    def undo(self):
        self.telecom.disconnect()