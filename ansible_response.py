ansible_dict = {"ansible_facts": {"ansible_all_ipv4_addresses": ["192.0.2.1", "192.0.2.2", "192.0.2.3", "192.0.2.4", "192.0.2.5", "10.0.2.15", "172.17.0.1"], "ansible_all_ipv6_addresses": ["fe80::9002:c8ff:fee8:bb09", "fe80::3c67:a5ff:fe17:e4cf", "fe80::a00:27ff:fee9:3de6", "fe80::42:3ff:fef6:9477"], "ansible_apparmor": {"status": "enabled"}, "ansible_architecture": "x86_64", "ansible_bios_date": "12/01/2006", "ansible_bios_version": "VirtualBox", "ansible_cmdline": {"BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic", "quiet": "true", "ro": "true", "root": "UUID=fb261367-cf98-4bce-b682-42b3de0a8ab9", "vga": "792", "zswap.enabled": "1"}, "ansible_date_time": {"date": "2021-01-20", "day": "20", "epoch": "1611160850", "year": "2021"}, "ansible_default_ipv4": {"address": "10.0.2.15", "alias": "enp0s3", "broadcast": "10.0.2.255", "gateway": "10.0.2.2", "interface": "enp0s3", "macaddress": "08:00:27:e9:3d:e6", "mtu": 1500, "netmask": "255.255.255.0", "network": "10.0.2.0", "type": "ether"}, "ansible_default_ipv6": {}, "ansible_device_links": {"ids": {"sda": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd"], "sda1": ["ata-VBOX_HARDDISK_VBbdc0f9c8-459ea1fd-part1"], "interfaces": [], "ipv4": {"address": "192.0.2.1", "broadcast": "global", "netmask": "255.255.255.255", "network": "192.0.2.1"}, "ipv6": [{"address": "fe80::9002:c8ff:fee8:bb09", "prefix": "64", "scope": "link"}], "macaddress": "92:02:c8:e8:bb:09", "mtu": 1500, "promisc": "false", "stp": "…", "ipv4": {"address": "10.0.2.15", "broadcast": "10.0.2.255", "netmask": "255.255.255.0", "network": "10.0.2.0"}, "ipv6": [{"address": "fe80::a00:27ff:fee9:3de6", "prefix": "64", "scope": "link"}], "macaddress": "08:00:27:e9:3d:e6", "module": "e1000", "mtu": 1500, "HOME": "/home/devasc\" , … , \"PATH\"\: \"/usr/local/sbin\: / usr/local/bin\: / usr/sbin\: / usr/bin\: / sbin\: ",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 "PWD": "/home/devasc\", \"SHELL\"\: \"/bin/bash", "SHLVL": "0", "SSH_CLIENT": "192.0.2.3 55752 22", "ansible_fqdn": "labvm.vm", "ansible_hostname": "labvm", "ansible_hostnqn": "", "ansible_is_chroot": "false", "ansible_lsb": {"codename": "focal", "description": "Ubuntu 20.04.1 LTS", "id": "Ubuntu", "major_release": "20", "release": "20.04"}, "ansible_machine": "x86_64", "ansible_machine_id": "c6a52afed8564edfa075a362c20348b8", "ansible_memfree_mb": 258, "ansible_nodename": "labvm", "ansible_os_family": "Debian", "ansible_pkg_mgr": "apt", "ansible_proc_cmdline": {"BOOT_IMAGE": "/boot/vmlinuz-5.4.0-37-generic", "quiet": "true", "ro": "true", "root": "UUID = fb261367-cf98-4bce-b682-42b3de0a8ab9", "vga": "792", "ansible_processor": ["0", "GenuineIntel", "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz", "1", "GenuineIntel", "Intel(R) Core(TM) i7-7600U CPU @ 2.80GHz"], "ansible_processor_cores": 2, "ansible_processor_count": 1, "ansible_product_name": "VirtualBox", "ansible_product_version": "1.2", "ansible_python": {"executable": "/usr/bin/python3", "has_sslcontext": "true", "type": "cpython", "version": {"major": 3, "micro": 2, "minor": 8, "releaselevel": "final", "serial": 0}, "version_info": [3, 8, 2, "final", 0]}, "ansible_python_version": "3.8.2", "ansible_system": "Linux", "ansible_system_capabilities": [""], "ansible_system_capabilities_enforced": "True", "ansible_system_vendor": "innotek GmbH", "ansible_uptime_seconds": 88854, "ansible_user_dir": "/home/devasc", "ansible_user_gecos": "DevNet Associate, , , ", "ansible_user_gid": 900, "ansible_user_id": "devasc", "ansible_user_shell": "/bin/bash", "ansible_user_uid": 900, "changed": "false", "deprecations": [], "warnings": []}}}}}
print("---------1--------")
print("Showing dictionary keys at level 1")
# ansible_dict = json.loads(ansible_json_doc)
print(ansible_dict.keys())

print("---------2--------")
print("Showing keys of ansible facts at level 2")
print(ansible_dict['ansible_facts'].keys())

print("---------3--------")
print("Showing data below ansible facts: ip address")
print("IP Address: " + ansible_dict["ansible_facts"]
      ["ansible_default_ipv4"]["address"])

#print('---------4--------')
#print("Showing data below ansible facts: ansible distribution")
#print("Ansible Distribution: " +
#      ansible_dict["ansible_facts"]["ansible_distribution"])
#print("Ansible Distribution Major: " +
#      ansible_dict["ansible_facts"]["ansible_distribution_major_version"])
#print("Ansible Distribution Release: " +
#      ansible_dict["ansible_facts"]["ansible_distribution_release"])
#print("Ansible Distribution Version: " +
#      ansible_dict["ansible_facts"]["ansible_distribution_version"])

#print('---------5--------')
#print("Showing data below ansible facts: kernel, nodename, os")
#print("Ansible Kernel: " + ansible_dict["ansible_facts"]["ansible_kernel"])
#print("Ansible Nodename: " + ansible_dict["ansible_facts"]["ansible_nodename"])
#print("Ansible OS Family: " +
#      ansible_dict["ansible_facts"]["ansible_os_family"])
#print("Ansible PKG Manager: " +
#      ansible_dict["ansible_facts"]["ansible_pkg_mgr"])
#print("Ansible Python Version: " +
#      ansible_dict["ansible_facts"]["ansible_python_version"])

#print('---------6--------')
#print("Showing data below ansible facts: ansible environment")
#print("Ansible Home: " + ansible_dict["ansible_facts"]["ansible_env"]["HOME"])
#print("Ansible User: " + ansible_dict["ansible_facts"]["ansible_env"]["USER"])