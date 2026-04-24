import base64
import json

token = input("Enter JWT token: ")

parts = token.split(".")

if len(parts) != 3:
    print("Invalid JWT format")
else:
    try:
        header = parts[0] + "=" * (-len(parts[0]) % 4)
        payload = parts[1] + "=" * (-len(parts[1]) % 4)

        decoded_header = base64.urlsafe_b64decode(header).decode()
        decoded_payload = base64.urlsafe_b64decode(payload).decode()

        print("\nHeader:")
        print(json.dumps(json.loads(decoded_header), indent=4))

        print("\nPayload:")
        print(json.dumps(json.loads(decoded_payload), indent=4))

    except Exception:
        print("Failed to decode token")
