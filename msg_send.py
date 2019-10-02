from azure.servicebus import ServiceBusService
from azure.servicebus import Message

sbs = ServiceBusService(
    service_namespace='SERVICEBUS_NAMESPACE', # namespace name as created on Azure portal
    shared_access_key_name='SHARED_ACCESS_POLICY_NAME', # Shared Access Policy name as created on Azure portal
    shared_access_key_value='SHARED_ACCESS_POLICY_KEY') # Shared Access Policy Key

# implementirati logiku ponavljanja s unosom poruke s tipkovnice
while True:
    poruka = input("Vaša poruka: ")
    msg = Message(poruka)
    sbs.send_topic_message('SERVICE_BUS_TOPIC', msg) # topic name as created on Azure portal