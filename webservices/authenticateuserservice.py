from protorpc import messages
from protorpc import remote

import xml.etree.ElementTree as ET

from webservices import baseservice
import logging

class AuthenticateUserRequest(messages.Message):
    userName = messages.StringField(1, required = True)
    password = messages.StringField(2, required = True)

class AuthenticateUserResponse(messages.Message):
    success = messages.BooleanField(1, required = True)
    errorCode = messages.StringField(2, required = False)
    errorMessage = messages.StringField(3, required = False)
    userName = messages.StringField(4, required = False)
    userToken = messages.StringField(5, required = False)

class AuthenticateUserService(baseservice.BaseService):
    def __init__(self):
        logging.info("AuthenticateUserService::ctor called")
        super(AuthenticateUserService, self).__init__("Authenticate")

    @remote.method(AuthenticateUserRequest, AuthenticateUserResponse)
    def authenticateuser(self, request):
        logging.info("AuthenticateUserRequest::authenticateuser called")

        # Handle test request
        if self.is_test_request(request):
            return self.generate_test_response(request);

        # Set common credentials
        self.set_credentials(request.userName, request.password)

        # NOTE: no service-specific parameters

        response_str = baseservice.BaseService.send_request(self)
        xml = ET.fromstring(response_str)

        elem = xml.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}AuthenticateResult")

        if elem == None:
            # TODO: look for error
            userToken = None
            success = False

        else:
            userToken = elem.text
            logging.info("userToken %s" % userToken)
            success = True

        response = AuthenticateUserResponse()

        response.userName = request.userName
        response.userToken = userToken
        response.success = success

        return response

    def generate_test_response(self, request):
        response = AuthenticateUserResponse()

        response.userName = request.userName
        response.userToken = "11111111-2222-3333-4444-555555555555"
        response.success = True

        return response
