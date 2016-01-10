from FuelSDK.rest import ET_CUDSupportRest


########
##
##  wrap an Exact Target Push Message
##
########
class ET_PushMessage(ET_CUDSupportRest):
    def __init__(self):
        super(ET_PushMessage, self).__init__()
        self.endpoint = 'https://www.exacttargetapis.com/push/v1/message/{id}'
        self.urlProps = ["id"]
        self.urlPropsRequired = []


########
##
##  wrap an Exact Target Push Message Contact and Deliveries
##
########
class ET_PushMessageContact(ET_CUDSupportRest):
    def __init__(self):
        super(ET_PushMessageContact, self).__init__()
        self.endpoint = 'https://www.exacttargetapis.com/push/v1/messageContact/{messageId}/send'
        self.urlProps = ["messageId"]
        self.urlPropsRequired = []


class ET_PushMessageContact_Deliveries(ET_CUDSupportRest):
    def __init__(self):
        super(ET_PushMessageContact_Deliveries, self).__init__()
        self.endpoint = 'https://www.exacttargetapis.com/push/v1/messageContact/{messageId}/deliveries/{tokenId}'
        self.urlProps = ["messageId", "tokenId"]
        self.urlPropsRequired = []


########
##
##  wrap an Exact Target Interaction Events
##
########
class ET_InteractionEvents(ET_CUDSupportRest):
    def __init__(self):
        super(ET_InteractionEvents, self).__init__()
        self.endpoint = 'https://www.exacttargetapis.com/interaction/v1/events'
        self.urlProps = []
        self.urlPropsRequired = []
