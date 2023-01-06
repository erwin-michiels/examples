resp_devices_json = {
    "response": [
        {
            "memorySize": "NA",
            "family": "Switches and Hubs",
            "hostname": "cat_9k_1",
            "macAddress": "f8:7b:20:67:62:80",
            "serialNumber": "FCW2136L0AK",
            # -- partly not shown --
            "deviceSupportLevel": "Supported",
            "collectionStatus": "Managed",
            "upTime": "25 days, 19:42:18.12",
            "lastUpdateTime": 1611060834555,
            "softwareType": "IOS-XE",
            "softwareVersion": "17.3.1",
            "bootDateTime": "2020-12-24 17:11:54",
            "lastUpdated": "2021-01-19 12:53:54",
            "managementIpAddress": "10.10.22.66",
            "platformId": "C9300-24UX",
            "reachabilityStatus": "Reachable",
            "series": "Cisco Catalyst 9300 Series Switches",
            "type": "Cisco Catalyst 9300 Switch",
            "location": "null",
            "role": "ACCESS",
            "instanceUuid": "21335daf-f5a1-4e97-970f-ce4eaec339f6",
            "instanceTenantId": "5dc444d31485c5004c0fb20b",
            "id": "21335daf-f5a1-4e97-970f-ce4eaec339f6"
        },
        {
            "memorySize": "NA",
            "family": "Switches and Hubs",
            "hostname": "cat_9k_2",
            "macAddress": "f8:7b:20:71:4d:80",
            "serialNumber": "FCW2140L039",
            # -- partly not shown --
            "managementIpAddress": "10.10.22.70",
            # --- not shown ---
            "type": "Cisco Catalyst 9300 Switch",
            "location": "null",
            "role": "ACCESS",
            "instanceUuid": "3e48558a-237a-4bca-8823-0580b88c6acf",
            "instanceTenantId": "5dc444d31485c5004c0fb20b",
            "id": "3e48558a-237a-4bca-8823-0580b88c6acf"
        }
    ],
    "version": "1.0"
}

dev_list = []   #create empty list
# loop through results and filter needed information
# create new JSON structure

for device in resp_devices_json['response']:
    if device['type'] != None:
        dev_dict = {} #create empty dict
        dev_dict['hostname'] = device['hostname']
        dev_dict['type'] = device['type']
        dev_dict['macAddress'] = device['macAddress']
        dev_dict['managementIpAddress'] = device['managementIpAddress']
        dev_dict['serialNumber'] = device['serialNumber']
        #dev_dict['softwareType'] = device['softwareType']
        #dev_dict['softwareVersion'] = device['softwareVersion']
        #dev_dict['reachabilityStatus'] = device['reachabilityStatus']
        dev_list.append(dev_dict)
print(dev_list)