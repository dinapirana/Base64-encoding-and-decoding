import base64

def encode_decode_base64():
    while True:
        user_input = input("Enter a string to encode/decode with base64 (q to quit): ")
if user_input.lower() == 'q':
            break

        # Encoding the input string using base64
        encoded_bytes = base64.b64encode(user_input.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')