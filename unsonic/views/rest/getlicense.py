import xml.etree.ElementTree as ET

from . import Command, addCmd


class GetLicense(Command):
    name = "getLicense.view"
    param_defs = {}

    def handleReq(self):
        license = ET.Element("license")
        license.set("valid", "true")
        license.set("email", "foo@bar.com")
        license.set("key", "0" * 32)
        license.set("date", "2013-07-21T21:08:04")
        return self.makeResp(child=license)
        
        
addCmd(GetLicense)