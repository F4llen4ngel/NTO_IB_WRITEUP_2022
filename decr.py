import os

files = [
"var/www/html/index.php.encr",
"var/www/html/xmlrpc.php.encr",
"var/www/html/authorize.php.encr",
"var/www/html/cron.php.encr",
"var/www/html/install.php.encr",
"var/www/html/19FLAG.txt.encr",
"var/www/html/update.php.encr",
"var/www/html/shell.php.encr"
]


for filename in files:
	with open(filename, "r") as f:
		decrypt_cmd = f"cat {filename} | base64 -d | openssl enc -aes-256-cbc -d -a -salt -in {filename} -out {filename + '.decrypted'} -pass pass:2286C8B299 -iv 40C827B72C7494AD3D92B7D4F752846C"
		os.system(decrypt_cmd)
