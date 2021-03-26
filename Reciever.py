from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os, time, datetime

CONNECTION_STR = os.environ['SERVICE_BUS_CONN_STR']
TOPIC_NAME = os.environ['SERVICE_BUS_TOPIC_NAME']
SUBSCRIPTION_NAME = os.environ['SERVICE_BUS_TOPIC_SUB_NAME']

print("["+ str(datetime.datetime.now()) + "] : Reciever Started ...")

# create a Service Bus client using the connection string
servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    while True:
        # get the Subscription Receiver object for the subscription    
        receiver = servicebus_client.get_subscription_receiver(topic_name=TOPIC_NAME, subscription_name=SUBSCRIPTION_NAME, max_wait_time=5)
        with receiver:
            for msg in receiver:
                print("["+ str(datetime.datetime.now()) + "] : Received: " + str(msg))
                # complete the message so that the message is removed from the subscription
                receiver.complete_message(msg)
        time.sleep(5)