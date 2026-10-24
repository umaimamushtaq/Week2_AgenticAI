import requests

token="UmaimaMushtaq_AgenticAI_Week2_Token_Very_Very_Secure"

headers={
    "Authorization":f"Bearer {token}"
}

print("request Headers:")
print("Authorization: Bearer <token>")

print("\n Header constructed successfully:", headers["Authorization"].
startswith("Bearer "))