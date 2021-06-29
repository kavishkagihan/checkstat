#!/usr/bin/python3
import sys, os
import concurrent.futures
import requests

url_list = []
prefer_https = None
status_ckeck = None
workers = 50
save = None
headers = False
body = False
from_file = False
save_dir = ""

def usage():
	print("Grepping for URLs according to the status code\n")
	print("Usage:")
	print("   checkstat [OPTIONS]\n")
	print("Opions:")
	print("   -f 		Specify a file to read from")
	print("   -s 		Specify a status code (200,403)")
	print("   -t 		Specify the number of threads")
	print("   -p 		Prefer https over http")
	print("   -I 		Enable saving results")
	print("   -H 		Save response header")
	print("   -B 		Save response body")
	print("   -o 		Specify a output directory")
	print("\nIf you dont specify a status code to search for,\nit will show all the status codes of the responses.")


if '-h' in sys.argv:
	usage()
	exit(0)

if '-t' in sys.argv:
	workers = int(sys.argv[int(sys.argv.index('-t') + 1 )])


if '-s' in sys.argv:
	status_ckeck = True


if '-I' in sys.argv:
	save = True
	if '-H' in sys.argv:
		headers = True

	if '-B' in sys.argv:
		body = True


if '-f' in sys.argv:
	from_file = True
	file = sys.argv[int(sys.argv.index('-f') + 1 )]

	try:
		with open(file) as f:
			file_content = f.readlines()
			f.close()

	except Exception as e:
		print("ERROR: ", e)


if save:
	if "-o" in sys.argv:
		try:
			save_dir = str(sys.argv[int(sys.argv.index('-o') + 1 )])
		except Exception as e:
			print("ERROR: specify a directory to save the results (-o save_dir)")
			exit(1)

if '-p' in sys.argv:
	prefer_https = True


if not from_file:
	for line in sys.stdin:
		url_list.append(line.rstrip())

else: 
	for line in file_content:
		url_list.append(line.rstrip())


def req(url):
	global workers

	try:
		if ("http://" in url) or ("https://" in url):
			pass

		else:
			if prefer_https:
				url = "https://" + url
			else:
				url = "http://" + url

		r = requests.get(url) 

		if status_ckeck:
			code = sys.argv[int(sys.argv.index('-s') + 1 )]
			if r.status_code == int(code.strip()):
				print(url)
		else:
			print(url + ' '*(len(url) + 5) + str(r.status_code))

		if save:
			os.system(f'mkdir {save_dir} 2>/dev/null')

			if headers:
				with open(save_dir + '/' + url.replace("/", ":")+'.headers' , 'w') as f:
					for header in r.headers:
						f.writelines((header.strip(),": " ,r.headers[header] + '\n'))
					f.close()

			if body:
				with open(save_dir + '/' + url.replace("/", ":")+'.body' , 'w') as f:
					f.writelines(r.text)
					f.close()

	except Exception as e:
		exit(1)

with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
	ex.map(req ,url_list)