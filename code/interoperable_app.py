import json
import sys
from pyfiglet import Figlet
from colorama import Fore, Back, Style 


#pip3 install pyfiglet
#pip3 install colorama

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

DEBUG = False

custom_fig = Figlet(font='doom')
help_text = "\n\nPlease enter command as --{runtime} {container_id} to apply benchmark tests\n\nExample: interoperable_app --crio 123134"


config_path_docker = "/run/containerd/io.containerd.runtime.v1.linux/moby/{}/config.json"
rootfs_path_docker = "/run/containerd/io.containerd.runtime.v1.linux/moby/{}/rootfs"
hostconfig_path_docker = "/var/lib/docker/containers/{}/hostconfig.json"
state_path_docker = "/run/docker/runtime-runc/moby/{}/state.json"


config_path_crio = "/var/lib/containers/storage/overlay-containers/{}/userdata/config.json"
state_path_crio = "/var/lib/containers/storage/overlay-containers/{}/userdata/state.json"

config_path_containerd = "/run/containerd/io.containerd.runtime.v2.task/default/{}/config.json"
state_path_containerd = "/run/containerd/runc/default/{}/state.json"


# config.json attiributes
app_armor_profile_key = "apparmorProfile"
process_key = "process"
capabilities_key = "capabilities"
permitted_capabilities = "permitted"

# hostconfig.json attributes
security_opts_key = "SecurityOpt"
priviliged_key = "Privileged"


if DEBUG == True:
    config_path_docker = "../../../docker-container-fs/config.json"
    hostconfig_path_docker = "../../../docker-container-fs-selinux/hostconfig.json"
    config_path_crio = "../../../crio/userdata/config.json"
    state_path_crio = "../../../crio/userdata/state.json"

def help_func():
    for item in sys.argv[1:]:
        if item == "--debug":
            DEBUG = True
    if sys.argv[1] and sys.argv[1] == "--help" or sys.argv[1] == "--h":
        print(Fore.YELLOW + help_text)
        print(Style.RESET_ALL + "")
        return True
    return False




def main():
    print(custom_fig.renderText('Interoperable!!'))
    data = {}
    #print(f"the script has the name {sys.argv[0]}" )
    if help_func():
        return
    if DEBUG == False:
        format_paths()
    if sys.argv[1] == "--crio" or sys.argv[1] == "-crio" or sys.argv[1] == "--c" or sys.argv[1] == "-c":
        crio_utils()
    elif sys.argv[1] == "--docker" or sys.argv[1] == "-docker" or sys.argv[1] == "--d" or sys.argv[1] == "-d":
        docker_utils()
    elif sys.argv[1] == "--containerd" or sys.argv[1] == "-containerd" or sys.argv[1] == "--ctr" or sys.argv[1] == "-ctr":
        containerd_utils()


def docker_utils():
    with open(config_path_docker) as json_file:
        data = json.load(json_file)
        process_attributes = data[process_key]
        appArmor = process_attributes[app_armor_profile_key] if app_armor_profile_key in process_attributes else 'NOT SET!'
        print(Fore.YELLOW)
        print(f"CIS 5.1:     appArmor: {process_attributes[app_armor_profile_key]}")
        print(f"CIS 5.3:     permitted capabilities: {process_attributes[capabilities_key][permitted_capabilities]}")
        print(Style.RESET_ALL + "")


def containerd_utils():
    with open(config_path_containerd) as json_file:
        data = json.load(json_file)
        process_attributes = data[process_key]
        appArmor = process_attributes[app_armor_profile_key] if app_armor_profile_key in process_attributes else 'NOT SET!'
        print(Fore.YELLOW)

        print(f"CIS 5.1: appArmor: {appArmor}")
        print(f"CIS 5.3:     permitted capabilities: {process_attributes[capabilities_key][permitted_capabilities]}")
        print(Style.RESET_ALL + "")

def crio_utils():
    print("**  CIS Benchmark for CRI-O. **")
    with open(config_path_crio) as json_file:
        data = json.load(json_file)
        process_attributes = data[process_key]
        #print(data)
        
        appArmor = process_attributes[app_armor_profile_key] if app_armor_profile_key in process_attributes else 'NOT SET!'
        print(f"CIS 5.1: appArmor: {appArmor}")
        print(f"CIS 5.3: permitted capabilities: {data[process_key][capabilities_key][permitted_capabilities]}")
        print(Style.RESET_ALL + "")
        
def format_paths():
    global config_path_docker
    global hostconfig_path_docker
    global state_path_docker
    global config_path_crio
    global state_path_crio
    global config_path_containerd

    config_path_docker = config_path_docker.format(sys.argv[2])
    config_path_containerd = config_path_containerd.format(sys.argv[2])
    hostconfig_path_docker = hostconfig_path_docker.format(sys.argv[2])
    state_path_docker = state_path_docker.format(sys.argv[2])
    config_path_crio = config_path_crio.format(sys.argv[2])
    state_path_crio = state_path_crio.format(sys.argv[2])




if __name__== "__main__":
    main()