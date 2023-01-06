response_json = {
    "response": [
        {
            "authorization": [
                {
                    "role": "ROLE_POLICY_ADMIN",
                    "scope": "ALL"
                }
            ],
            "username": "devnetuser",
            "authSource": "internal"
        }
    ],
    "version": "1.0"
}

# Parsing raw response to list out all users and their role
for item in response_json["response"]:
    for item1 in item["authorization"]:
        print("User \'%s\', role is the %s."%(item["username"],(item1["role"])[5:]))