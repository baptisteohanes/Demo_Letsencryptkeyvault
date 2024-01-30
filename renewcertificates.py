#!/usr/bin/env python
import os
import datetime
import subprocess
from azure.keyvault.certificates import CertificateClient, CertificatePolicy, KeyVaultCertificate
from azure.identity import DefaultAzureCredential
# ------------------------------------

VAULT_URL = os.environ["VAULT_URL"]
AZURE_CLIENT_ID = os.environ["AZURE_CLIENT_ID"]
IDENTITY_ENDPOINT= os.environ["IDENTITY_ENDPOINT"]
IDENTITY_HEADER = os.environ["IDENTITY_HEADER"]

print(f"Logging in to {VAULT_URL} with client id '{AZURE_CLIENT_ID}'...")
print(f"IDENTITY_ENDPOINT: {IDENTITY_ENDPOINT}")
print(f"IDENTITY_HEADER: {IDENTITY_HEADER}")

credential = DefaultAzureCredential(managed_identity_client_id=AZURE_CLIENT_ID)
client = CertificateClient(vault_url=VAULT_URL, credential=credential)

#Let's list the certificates.

print("\n.. List certificates from the Key Vault")
certificates = client.list_properties_of_certificates()
for certificate in certificates:
    print(f"Certificate with name '{certificate.name}' was found.")
    print(f"Certificate expiration date is '{certificate.expires_on}'.")
    if certificate.expires_on>(datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(days=7)):
        print("Certificate has to be renewed")
print("\nrun_sample done")

#Let's login with AzLogin
subprocess.run(["az", "login", "--debug","--identity", "--username", AZURE_CLIENT_ID])