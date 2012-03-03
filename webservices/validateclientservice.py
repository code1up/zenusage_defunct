from protorpc import messages
from protorpc import remote

import xml.etree.ElementTree as ET

import baseservice
import logging

class ValidateClientRequest(messages.Message):
    userName = messages.StringField(1, required = True)
    password = messages.StringField(2, required = True)
    userToken = messages.StringField(3, required = True)
    version = messages.StringField(4, required = True)
    clientName = messages.StringField(5, required = True)
    isBeta = messages.BooleanField(6, required = True)

class ValidateClientResponse(messages.Message):
    success = messages.BooleanField(1, required = True)
    userName = messages.StringField(2, required = True)
    clientToken = messages.StringField(3, required = False)

class ValidateClientService(baseservice.BaseService):
    def __init__(self):
        logging.info("ValidateClientService::ctor called")
        super(ValidateClientService, self).__init__("ValidateClient")

    @remote.method(ValidateClientRequest, ValidateClientResponse)
    def validateclient(self, request):
        logging.info("ValidateClientRequest::validateclient called")

        # Handle test request
        if self.is_test_request(request):
            return self.generate_test_response(request)

        # Set common credentials
        self.set_credentials(request.userName, request.password)

        # Add service-specific parameters
        self.parameters["AuthenticationGUID"] = request.userToken
        self.parameters["ClientVersion"] = request.version
        self.parameters["ClientName"] = request.clientName
        self.parameters["ClientIsBeta"] = self.to_boolean(request.isBeta)

        response_str = baseservice.BaseService.send_request(self)
        xml = ET.fromstring(response_str)

        elem = xml.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}ValidateClientResult")

        if elem == None:
            # TODO: look for error
            clientToken = None
            success = False

        else:
            clientToken = elem.text
            logging.info("ValidateClientResult %s" % clientToken)
            success = True

        response = ValidateClientResponse()

        response.userName = request.userName
        response.clientToken = clientToken
        response.success = success

        return response

    def generate_test_response(self, request):
        response = ValidateClientResponse()

        response.userName = request.userName
        response.clientToken = "AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE"
        response.success = True

        return response
