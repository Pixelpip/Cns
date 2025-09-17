# Implementation of Mutual Authentication Protocol

## 1. Generate Certificates
First, create the necessary certificates and keys using OpenSSL.

```bash
# Create a Certificate Authority (CA), and server & client certificates
openssl genrsa -out myCA.key 2048
openssl req -x509 -new -nodes -key myCA.key -sha256 -days 1024 -out myCA.crt -subj "/CN=myCA"

openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
openssl x509 -req -in server.csr -CA myCA.crt -CAkey myCA.key -CAcreateserial -out server.crt -days 500

openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/CN=test-client"
openssl x509 -req -in client.csr -CA myCA.crt -CAkey myCA.key -CAcreateserial -out client.crt -days 500

# Clean up temporary files
rm *.csr *.srl
```

## 2. Install Dependencies
Install Flask and Requests using pip.

```bash
pip install Flask requests
```

## 3. Run the Application
Open Terminal 1 and run the server:

```bash
python server.py
```

Open Terminal 2 and run the client:

```bash
python client.py
```