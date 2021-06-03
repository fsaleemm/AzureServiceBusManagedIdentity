from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.identity import AzureCliCredential, ManagedIdentityCredential, ChainedTokenCredential
import os

FULLY_QUALIFIED_NAMESPACE = os.environ['SERVICE_BUS_FULLY_QUALIFIED_NAMESPACE']
TOPIC_NAME = os.environ['SERVICE_BUS_TOPIC_NAME']

# get Azure CLI credentials
azure_cli = AzureCliCredential()

# get Managed Identity
managed_identity = ManagedIdentityCredential()

# Custom Authentication Flow
credential_chain = ChainedTokenCredential(managed_identity, azure_cli)

# create a Service Bus client using default credentials
servicebus_client = ServiceBusClient(FULLY_QUALIFIED_NAMESPACE, credential_chain)

with servicebus_client:
    # get a Topic Sender object to send messages to the topic
    sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
    with sender:
        # send one message        
        message = ServiceBusMessage("This is message using Chained Credentail - Managed Identity, Azure CLI")
        sender.send_messages(message)
        print("Sent a single message")

#print("Done sending messages")
print("-----------------------")