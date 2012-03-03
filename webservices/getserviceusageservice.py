from protorpc import messages
from protorpc import remote

import xml.etree.ElementTree as ET

from webservices import baseservice
import logging

class GetServiceUsageRequest(messages.Message):
    userName = messages.StringField(1, required = True)
    password = messages.StringField(2, required = True)
    userToken = messages.StringField(3, required = True)
    clientToken = messages.StringField(4, required = True)
    serviceNames = messages.StringField(5, repeated = True)
    dateTimeFrom = messages.StringField(6, required = True)
    dateTimeTo = messages.StringField(7, required = True)

class ServiceUsage(messages.Message):
    dateTime = messages.StringField(1, required = True)
    year = messages.IntegerField(2, required = True)
    month = messages.IntegerField(3, required = True)
    source = messages.StringField(4, required = True)
    downloadUsage = messages.IntegerField(5, required = True)
    uploadUsage = messages.IntegerField(6, required = True)
    units = messages.StringField(7, required = True)

class ServiceStatistics(messages.Message):
    serviceName = messages.StringField(1, required = True)
    aliasName = messages.StringField(2, required = True)
    productName = messages.StringField(3, required = True)
    usageAllowance = messages.IntegerField(4, required = True)
    regradeAllowance = messages.IntegerField(5, required = True)
    bankAllowance = messages.IntegerField(6, required = True)
    monthlyAllowance = messages.IntegerField(7, required = True)
    statusCode = messages.StringField(8, required = True)
    liveServiceUsage = messages.MessageField(ServiceUsage, 9, required = False)
    historicalServiceUsages = messages.MessageField(ServiceUsage, 10, repeated = True)

class GetServiceUsageResponse(messages.Message):
    success = messages.BooleanField(1, required = True)
    errorCode = messages.StringField(2, required = False)
    errorMessage = messages.StringField(3, required = False)
    userName = messages.StringField(4, required = False)
    dateTimeFrom = messages.StringField(6, required = True)
    dateTimeTo = messages.StringField(7, required = True)
    statistics = messages.MessageField(ServiceStatistics, 8, repeated = True, required = False)

class GetServiceUsageService(baseservice.BaseService):
    def __init__(self):
        logging.info("GetServiceUsageService::ctor called")
        super(GetServiceUsageService, self).__init__("GetUsage")

    @remote.method(GetServiceUsageRequest, GetServiceUsageResponse)
    def getserviceusage(self, request):
        logging.info("GetServiceUsageService::getserviceusage called")

        # Set common credentials
        self.set_credentials(request.userName, request.password)

        # Append time and timezone to date parameters
        dateTimeFromFormat = "%sT00:00:00Z"
        dateTimeToFormat = "%sT23:59:59Z"

        dateTimeFrom = dateTimeFromFormat % request.dateTimeFrom
        dateTimeTo = dateTimeToFormat % request.dateTimeTo

        # Add service-specific parameters
        self.parameters["AuthenticationGUID"] = request.userToken
        self.parameters["ClientValidationGUID"] = request.clientToken
        self.parameters["adslAccounts"] = request.serviceNames
        self.parameters["dateTimeFrom"] = dateTimeFrom
        self.parameters["dateTimeTo"] = dateTimeTo

        response_str = baseservice.BaseService.send_request(self)
        xml = ET.fromstring(response_str)

        parentElems = xml.findall(".//{https://webservices.zen.co.uk/broadband/v3.11/}Statistic")

        response = GetServiceUsageResponse()

        if len(parentElems) == 0:
            # TODO: look for error / set error
            success = False

        else:
            for parentElem in parentElems:
                statistics = ServiceStatistics()

                # Statistic/BroadbandAccount
                logging.info("Statistic/BroadbandAccount")
                logging.info("\tServiceName=> %s" % parentElem.attrib["BroadbandAccount"])

                statistics.serviceName = parentElem.attrib["BroadbandAccount"]

                # Statistic/AdditionalDetails
                logging.info("Statistic/AdditionalDetails")
                elem = parentElem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}AdditionalDetails")

                # Statistic/AdditionalDetails/AllowanceDetails
                logging.info("Statistic/AdditionalDetails/AllowanceDetails")
                subelem = elem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}AllowanceDetails")

                logging.info("\tUsageAllowance => %s" % subelem.attrib["UsageAllowance"])
                logging.info("\tRegradeAllowance => %s" % subelem.attrib["RegradeAllowance"])
                logging.info("\tBankAllowance => %s" % subelem.attrib["BankAllowance"])
                logging.info("\tMonthlyAllowance => %s" % subelem.attrib["MonthlyAllowance"])
                logging.info("\tProductName => %s" % subelem.attrib["ProductName"])

                statistics.usageAllowance = int(subelem.attrib["UsageAllowance"])
                statistics.regradeAllowance = int(subelem.attrib["RegradeAllowance"])
                statistics.bankAllowance = int(subelem.attrib["BankAllowance"])
                statistics.monthlyAllowance = int(subelem.attrib["MonthlyAllowance"])
                statistics.productName = subelem.attrib["ProductName"]

                # Statistic/AdditionalDetails/AliasName
                logging.info("Statistic/AdditionalDetails/AliasName")
                elem = parentElem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}AliasName")
                logging.info("\tAliasName => %s" % elem.text)

                statistics.aliasName = elem.text

                # Statistic/AdditionalDetails/StatusCode
                logging.info("Statistic/AdditionalDetails/StatusCode")
                elem = parentElem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}StatusCode")
                logging.info("\tStatusCode => %s" % elem.text)

                statistics.statusCode = elem.text

                # Statistic/UsageStatistics
                for elem in parentElem.findall(".//{https://webservices.zen.co.uk/broadband/v3.11/}UsageStatistics"):
                    serviceUsage = ServiceUsage()

                    logging.info("Statistic/UsageStatistics")

                    logging.info("\tYear => %s" % elem.attrib["Year"])
                    logging.info("\tMonth => %s" % elem.attrib["Month"])
                    # logging.info("\tDateTime => %s" % elem.attrib["DateTime"])
                    logging.info("\tStatisticSource => %s" % elem.attrib["StatisticSource"])

                    serviceUsage.year = int(elem.attrib["Year"])
                    serviceUsage.month = int(elem.attrib["Month"])
                    serviceUsage.dateTime = elem.attrib["DateTime"]
                    serviceUsage.source = elem.attrib["StatisticSource"]

                    # Statistic/UsageStatistics/DownloadUsage
                    subelem = elem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}DownloadUsage")
                    logging.info("\tDownloadUsage => %s" % subelem.text)

                    serviceUsage.downloadUsage = int(subelem.text)

                    # Statistic/UsageStatistics/UploadUsage
                    subelem = elem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}UploadUsage")
                    logging.info("\tUploadUsage => %s" % subelem.text)

                    serviceUsage.uploadUsage = int(subelem.text)

                    # Statistic/UsageStatistics/SizeRepresentation
                    subelem = elem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}SizeRepresentation")
                    logging.info("\tSizeRepresentation => %s" % subelem.text)

                    serviceUsage.units = subelem.text

                    # Append service usage to live or historical statistics
                    if serviceUsage.source == "Live":
                        statistics.liveServiceUsage = serviceUsage

                    elif serviceUsage.source == "Historical":
                        statistics.historicalServiceUsages.append(serviceUsage)

                    else:
                        logging.warn("Unknown source: \"%s\"", source)

                # Statistic/DateTimeFrom
                logging.info("Statistic/DateTimeFrom")
                elem = parentElem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}DateTimeFrom")
                logging.info("\tDateTimeFrom => %s" % elem.text)

                # Statistic/DateTimeTo
                logging.info("Statistic/DateTimeTo")
                elem = parentElem.find(".//{https://webservices.zen.co.uk/broadband/v3.11/}DateTimeTo")
                logging.info("\tDateTimeTo => %s" % elem.text)

                # Append statistics to response
                response.statistics.append(statistics)

            success = True

        response.success = success
        response.errorCode = None
        response.errorMessage = None

        response.userName = request.userName
        response.dateTimeFrom = request.dateTimeFrom
        response.dateTimeTo = request.dateTimeTo

        if not response.success:
            response.statistics = None

        return response
