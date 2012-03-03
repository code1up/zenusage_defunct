from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from protorpc.webapp import service_handlers

from webservices import authenticateuserservice
from webservices import getservicesservice
from webservices import getserviceusageservice
from webservices import validateclientservice

# http://localhost:8080/webservices/authenticateuser/authenticateuserservice
# http://localhost:8080/webservices/authenticateuser/authenticateuser
# http://localhost:8080/protorpc/form

service_mappings = service_handlers.service_mapping([
    ("/webservices/user", authenticateuserservice.AuthenticateUserService),
    ("/webservices/client", validateclientservice.ValidateClientService),
    ("/webservices/services", getservicesservice.GetServicesService),
    ("/webservices/serviceusage", getserviceusageservice.GetServiceUsageService)
])

application = webapp.WSGIApplication(service_mappings, debug = True)

def main():
    util.run_wsgi_app(application)

if __name__ == "__main__":
    main()
