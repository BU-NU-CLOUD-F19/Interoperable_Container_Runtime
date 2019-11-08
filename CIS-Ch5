CIS Benchmark Chapter 5 for Docker
| Number | Definition | Implementation
| ------------- | ------------- | ------------- |

|5.1		|Do not disable AppArmor Profile (Scored)	|/proc/{pid}/attr/apparmor/current	|
|5.2		|Verify SELinux security options, if applicable (Scored)	|ps -eZ &#124; grep {pid_container}	|
|5.3		|Restrict Linux Kernel Capabilities within containers (Scored)	|/run/containerd/io.containerd.runtime.v1.linux/moby/{}/config.json -> ["process"]["capabilities"]["permitted"]	|
|5.4		|Do not use privileged containers (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["Privileged"]	|
|5.5		|"Do not mount sensitive host system directories on containers(Scored)"|	/run/containerd/io.containerd.runtime.v1.linux/moby/{}/config.json -> ["mounts"]|	
|5.7		|Do not map privileged ports within containers (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["PortBindings"]	|
|5.8		|Open only needed ports on container (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["PortBindings"]	|
|5.9		|Do not share the host's network namespace (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["NetworkMode"]	|
|5,10	|Limit memory usage for container (Scored)	|/sys/fs/{cgroup_from_config}/memory/{cont_id}/memory.limit_in_bytes	|
|5,11	|Set container CPU priority appropriately (Scored)	|/sys/fs/{cgroup_from_config}/cpu/{cont_id}/mcpu.share	|
|5,12	|Mount container's root filesystem as read only (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["ReadOnlyRootfs"]	|
|5,13	|Bind incoming container traffic to a specific host interface (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["PortBindings"]	|
|5.14	|Set the 'on-failure' container restart policy to 5 (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["RestartPolicy"]["MaximumRetryCount"]	|
|5.15	|Do not share the host's process namespace (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["PidMode"]	|
|5.16	|Do not share the host's IPC namespace (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["IpcMode"]|	
|5.17	|Do not directly expose host devices to containers (Not Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["Devices"]	|
|5.18	|Override default ulimit at runtime only if needed (Not Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["Ulimits"]	|
|5,20	|Do not share the host's UTS namespace (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["UTSMode"]	|
|5,21	|Do not disable default seccomp profile (Scored)	|/run/containerd/io.containerd.runtime.v1.linux/moby/{}/config.json -> ["linux"]["seccomp"]	|
|5,24	|Confirm cgroup usage (Scored)	|/run/containerd/io.containerd.runtime.v1.linux/moby/{}/config.json -> ["linux"]["cgroup"]	|
|5,25	|Restrict container from acquiring additional privileges (Scored)	|/var/lib/docker/containers/{}/hostconfig.json -> ["SecurityOpt"]	|
|5,28	|Use PIDs cgroup limit (Scored)	|/sys/fs/{cgroup_from_config}/pids/{cont_id}/pids.max	|
