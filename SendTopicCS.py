from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os

# the connection string will be secret in keyvault typically
CONNECTION_STR = os.environ['SERVICE_BUS_CONN_STR']
TOPIC_NAME = os.environ['SERVICE_BUS_TOPIC_NAME']

# create a Service Bus client using the connection string
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    # get a Topic Sender object to send messages to the topic
    sender = servicebus_client.get_topic_sender(topic_name=TOPIC_NAME)
    with sender:
        # send one message        
        message = ServiceBusMessage("This is message using Service Bus Connection String")
        sender.send_messages(message)
        print("Sent a single message")

#print("Done sending messages")
print("-----------------------")