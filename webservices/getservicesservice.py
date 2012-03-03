from protorpc import messages
from protorpc import remote

import xml.etree.ElementTree as ET

import baseservice
import logging

class Service(messages.Message):
    serviceName = messages.StringField(1, required = True)
    serviceAlias = messages.StringField(2, required = False)
    productName = messages.StringField(3, required = True)
    isUsageAvailable = messages.BooleanField(4, required = True)
    narrative = messages.StringField(5, required = False)

class GetServicesRequest(messages.Message):
    userName = messages.StringField(1, required = True)
    password = messages.StringField(2, required = True)
    userToken = messages.StringField(3, required = True)
    clientToken = messages.StringField(4, required = True)

class GetServicesResponse(messages.Message):
    userName = messages.StringField(1, required = True)
    success = messages.BooleanField(2, required = True)
    services = messages.MessageField(Service, 3, repeated = True)

class GetServicesService(baseservice.BaseService):
    def __init__(self):
        logging.info("GetServicesService::ctor called")
        super(GetServicesService, self).__init__("GetAuthorisedBroadbandAccounts")

    @remote.method(GetServicesRequest, GetServicesResponse)
    def getservices(self, request):
        logging.info("GetServicesService::getservices called")

        # Handle test request
        if self.is_test_request(request):
            return self.generate_test_response(request);

        # Set common credentials
        self.set_credentials(request.userName, request.password)

        # Add service-specific parameters
        self.parameters["AuthenticationGUID"] = request.userToken
        self.parameters["ClientValidationGUID"] = request.clientToken

        response_str = baseservice.BaseService.send_request(self)
        xml = ET.fromstring(response_str)

        serviceNameElems = xml.findall(".//{https://webservices.zen.co.uk/broadband/v3.11/}DSLUsername")
        serviceAliasElems = xml.findall(".//{https://webservices.zen.co.uk/broadband/v3.11/}AliasName")
        productNameElems = xml.findall(".//{https://webservices.zen.co.uk/broadband/v3.11/}ProductName")
        isUsageAvailableElems = xml.findall(".//{https://webservices.zen.co.uk/broadband/v3.11/}IsUsageInformationAvailable")
        narrativeElems = xml.findall(".//{https://webservices.zen.co.uk/broadband/v3.11/}Message")

        # We depend on this assertion later
        assert \
            len(serviceNameElems) == \
            len(serviceAliasElems) == \
            len(productNameElems) == \
            len(isUsageAvailableElems) == \
            len(narrativeElems)

        # TODO: get other repeating fields and ensure all same length

        services = []

        if len(serviceNameElems) > 0:
            for i in range(len(serviceNameElems)):
                logging.info("GetServicesService %s" % serviceNameElems[i])

                service = Service()

                service.serviceName = serviceNameElems[i].text
                service.serviceAlias = serviceAliasElems[i].text
                service.productName = productNameElems[i].text
                service.isUsageAvailable = self.from_boolean(isUsageAvailableElems[i].text)
                service.narrative = narrativeElems[i].text

                services.append(service)

        success = True

        response = GetServicesResponse()

        response.services = services
        response.userName = request.userName
        response.success = success

        return response

    def generate_test_response(self, request):
        services = []

        service = Service()

        service.serviceName = "serviceName"
        service.serviceAlias = "serviceAlias"
        service.productName = "productName"
        service.isUsageAvailable = True
        service.narrative = None

        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)
        services.append(service)

        success = True

        response = GetServicesResponse()

        response.services = services
        response.userName = request.userName
        response.success = success

        return response
