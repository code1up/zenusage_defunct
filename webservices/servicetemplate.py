from protorpc.messages import FieldList

import logging

class ServiceTemplate:
    def __init__(self, service):
        logging.info("ServiceTemplate::ctor called")

        self.template = """<soap:Envelope
           xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\"
           xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"
           xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"
           xmlns:wsa=\"http://schemas.xmlsoap.org/ws/2004/08/addressing\"
           xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\"
           xmlns:wsu=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd\">
           <soap:Header>
              <wsa:Action>https://webservices.zen.co.uk/broadbandstatistics/GetUsage</wsa:Action>
              <wsa:MessageID>urn:uuid:97fbd859-2a6e-4bc1-b201-92accf4828c3</wsa:MessageID>
              <wsa:ReplyTo>
                 <wsa:Address>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:Address>
              </wsa:ReplyTo>
              <wsa:To>https://webservices.zen.co.uk/broadband/v3.11/serviceengine.asmx</wsa:To>
              <wsse:Security soap:mustUnderstand=\"1\">
                 <wsse:UsernameToken wsu:Id=\"SecurityToken-3e12170e-c6b4-4546-bde6-d6fbfd00cc10\">
                    <wsse:Username>__username__</wsse:Username>
                    <wsse:Password Type=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText\">__password__</wsse:Password>
                 </wsse:UsernameToken>
              </wsse:Security>
           </soap:Header>
           <soap:Body>
              <__action__ xmlns=\"https://webservices.zen.co.uk/broadband/v3.11/\">
                 __parameters__
             </__action__>
           </soap:Body>
        </soap:Envelope>"""

        self.service = service

    def generate_request_str(self):
        logging.info("ServiceTemplate::generate_request_str called")

        xml = self.template

        # Action
        xml = xml.replace("__action__", self.service.action)

        # Credentials
        xml = xml.replace("__username__", self.service.username)
        xml = xml.replace("__password__", self.service.password)

        # Parameters
        parameters = ""

        format_key_open = "<%(k)s>"
        format_value = "%(v)s"
        format_key_close = "</%(k)s>"

        format_str = format_key_open + format_value + format_key_close

        for k, v in self.service.parameters.iteritems():
            logging.info("k: %s" % k)
            logging.info("v: %s" % v)

            logging.info("type(k): %s" % type(k))
            logging.info("type(v): %s" % type(v))

            if type(v) is str or type(v) is unicode:
                parameters += format_str % { "k": k, "v": v }

            elif type(v) is FieldList:
                parameters += format_key_open % { "k": k }

                for v2 in v:
                    # TODO: "string" key is hardcoded
                    parameters += format_str % { "k": "string", "v": v2 }
                    logging.info("----- v2: %s" % v2)
                    logging.info("----- type(v2): %s" % type(v2))

                parameters += format_key_close % { "k": k }

            else:
                logging.error("Unhandled parameter type: %s", type(v))

        xml = xml.replace("__parameters__", parameters)

        return xml
