import os
import shutil
import filetype as ft
from gzip import GzipFile
from bz2 import BZ2File
from rarfile import RarFile
from zipfile import ZipFile
import tarfile

def unpack(file_name, extract_path=None):

	dirname, basename = os.path.split(os.path.abspath(file_name))
	is_dir = os.path.isdir(file_name)
	is_file = os.path.isfile(file_name)

	if not extract_path and is_dir:
		unpack_dir(file_name)
	elif not extract_path and is_file:
		unpack_file(file_name)
	elif file_dir_name == extract_path and is_dir:
		unpack_dir(file_name)
	elif file_dir_name == extract_path and is_file:
		unpack_file(file_name)
	else:
		if not os.path.exists(extract_path):
			os.makedirs(extract_path)
		if is_dir:
			shutil.copytree(file_name, extract_path)
			unpack_dir(extract_path + "/" + basename)
		elif is_file:
			shutil.copy(file_name, extract_path)
			unpack_file(extract_path + "/" + basename)

def unpack_dir(directory):
	for root, dirs, dirfiles in os.walk(directory):
		for name in dirfiles:
			full_name = root + "/" + name
			unpack_file(full_name)

def unpack_file(fname):
	if ft.is_compression(fname) or ft.is_archived(fname):	
		if ft.is_compression(fname):
			new_file = decompress(fname)
		elif ft.is_archived(fname):
			new_file = unarchive(fname)
	
		if fname != new_file:
			os.remove(fname)
		
		if os.path.isdir(new_file):
			unpack_dir(new_file)
		else:
			unpack_file(new_file)
		
def decompress(fname):
	ftype = ft.get_type(fname)
	
	if ftype == "gz":
		ext = GzipFile(fname, 'rb')
	elif ftype == "bz2":
		ext = BZ2File(fname, 'rb')

	filedata = ext.read()
	new_name = get_new_name(fname[:fname.rfind(".")])
	with open(new_name, "w") as w:
		w.write(filedata)

	new_type = ft.get_type(new_name)
	if new_type:
		new_plus_type = get_new_name(new_name + "." + new_type)
		os.rename(new_name, new_plus_type)
		return new_plus_type
	return new_name

def unarchive(fname):
	ftype = ft.get_type(fname)
	
	if ftype == "rar":
		ext = RarFile(fname)
	elif ftype == "tar":
		ext = tarfile.open(fname)
	elif ftype == "zip":
		ext = ZipFile(fname)

	new_path = get_new_name(fname[:fname.rfind(".")] + "_extracted")
	if not os.path.exists(new_path):
		os.makedirs(new_path)
	ext.extractall(path=new_path)
	return new_path

def flatten_folder(base_dir):
	
	for root, dirs, files in os.walk(base_dir):
		if root != base_dir:
			for name in files:
				new_name = get_new_name(base_dir + "/" + name)
				shutil.move(root + "/" + name, new_name)
	for root, dirs, files in os.walk(base_dir):
		for d in dirs:
			shutil.rmtree(os.path.join(root, d))

def get_new_name(fname):
	if not os.path.exists(fname):
		return fname
	if fname.find(".") < 0 or fname.rfind(".") < (len(fname) - 5):
		is_dir = True
	else:
		is_dir = False
	count = 1
	while True:
		count_val = "(" + str(count) + ")"
		if is_dir:
			temp_name = fname + count_val
		else:
			temp_name = fname[:fname.rfind(".")] + count_val + fname[fname.rfind("."):]
		if not os.path.exists(temp_name):
			return temp_name
		count += 1
