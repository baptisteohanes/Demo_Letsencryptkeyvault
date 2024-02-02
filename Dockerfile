FROM mcr.microsoft.com/azure-cli
COPY /cli-v0.4-linux-x64 /usr/local/bin
COPY /renewcertificates.sh /usr/local/bin
#RUN pip install azure-keyvault-certificates azure-identity
WORKDIR /usr/local/bin
ENTRYPOINT ["./renewcertificates.sh"]