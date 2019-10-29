Should prioirtize the "Score" over "Not-Scored" Benchmarks, as Scored ones have more rigidly defined security consequences, and will likely be easier to implement, as remediation points to specific attributes in the target file.

Next steps: determine how to pull image file based on targeted container ID on commandline
Evaluate equivalent commands for image files in CRI-O/containerd
Begin coding prototype for 4.1

***

4.1 Create a user

Am looking for USER <username/ID> or equivalent in the image file; if this is missing, container is running as root which is the default behavior in Docker at least.

4.5 Enable Content trust

Disabled by default; provides ability to use digital signatures

in Docker, this is DOCKER_CONTENT_TRUST=1 which is an enviornment variable.

4.6 Add HEALTHCHECK instruction

Am looking for HEALTHCHECK in the image file; if not present health check is disabled

***

4.2 Use trusted base images

"Ensure that the container image is written either from scratch or is based on another established and trusted base image downloaded over a secure channel"

No easy way to do this programatically, audit relies on inspecting the host and then obtaining "proof of evidence" that the images were obtained from trusted source from the SysAdmin.

Could simply implement means of listing the image, but can't be flagged as pass/fail

4.3 Do not install unncessary packages in the container

Intended to ensure that the container matches with the basic concept that containers should represent a slimmed down version of the OS. However, this also requires knowing what the container is doing in order to determine whether an installed package is legitimate. Could implement a means to simply list the packages present, but again can't really classify this as pass/fail by nature.

4.4 Scan and rebuild the images to include security patches 

Requires running same command as previous step, except this time evaluating packages to determine that the most up to date version is installed. 

4.7 Do not use update instructions alone in the Dockerfile

Requires inspection of history in the images, and looking for update instructions in a single line. Undesirable as "Adding the update instructions in a single line on the Dockerfile will cache the update layer. Thus, when you build any image later using the same instruction, previously cached update layer will be used. This could potentially deny any fresh updates to go in the later builds." 

While Not Scored, might be possible to flag a fail due to looking for update statements.

4.8 Remove setuid and setgid permissions in the images

Requires reviewing executables in the image with setuid/setgid permissions, and ensuring that they are "legitimate". THerefore, manual review is required, cannot flag as pass/fail by default

 4.9 Use COPY instead of ADD in Dockerfile
 
 Requires inspecting the file - could flagg as "fail" based on presence of ADD statements.
 
 4.10 Do not store secrets in Dockerfiles 
 
 Requires inspection of history, though "secrets" are illdefined in the Benchmark document.
 
 4.11 Install verified packages only
 
 Inspect history, use GPG keys or other secure mechanisms to validate authenticity of packages.
 
