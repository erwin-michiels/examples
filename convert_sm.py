#### FIVE FUNCTIONS TO HELP DESIGN IP SUBNETS 
##   IPv4 subnet masks, prefixes, number of addressess, number of hosts
##   Converting subnet mask into prefix notation
##   Getting number of hosts for a specific prefix
#### ONLY A SMALL COLLECTION OF PREFIXES ARE USED IN THIS EXAMPLE

netmask_prefixes = {
     '255.255.255.252': '/30'
    ,'255.255.255.248': '/29'
    ,'255.255.255.240': '/28'
    ,'255.255.255.224': '/27'
    ,'255.255.255.192': '/26'
    ,'255.255.255.128': '/25'
    ,'255.255.255.0'  : '/24'
    ,'255.255.254.0'  : '/23'
}

prefix_netmasks = {
     '/30': '255.255.255.252'
    ,'/29': '255.255.255.248'
    ,'/28': '255.255.255.240' 
    ,'/27': '255.255.255.224' 
    ,'/26': '255.255.255.192' 
    ,'/25': '255.255.255.128' 
    ,'/24': '255.255.255.0'   
    ,'/23': '255.255.254.0'   
}

netmask_netbits = {
    '255.255.255.252': '1111 1111 1111 1111 1111 1111 1111 1100',
    '255.255.255.248': '1111 1111 1111 1111 1111 1111 1111 1000',
    '255.255.255.240': '1111 1111 1111 1111 1111 1111 1111 0000',
    '255.255.255.224': '1111 1111 1111 1111 1111 1111 1110 0000',
    '255.255.255.192': '1111 1111 1111 1111 1111 1111 1100 0000',
    '255.255.255.128': '1111 1111 1111 1111 1111 1111 1000 0000',
    '255.255.255.0'  : '1111 1111 1111 1111 1111 1111 0000 0000',
    '255.255.254.0'  : '1111 1111 1111 1111 1111 1110 0000 0000',
    '255.255.252.0'  : '1111 1111 1111 1111 1111 1100 0000 0000',
    '255.255.248.0'  : '1111 1111 1111 1111 1111 1000 0000 0000',
    '255.255.240.0'  : '1111 1111 1111 1111 1111 0000 0000 0000',
    '255.255.224.0'  : '1111 1111 1111 1111 1110 0000 0000 0000'
}

def get_net_prefix(p_subnet_mask):
    try:
        net_prefix = netmask_prefixes[p_subnet_mask]
        return net_prefix
    except:
        return "Wrong input: garbage in, garbage out"

def get_number_ip_addresses(p_prefix):
    #### example /30 => 30
    pbits = 32-int(p_prefix[1:])
    return 2 ** pbits

def get_number_ip_hosts(p_prefix):
    #pbits = 32-int(p_prefix[1:])
    return get_number_ip_addresses(p_prefix)-2
    #return (2 ** pbits)-2

def get_netmask(p_prefix):
    try:
        net_mask = prefix_netmasks[p_prefix]
        return net_mask
    except:
        return "Wrong input: garbage in, garbage out"

def get_network_bits(p_subnet_mask):
    try:
        net_bits = netmask_netbits[p_subnet_mask]
        return net_bits
    except:
        return "Wrong input: garbage in, garbage out"

if __name__ == "__main__":
    ### dev test function via prefix
    subnet_mask = ('255.255.255.192')
    print(subnet_mask)
    net_prefix = get_net_prefix(subnet_mask)
    print(net_prefix)
    net_mask = get_netmask(net_prefix)
    net_bits = get_network_bits(net_mask)
    print(net_bits)
    net_number_addr =  get_number_ip_addresses(net_prefix)
    net_number_ip_hosts =  get_number_ip_hosts(net_prefix)
    print(net_number_addr)
    print(net_number_ip_hosts)
    print(type(prefix_netmasks))