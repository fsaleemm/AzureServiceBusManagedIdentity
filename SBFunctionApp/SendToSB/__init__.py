import logging, os
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.identity import DefaultAzureCredential

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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
            send_single_message(sender)

    logging.info("Done sending messages")

    return func.HttpResponse("This HTTP triggered function executed successfully.")


def send_single_message(sender):
    # create a Service Bus message
    message = ServiceBusMessage("This is message using Managed Identity of Azure Function")
    # send the message to the topic
    sender.send_messages(message)
    logging.info("Sent a single message")