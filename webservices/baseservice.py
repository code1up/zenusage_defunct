from protorpc import remote

import httplib
import socket

import xml.etree.ElementTree as ET

import servicetemplate
import logging

class BaseService(remote.Service):
    def __init__(self, action):
        logging.info("BaseService::ctor called, action %s" % action)

        # TODO: why?
        self.map_known_namespaces()

        self.action = action
        self.username = None
        self.password = None
        self.parameters = { }

        self.url = "webservices.zen.co.uk"
        self.path = "/broadband/v3.11/serviceengine.asmx"
        self.content_type = "text/xml; charset=\"UTF-8\""

    def is_test_request(self, request):
        return request.userName.endswith("@example.com")

    def set_credentials(self, username, password):
        logging.info("BaseService::set_credentials called, username %s" % username)

        self.username = username
        self.password = password

        self.parameters["username"] = username
        self.parameters["password"] = password

    def send_request(self):
        logging.info("BaseService::send_request called, action %(action)s, username %(username)s"
                % {"action": self.action, "username": self.username})

        template = servicetemplate.ServiceTemplate(self)
        request_str = template.generate_request_str()

        logging.info(request_str)

        webservice = httplib.HTTPS(self.url)

        webservice.putrequest("POST", self.path)
        webservice.putheader("content-type", self.content_type)
        webservice.endheaders()

        webservice.send(request_str)

        header = webservice.getreply()
        response_file = webservice.getfile()
        response_str = response_file.read()

        logging.info(header)
        logging.info(response_str)

        return response_str

    def map_known_namespaces(self):
        logging.info("BaseService::map_known_namespaces called")

        ET._namespace_map["http://schemas.xmlsoap.org/soap/envelope/"] = "soap"
        ET._namespace_map["http://www.w3.org/2001/XMLSchema-instance"] = "xsi"
        ET._namespace_map["http://www.w3.org/2001/XMLSchema"] = "xsd"
        ET._namespace_map["http://schemas.xmlsoap.org/ws/2004/08/addressing"] = "wsa"
        ET._namespace_map["http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"] = "wsse"
        ET._namespace_map["http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"] = "wsu"
        ET._namespace_map["https://webservices.zen.co.uk/broadband/v3.11/"] = "zen"

    def to_boolean(self, value):
        return str(value).lower()

    def from_boolean(self, value):
        return str(value).upper() == "TRUE"
