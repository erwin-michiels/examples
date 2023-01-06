# Dictionary of network prefixes and subnet masks (partial example)

prefix_subnet_masks = {
    "/24": "255.255.255.0",
    "/25": "255.255.255.128",
    "/26": "255.255.255.192"
}

# example 1
subnet_mask_1 = prefix_subnet_masks["/24"]
print(subnet_mask_1)
# outputs: 255.255.255.0

# example 2
subnet_mask_2 = prefix_subnet_masks.get("/26")
print(subnet_mask_2)
# outputs: 255.255.255.192