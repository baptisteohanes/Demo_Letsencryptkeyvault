#!/bin/sh
MSI_HEADER=${IDENTITY_HEADER}
MSI_ENDPOINT=${IDENTITY_ENDPOINT}
AZURE_CLIENT_ID=${CLIENT_ID}
VAULT_NAME=${VAULT_NAME}
VAULT_URL="https://${VAULT_NAME}.vault.azure.net/"
az login --identity
az keyvault certificate list --vault ${VAULT_NAME}
