import datetime

from . import Command, addCmd, playable_id_t, MissingParam
from ...models import rateItem


class Star(Command):
    name = "star.view"
    param_defs = {
        "id": {"type": playable_id_t},
        "albumId": {"type": playable_id_t},
        "artistId": {"type": playable_id_t},
        }
    dbsess = True


    def handleReq(self, session):
        if self.params["id"]:
            id = self.params["id"]
        elif self.params["albumId"]:
            id = self.params["albumId"]
        elif self.params["artistId"]:
            id = self.params["artistId"]
        else:
            raise MissingParam("Missing a valid id parameter")

        rateItem(session, self.req.authed_user.id, id,
                 starred=datetime.datetime.now())
        return self.makeResp()


addCmd(Star)
