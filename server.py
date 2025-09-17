import ssl
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    # The fact that the request reached this point means the client's
    # certificate was successfully verified by the SSL context.
    # The crash was happening when trying to *read* the cert details,
    # not during the verification itself.
    print("Successfully connected with a verified client.")
    return "<h1>Connection Successful!</h1><p>Your client certificate was accepted.</p>"
if __name__ == '__main__':
    # Create an SSL context
    # This configures the server to require and verify a client certificate
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    
    # 1. Load the server's own certificate and private key
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')
    
    # 2. Load the CA certificate to verify clients against
    context.load_verify_locations(cafile='myCA.crt')
    
    # 3. Enforce client certificate validation
    context.verify_mode = ssl.CERT_REQUIRED
    
    # Run the Flask app with the custom SSL context
    print("Starting server with mTLS on https://localhost:5000")
    app.run(port=5000, ssl_context=context)