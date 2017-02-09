from . import Command, addCmd


class GetChatMessages(Command):
    name = "getChatMessages.view"
    param_defs = {"since": {}}
    dbsess = True


    def handleReq(self, session):
        return self.makeResp()


addCmd(GetChatMessages)
