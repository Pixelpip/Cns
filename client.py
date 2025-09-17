import requests

# Define file paths for certificates and key
ca_cert = 'myCA.crt'
client_cert = 'client.crt'
client_key = 'client.key'

server_url = 'https://localhost:5000'

try:
    print(f"Attempting to connect to {server_url} with client certificate...")
    
    response = requests.get(
        server_url,
        # Provide the client certificate and key
        cert=(client_cert, client_key),
        
        # Provide the CA certificate to verify the server
        verify=ca_cert
    )
    
    # If the request was successful, print the response
    response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)
    print("\n******Connection Successful!****")
    print("\nServer Response:")
    print(response.text)

except requests.exceptions.SSLError as e:
    print("\n*****SSL Error. Handshake failed. Is the server running with the correct CA?*********")
    print(e)
except requests.exceptions.ConnectionError as e:
    print("\n********Connection Error. Is the server running?******")
    print(e)
except Exception as e:
    print(f"\n*******An unexpected error occurred: {e}********")