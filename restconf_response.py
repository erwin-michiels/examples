response_json = {
    "ietf-interfaces:interfaces": {

        "interface": [{
            "name": "GigabitEthernet1",
            "description": "VBox",
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": "true",
            "ietf-ip:ipv4": {
                    "address": [{
                        "ip": "192.168.56.101",
                        "netmask": "255.255.255.0"
                    }]
            },
            "ietf-ip:ipv6": {}
        },
            {
            "name": "Loopback9",
                "description": "Lo9",
                "type": "iana-if-type:softwareLoopback",
                "enabled": "true",
                "ietf-ip:ipv4": {
                    "address": [{
                        "ip": "10.9.9.9",
                        "netmask": "255.255.255.0"
                    }]
                },
                "ietf-ip:ipv6": {}
        }
        ]
    }
}

print("=> Printing filtered response")
print("Interface Name: ")
print(response_json["ietf-interfaces:interfaces"]["interface"][0]["name"])
print("IP Address + Subnet: " )
ip_subnet = response_json["ietf-interfaces:interfaces"]["interface"][0]["ietf-ip:ipv4"]["address"] 
print(ip_subnet)
print("IP Address: " )
ip = response_json["ietf-interfaces:interfaces"]["interface"][0]["ietf-ip:ipv4"]["address"][0]["ip"]
print(ip)