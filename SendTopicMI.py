from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.identity import DefaultAzureCredential
import os

FULLY_QUALIFIED_NAMESPACE = os.environ['SERVICE_BUS_FULLY_QUALIFIED_NAMESPACE']
TOPIC_NAME = os.environ['SERVICE_BUS_TOPIC_NAME']

# get default credentials
credential = DefaultAzureCredential()

# create a Service Bus client using default credentials
servicebus_client = ServiceBusClient(FULLY_QUALIFIED_NAMESPACE, credential)

with servicebus_client:
    # get a Topic Sender object to send messages to the topic
    sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
    with sender:
        # send one message        
        message = ServiceBusMessage("This is message using Default Azure Credential")
        sender.send_messages(message)
        print("Sent a single message")

#print("Done sending messages")
print("-----------------------")