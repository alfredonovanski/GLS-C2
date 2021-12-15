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

def result():
	try:
		os.system("curl {} -o cute_lulu3.png".format(URL))
	except Exception:
		print("Error")
	print("[!] Image Downloaded")

	with open('cute_lulu2.png', 'rb') as img:
		image = Image(img)
	check_payload = base64.b64decode(image.copyright).decode()
	print("Executed Payload Result: \n")
	print(check_payload)

def main():
	global URL

	cmd_args, gopt = getopt(argv[1:], "u:", ["url="])
	if not cmd_args:
		print(usage_text)
		sys.exit()

	for opt, val in cmd_args:
		if(opt in ["-u", "--url"]):
			URL = val
	result()

if __name__ == "__main__":
	main()