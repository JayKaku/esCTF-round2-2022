import py7zr
import tarfile
import rarfile
import zipfile
import base64
from io import BytesIO

def unzip(bio):
	header = str(bio.read(2).hex())
	bio.seek(0)
	
	# 7z
	if header == "377a":
		return py7zr.SevenZipFile(bio, "r").readall()
	
	# tar
	elif header == "1f8b" or header == b"1f00":	
		tar = tarfile.open(fileobj=bio, mode="r:*")
		files = [(info.name, tar.extractfile(info.name)) for info in tar]
		return { name: BytesIO(bio.read()) for name, bio in files if bio }
	
	# rar
	elif header == "5261":	
		rar = rarfile.RarFile(bio)
		files = [(info.filename, rar.read(info)) for info in rar if not info.is_dir()]
		return { name: BytesIO(bio) for name, bio in files }
	
	# zip
	elif header == "504b":
		zip = zipfile.ZipFile(bio)
		files = [(info.filename, zip.read(info)) for info in zip.infolist() if not info.is_dir()]
		return { name: BytesIO(bio) for name, bio in files }
	
	else:
		raise ValueError(f"unknown header {header}")

f = BytesIO(open("file.7z", "rb").read())
path = []
while True:
	files = unzip(f)
	if len(files.items()) != 1:
		print(files)
		break
	name, bio = list(files.items())[0]
	
	if "/" in name:
		folder, file = name.split("/")
	if file != "OpenMe.zip":
		f = bio
		if len(path) == 0:
			path.append(folder)
		path.append(file)
	else:
		full_path = "".join(path);
		print(full_path)
		decoded = base64.b64decode(full_path).decode("utf8")
		print()
		print(decoded)
		pwd = "".join([c for c in decoded if c.isnumeric()])
		
		zip = zipfile.ZipFile(bio)
		print()
		print(zip.read("flag.txt", bytes(pwd, "utf8")).decode("utf8"))
		break
