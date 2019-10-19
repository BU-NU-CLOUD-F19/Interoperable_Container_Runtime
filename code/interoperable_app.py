import json
import sys
from pyfiglet import Figlet

#pip install pyfiglet

"""
CIS 5.1 -->  Do not disable AppArmor Profile (Scored) 
		--> config.json[process_key][app_armor_profile_key]

CIS 5.2 --> Verify SELinux security options, if applicable (Scored)
		--> hostconfig.json[security_opts_key][0] == ??
		--> label=disable default if no SE_Linux provided!!!

CIS 5.3 -->  Restrict Linux Kernel Capabilities within containers (Scored) 
		--> config.json[process_key][capabilities_key][permitted_capabilities]
		--> NET_ADMIN, SYS_ADMIN, SYS_MODULE --> restricted

CIS 5.4 -->  Do not use privileged containers (Scored)
		--> hostconfig.json[priviliged_key]

"""

DEBUG = True

custom_fig = Figlet(font='doom')
help_text = "Please provide a helper text for commands and stuff"


config_path = "/run/containerd/io.containerd.runtime.v1.linux/moby/{container_id}/config.json"
rootfs_path = "/run/containerd/io.containerd.runtime.v1.linux/moby/{container_id}"
hostconfig_path = "/var/lib/docker/containers/{container_id}"
state_path = "/run/docker/runtime-runc/moby/{container_id}"


# config.json attiributes
app_armor_profile_key = "apparmorProfile"
process_key = "process"
capabilities_key = "capabilities"
permitted_capabilities = "permitted"

# hostconfig.json attributes
security_opts_key = "SecurityOpt"
priviliged_key = "Privileged"


if DEBUG == True:
	config_path = "../../../docker-container-fs/config.json"
	hostconfig_path = "../../../docker-container-fs-selinux/hostconfig.json"

def help_func():
	if sys.argv[1] and sys.argv[1] == "--help" or sys.argv[1] == "--h":
		print(help_text)




def main():
	print(custom_fig.renderText('Interoperable!!'))
	data = {}
	#print(f"the script has the name {sys.argv[0]}" )
	#help_func()
	with open(config_path) as json_file:
	    data = json.load(json_file)
	    #print(data)
	    print(f"CIS 5.1:	 appArmor: {data[process_key][app_armor_profile_key]}")
	    print(f"CIS 5.3:     permitted capabilities: {data[process_key][capabilities_key][permitted_capabilities]}")


	with open(hostconfig_path) as json_file:
		data = json.load(json_file)
		print(f"CIS 5.4:	 Privileged : {data[priviliged_key]}")
		print(f"CIS 5.2:	 SE_Linux : {data[security_opts_key]}")






if __name__== "__main__":
	main()