import base64

def encode_decode_base64():
    while True:
        user_input = input("Enter a string to encode/decode with base64 (q to quit): ")
if user_input.lower() == 'q':
            break

        # Encoding the input string using base64
        encoded_bytes = base64.b64encode(user_input.encode('utf-8'))
        encoded_string = encoded_bytes.decode('utf-8')
        print("Encoded: ", encoded_string)

        # Decoding the encoded string using base64
        decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))

decoded_string = decoded_bytes.decode('utf-8')
        print("Decoded: ", decoded_string)

encode_decode_base64()