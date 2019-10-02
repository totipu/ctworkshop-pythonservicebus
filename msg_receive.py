from azure.servicebus import ServiceBusService
from azure.servicebus import Message

sbs = ServiceBusService(
    service_namespace='SERVICEBUS_NAMESPACE', # namespace name as created on Azure portal
    shared_access_key_name='SHARED_ACCESS_POLICY_NAME', # Shared Access Policy name as created on Azure portal
    shared_access_key_value='SHARED_ACCESS_POLICY_KEY') # Shared Access Policy Key

while True :
    msg = sbs.receive_subscription_message('SERVICE_BUS_TOPIC', 'SERVICEBUS_SUBSCRIPTION_1', peek_lock=False)
    print(msg.body)