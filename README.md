[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Ffsaleemm%2FAzureServiceBusManagedIdentity%2Fmain%2Ftemplates%2Fazuredeploy.json)

# Service Bus and Azure Identity

## Introduction

This is sample code to demonstrate how credentials and authentication flow work with Azure hosted applications, specifically Azure Service Bus. This document assumes that the reader is familiar with [Azure Service Bus concepts](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview#concepts-and-terminology), specifically around Sender, Receiver, Namespaces, Topics and Subscriptions. 

The sample includes the following:

1. Receiver.py: This receiver subscribes to one of the Subscriptions for the Topic.
1. SendTopicCS.py: This sends a message to the Topic using the traditional Service Bus Connection string.
1. SendTopicMI.py: This sends a message to the Topic using the Default Azure Credential.
1. SendTopicMI2.py: This sends a message to the Topic using the Chained Token Credential.

## Architecture

The following components will be deployed to your resource group.

![Components Deployed](/images/comp.PNG)

## Demo Script

1. Deploy the components using the Deploy to Azure button above.
1. Start the Receiver.

    ```bash
    python Receiver.py
    ```

1. Send a message using the Connection string sender script.

    ```bash
    python SendTopicCS.py
    ```

    ![Receiver Connection String](/images/reccs.PNG)

1. Walk through the Default Credential authentication flow.
1. Send a message using the default credential sender script.

    ```bash
    python SendTopicMI.py
    ```

    ![Receiver Default Credentail](/images/recmi.PNG)

1. Explain the Send Claim error.
1. Setup the Send Role in Azure Service Bus to include your user.
1. Send a message using the default credential sender script. There will be no error.
1. Walk through the custom authentication flow.
1. Send a message using the chained token credential sender script.

    ```bash
    python SendTopicMI2.py
    ```

1. Deploy the SendToSB function to the Function App.
1. Setup the Managed Identity for Function App.
1. Setup the Send Role in Azure Service Bus to include the Function App Managed Identity.
1. Run the SendToSB function via Azure Portal.

Disclaimer: This is a sample application/code with rudimentary error/exception handling and no unit testing. It is intended as an illustration/demo and not for production use.