import json
import sys
from pyfiglet import Figlet
from colorama import Fore, Back, Style 
import os

custom_fig = Figlet(font='doom')
# help_text = "\n\nPlease enter command as --{runtime} {container_id} to apply benchmark tests on the associated container image\n\nExample: interoperable_image_app --crio 123134"

# Configuration paths and attributes, Docker
config_path_docker = "/var/lib/docker/containers/{}/config.v2.json"
image_file_path_docker = "/var/lib/docker/image/overlay2/imagedb/content/sha256/{}"
image_hash_id_docker = "Image"


# Configuration paths and attributes, CRI-O
config_path_crio = "/var/lib/containers/storage/overlay-containers/{}/userdata/config.json"
image_overlay_crio = "/var/lib/containers/storage/overlay-images/images.json"
image_file_path_crio = "/var/lib/containers/storage/overlay-images/{}"

# Configuration paths and attributes, containerd

image_file_ctrd = "/var/lib/containerd/io.containerd.content.v1.content/blobs/sha256/{}"

# image file attributes
config_key = "config"
user_key = "User"
health_key = "Healthcheck"
history_key = "history"

# Benchmark check strings
Fp1 = "CIS 4.1: Create a user for the conatiner: "
Fp6 = "CIS 4.6: Add HEALTHCHECK instruction to the container image: "
Fp9 = "CIS 4.9: Use COPY instead of ADD in Dockerfile: "

# helper to print help function
def help_func():
	if sys.argv[1] and sys.argv[1] == "--help" or sys.argv[1] == "--h":
		print("\nPlease enter command as --<runtime> <container_id> to apply benchmarks on image container is running")
		print("Example: interoperable_image_app --crio 123134\n")
		return True
	return False

# define checks in Docker
def docker_inspect_image():
	global config_path_docker
	global image_file_path_docker
	global image_hash_id_docker
	global config_key
	global user_key
	global health_key
	global history_key

	if sys.argv[1] and sys.argv[1] == "--docker" or sys.argv[1] == "--d":
		config_path_docker = config_path_docker.format(sys.argv[2])
		# open docker container configuration file to get image id
		with open(config_path_docker) as config_json:
			config_data = json.load(config_json)
			# hash includes 'sha256:' to indicate hashtype, split off since image folder only includes ID
			image_id = config_data[image_hash_id_docker].split(':')[1]
			# format image file path
			image_file_path_docker = image_file_path_docker.format(image_id)
			with open(image_file_path_docker) as image_json:
				image_data = json.load(image_json)
				# userid and healthcheck are sub attributes of config attribute
				image_config = image_data[config_key]
				# 4.1, user created
				userid = image_config[user_key] if image_config[user_key] is not '' else 'NOT SET!'
				# 4.6, healthcheck instruction exists
				healthcheck = image_config[health_key] if health_key in image_config else 'NOT SET!'
				# history is its own attibute, stores a new line for each history line
				# 4.9, Use Copy not Add
				history = image_data[history_key]
				# print result of each check
				if userid == 'NOT SET!':
					print(Fore.RED + f"{Fp1} FAILURE, USER ID {userid}")
					print(Style.RESET_ALL + '')
				else:
					print(Fore.GREEN + f"{Fp1} PASS, USER ID = {userid}")
					print(Style.RESET_ALL + '')
				if healthcheck == 'NOT SET!':
					print(Fore.RED + f"{Fp6} FAILURE, HEALTHCHECK INSTRUCTIONS {healthcheck}")
					print(Style.RESET_ALL + '')
				else:
					print(Style.GREEN + f"{Fp6} PASS, HEALTHCHECK INSTRUCTIONS {healthcheck}")
					print(Style.RESET_ALL + '')
				print(f'{Fp9}')
				for x in history: print(f'{x}')
		return True
	return False

def main():
	print(custom_fig.renderText('Interoperable Image!!'))
	if help_func():
		return
	#elif crio_inspect_image():
	#    return
	elif docker_inspect_image():
		return
	#elif ctrd_inspect_image():
	#   containerd_utils()
	else:
		print("Please use --help command for more information")

if __name__== "__main__":
	main()
	