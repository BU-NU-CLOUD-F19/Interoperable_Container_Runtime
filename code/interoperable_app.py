#!/usr/bin/python3
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
pid_docker = "/run/containerd/io.containerd.runtime.v1.linux/moby/{}/init.pid"
hostconfig_path_docker = "/var/lib/docker/containers/{}/hostconfig.json"
state_path_docker = "/run/docker/runtime-runc/moby/{}/state.json"
cpu_shares_docker = "/sys/fs/cgroup/cpu/{}/cpu.shares"
memory_limit_docker = "/sys/fs/cgroup/memory/{}/memory.limit_in_bytes"

pids_docker = "/sys/fs/cgroup/pids/{}/pids.max"


config_path_crio = "/var/lib/containers/storage/overlay-containers/{}/userdata/config.json"
state_path_crio = "/var/lib/containers/storage/overlay-containers/{}/userdata/state.json"
cpu_shares_crio = "/sys/fs/cgroup/cpu/{}/cpu.shares"
memory_limit_crio = "/sys/fs/cgroup/memory/{}/memory.limit_in_bytes"
pid_limit_crio = "/sys/fs/cgroup/pids/{}/pids.max"



config_path_containerd = "/run/containerd/io.containerd.runtime.v2.task/default/{}/config.json"
state_path_containerd = "/run/containerd/runc/default/{}/state.json"

cpu_shares_containerd = "/sys/fs/cgroup/cpu/{}/cpu.shares"
memory_limit_containerd = "/sys/fs/cgroup/memory/{}/memory.limit_in_bytes"
pid_limit_containerd = "/sys/fs/cgroup/pids/{}/pids.max"

# config.json attiributes
app_armor_profile_key = "apparmorProfile"
process_key = "process"
root_key = "root"
os_key = "linux"
devices_key = "devices"
resources_key = "resources"
cgroups_key = "cgroupsPath"
cgroups_parent_key = "CgroupParent"
seccomp_key = "seccomp"
mounts_key = "mounts"

readonlyroot_crio = "readonly"
annotations_crio = "annotations"
cgroups_parent_crio = "io.kubernetes.cri-o.CgroupParent"
privileged_crio = "io.kubernetes.cri-o.PrivilegedRuntime"
ports_crio = "io.kubernetes.cri-o.PortMappings"
host_network_crio = "io.kubernetes.cri-o.HostNetwork"
seccomp_crio = "io.kubernetes.cri-o.SeccompProfilePath"
capabilities_key = "capabilities"
permitted_capabilities = "permitted"

# hostconfig.json attributes
security_opts_key = "SecurityOpt"
priviliged_key = "Privileged"
portBindings_key = "PortBindings"
NetworkMode_key = "NetworkMode"
ReadonlyRootfs_key = "ReadonlyRootfs"


#containerd keys
noNewPrivileges = "noNewPrivileges"
config_key = "config"
readonlyfs_key = "readonlyfs"


#Benchmark strings
#Five point ...    V because four also starts with F
Vp1 = 'CIS 5.1:    AppArmor:'
Vp2 = 'CIS 5.2:    Verify SELinux security options'
Vp3 = 'CIS 5.3:    Permitted capabilities:'
Vp4 = 'CIS 5.4:    Privileged runtime:'
Vp5 = 'CIS 5.5:    Mounts: '
Vp6 = 'CIS 5.6:    SSH Within containers:'
Vp7 = 'CIS 5.7:    Privileged ports used:'
Vp8 = 'CIS 5.8:    Check ports:'
Vp9 = 'CIS 5.9:    Host Network:'
Vp10 = 'CIS 5.10:    Memory Limit in bytes:'
Vp11 = 'CIS 5.11:    CPU Share: '
Vp12 = 'CIS 5.12:    Read-only rootfs:'
Vp13 = 'CIS 5.13:    Check specific host-ip:'
Vp14 = "CIS 5.14:    'on-failure' Restart Policy:"
Vp15 = "CIS 5.15:    Host's process namespace not shared:"
Vp16 = "CIS 5.16:    Host's IPC namespace not shared:"
Vp17 = 'CIS 5.17:    Host devices:' 
Vp18 = 'CIS 5.18:    Override default ulimit at runtime if needed:'
Vp19 = 'CIS 5.19:    Mount Propagation not Shared:'
Vp20 = "CIS 5.20:    Host's UTS namespace not shared:"
Vp21 = 'CIS 5.21:    Check Seccomp profile:'
Vp22 = 'CIS 5.22:     Privileged docker exec:'
Vp23 = 'CIS 5.23:     User docker exec'
Vp24 = 'CIS 5.24:     Confirm cgroup usage:'




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
    if sys.argv[1] == "--crio" or sys.argv[1] == "-crio" or sys.argv[1] == "-cri-o" or sys.argv[1] == "--c" or sys.argv[1] == "-c":
        crio_utils()
    elif sys.argv[1] == "--docker" or sys.argv[1] == "-docker" or sys.argv[1] == "--d" or sys.argv[1] == "-d":
        docker_utils()
    elif sys.argv[1] == "--containerd" or sys.argv[1] == "-containerd" or sys.argv[1] == "--ctr" or sys.argv[1] == "-ctr":
        containerd_utils()



def cat_n_grep(filename, lookfor, debug=False): #equivalent to "cat filename | grep lookfor"
    found_it = False
    file = open(filename)
    text = file.read()
    if (debug): print('cat_n_grep read: ', text, sep=' ')
    return True if (lookfor in text) else False


def getpid(runtime):
    if (runtime == 'crio'):
        with open(state_path_crio) as json_file:
            data = json.load(json_file)
            p_id = data['pid'] if ('pid' in data) else False
            return p_id
    if (runtime == 'docker'): #todo
        return False
    if (runtime == 'containerd'): #todo
        return False


def docker_utils():
    with open(config_path_docker) as json_file:
        data = json.load(json_file)
        process_attributes = data[process_key]
        appArmor = process_attributes[app_armor_profile_key] if (app_armor_profile_key in process_attributes) else ('NOT SET!')
        print(Fore.YELLOW)
        print(f"CIS 5.1:     AppArmor: {process_attributes[app_armor_profile_key]}\n")
        print(f"CIS 5.3:     Permitted capabilities: {process_attributes[capabilities_key][permitted_capabilities]}\n")
        print(f"CIS 5.5:     Do not mount sensitive host system directories on containers: {data[mounts_key]}\n")
        print(f"CIS 5.17:     Host Devices: {data[os_key][resources_key][devices_key]}\n")
        
        #TODO: discuss long text
        #print(f"CIS 5.21:     Seccomp Profile: {data[os_key][seccomp_key]}\n")
        
        print(Style.RESET_ALL + "")

        cgrouppath = data[os_key][cgroups_key]

        print(f"CIS 5.24:     Confirm cgroup usage: {cgrouppath}\n")

        memory_limit_docker_formatted = memory_limit_docker.format(cgrouppath)
        cpu_shares_docker_formatted = cpu_shares_docker.format(cgrouppath)
        pids_docker_formatted = pids_docker.format(cgrouppath)


        with open(memory_limit_docker_formatted) as memory_limit:
            mem_limit = memory_limit.read()
            print(Fore.YELLOW)
            print(f"CIS 5.10:     Mem Limit: {mem_limit}")
            print(Style.RESET_ALL + "")
            memory_limit.close()

        with open(cpu_shares_docker_formatted) as cpu_shares:
            cpu_share = cpu_shares.read()
            print(Fore.YELLOW)
            print(f"CIS 5.11:     CPU Share: {cpu_share}")
            print(Style.RESET_ALL + "")
            cpu_shares.close()

        with open(pids_docker_formatted) as pids:
            pids_limit = pids.read()
            print(Fore.YELLOW)
            print(f"CIS 5.28:     Use PIDs cgroup limit: {pids_limit}")
            print(Style.RESET_ALL + "")
            pids.close()
        json_file.close()

    with open(hostconfig_path_docker) as json_file:
        data = json.load(json_file)
        print(Fore.YELLOW)
        print(f"CIS 5.4:     Privileged: {data[priviliged_key]}")
        print(f"CIS 5.7:     Check Privileged ports: {data[portBindings_key]}")
        print(f"CIS 5.8:     Check ports: {data[portBindings_key]}")
        print(f"CIS 5.9:     NetworkMode: {data[NetworkMode_key]}")
        print(f"CIS 5.12:     ReadonlyRootfs: {data[ReadonlyRootfs_key]}")
        print(f"CIS 5.13:     Check specific host-ip: {data[portBindings_key]}")
        #print(f"CIS 5.24:     Confirm cgroup usage -parent: {data[cgroups_parent_key]}\n")
        print(Style.RESET_ALL + "")
        json_file.close()




    with open(pid_docker) as pid_file:
        pid_container = pid_file.read()
        print(f"Pid: {pid_container}")
        pid_file.close()
    


def containerd_utils():
    with open(config_path_containerd) as json_file:
        data = json.load(json_file)
        process_attributes = data[process_key]
        appArmor = process_attributes[app_armor_profile_key] if app_armor_profile_key in process_attributes else 'NOT SET!'
        print(Fore.YELLOW)

        print(f"CIS 5.1:    AppArmor: {appArmor}")
        print(f"CIS 5.3:    Permitted capabilities: {process_attributes[capabilities_key][permitted_capabilities]}")
        print(f"CIS 5.4:    Privileged runtime: {process_attributes[noNewPrivileges]}")
        print(f"CIS 5.5:    Mounts: {data[mounts_key]}")
        print(f"CIS 5.17:    Host Devices: {data[os_key][resources_key][devices_key]}")


        cgrouppath = data[os_key][cgroups_key]
        print(f"CIS 5.24:    Check Cgroup path: {cgrouppath}")

        cpu_share = cpu_shares_containerd.format(cgrouppath)
        memory_limit = memory_limit_containerd.format(cgrouppath)
        pid_limit = pid_limit_containerd.format(cgrouppath)

        with open(memory_limit) as mem:
            mem_result = mem.read()
            print(f"CIS 5.10: Memory Limit in bytes: {mem_result}")
            mem.close()

        with open(cpu_share) as cpu:
            cpu_result = cpu.read()
            print(f"CIS 5.11: CPU Share: {cpu_result}")
            cpu.close()

        with open(pid_limit) as pid:
            pids_limit = pid.read()
            print(f"CIS 5.28:     Use PIDs cgroup limit: {pids_limit}")
            pid.close()

        print(Style.RESET_ALL + "")
    with open(state_path_containerd) as state_json:
        data = json.load(state_json)
        print(f"CIS 5.12:    ReadonlyRootfs: {data[config_key][readonlyfs_key]}")
        print(f"CIS 5.21:    SEccomp profile: {data[config_key][seccomp_key]}")



def crio_utils():
    print("**  CIS Benchmark for CRI-O. **")
    with open(config_path_crio) as json_file:
        data = json.load(json_file)
        process_attributes = data[process_key]
        #print(data)
        
        appArmor = process_attributes[app_armor_profile_key] if app_armor_profile_key in process_attributes else 'NOT SET!'
        print(f"CIS 5.1: AppArmor: {appArmor}")
        #no 5.2 yet
        print(f"CIS 5.3: Permitted capabilities: {data[process_key][capabilities_key][permitted_capabilities]}")
        
        #5.4
        if (privileged_crio in (data[annotations_crio])): 
            print(f"CIS 5.4: Privileged runtime: {data[annotations_crio][privileged_crio]}")
        else:
            print('CIS 5.4: Privileged runtime: Failed. Could not find: ', privileged_crio)
        
        #5.5
        if (mounts_key in data):
            print(f"CIS 5.5: Mounts: {data[mounts_key]}")
        else:
            print('CIS 5.5: Mounts: Failed. ' + mounts_key + 'not found') 

        #5.6
        container_pid = getpid('crio')
        if (container_pid):
            ssh_check = cat_n_grep(('/proc/' + str(container_pid) + '/cmdline'), 'ssh', True)
        print(Vp6, ssh_check)
        
        #5.7 & 5.8
        if (ports_crio in data[annotations_crio]):
            print(Vp7, data[annotations_crio][ports_crio])
            print(Vp8, data[annotations_crio][ports_crio])
        else:
            print(Vp7, 'Failed. Could not find ', ports_crio, sep=' ')
            print(Vp8, 'Failed. Could not find ', ports_crio, sep=' ')

        #5.9
        if (host_network_crio in data[annotations_crio]):
            print(Vp9, data[annotations_crio][host_network_crio], sep=' ')
        else:
            print(Vp9, host_network_crio, sep=' ')
        
        #5.10        
        with open(memory_limit) as mem:
            mem_result = mem.read()
            print(f"CIS 5.10: Memory Limit in bytes: {mem_result}")
            mem.close()

        #5.11
        with open(cpu_share) as cpu:
            cpu_result = cpu.read()
            print(f"CIS 5.11: CPU Share: {cpu_result}")
            cpu.close()

        #5.12
        if (root_key in data):
            if (readonlyroot_crio in data[root_key]):
                print(f"CIS 5.12: Read-only rootfs: {data[root_key][readonlyroot_crio]}")
            else:
                print('CIS 5.12: Read only rootfs: Failed. Could not find', readonlyroot_crio, sep=' ')
        else:
            print('CIS 5.12: Read only rootfs: Failed. Could not find', root_key, sep=' ')

        #5.13
        if (ports_crio in data[annotations_crio]):
            print(f"CIS 5.13: Check specific host-ip: {data[annotations_crio][ports_crio]}")
        else:
            print('CIS 5.13: Check specific host-ip: Failed. Could not find', ports_crio, sep=' ') 

        print(f"CIS 5.17: Host devices: {data[os_key][resources_key][devices_key]}")
        print(f"CIS 5.21: Check Seccomp profile: {data[annotations_crio][seccomp_crio]}")
        #print(f"CIS 5.24: Confirm cgroup usage -parent: {data[annotations_crio][cgroups_parent_crio]}")

        cgrouppath = data[os_key][cgroups_key]
        print(f"CIS 5.24: Confirm cgroup usage: {cgrouppath}")


        cpu_share = cpu_shares_crio.format(cgrouppath)
        memory_limit = memory_limit_crio.format(cgrouppath)
        pid_limit = pid_limit_crio.format(cgrouppath)

        
        
        with open(pid_limit) as pid:
            pid_max = pid.read()
            print(f"CIS 5.28: Pid Max: {pid_max}")
            cpu.close()

        print(Style.RESET_ALL + "")
        
def format_paths():
    global config_path_docker
    global hostconfig_path_docker
    global state_path_docker
    global config_path_crio
    global state_path_crio
    global config_path_containerd
    global state_path_containerd
    global pid_docker



    pid_docker = pid_docker.format(sys.argv[2])

    config_path_docker = config_path_docker.format(sys.argv[2])
    #cpu_shares_docker = cpu_shares_docker.format(sys.argv[2])
    #memory_limit_docker = memory_limit_docker.format(sys.argv[2])

    config_path_containerd = config_path_containerd.format(sys.argv[2])
    state_path_containerd = state_path_containerd.format(sys.argv[2])
    hostconfig_path_docker = hostconfig_path_docker.format(sys.argv[2])
    state_path_docker = state_path_docker.format(sys.argv[2])
    config_path_crio = config_path_crio.format(sys.argv[2])
    state_path_crio = state_path_crio.format(sys.argv[2])




if __name__== "__main__":
    main()