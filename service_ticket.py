response_json = {
    "response": {
        "serviceTicket": "ST-415-HpemSXpzSnTAYFQIqTNQ-cas",
        "idleTimeout": 1800,
        "sessionTimeout": 21600
    },
    "version": "1.0"
}

print ("ticket: ",response_json["response"]["serviceTicket"])