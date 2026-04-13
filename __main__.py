import argparse
import zipfile
from lxml import etree
from datetime import datetime
from pathlib import Path
import uuid

root = Path("/storage/emulated/0/Download/gsmaps/")

class Setup:
	def __init__(self,
		mod, mod_version, 
		compress_mod, compress_textures, 
		resize_textures, astc_blocks_size, 
		format_xml, save_method, dirname
	):
		if Path(mod).absolute().exists():
			self.mod = str(Path(mod).absolute())
			self.mod_version = mod_version
			self.compress_mod = compress_mod
			self.compress_textures = compress_textures
			self.resize_textures = resize_textures
			self.astc_blocks_size = astc_blocks_size
			self.format_xml = format_xml
			self.method = save_method
			self.dirname = dirname
			self.temp_mod_dir = str(root / "mods" / str(uuid.uuid4()))
			if self.mod_version == "fs22" or str(Path(self.mod).stem)[:4].lower() == "fs22":
				self.create_setup_file()
			else:
				print("Set the game version or index a mod with the FS22 prefix.")
		else:
			print(f"The mod could not be found: {Path(mod).absolute()};")
	def create_setup_file(self):
		Path(self.temp_mod_dir).mkdir(parents=True)
		filename = Path(self.temp_mod_dir) / "setup.xml"
		root = etree.Element("setup")
		root.set("mod", self.mod)
		tree = etree.ElementTree(root)
		tree.write(filename, standalone=False, xml_declaration=True)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="gsmaps", description=None, epilog="Currently, the converter only supports Farming Simulator 2022 mods.")
	parser.add_argument("-m", "--mod", required=True, help=None)
	parser.add_argument("-v", "--mod-version", required=False, choices=["fs19", "fs22", "fs25"], help=None)
	parser.add_argument("-c", "--compress-mod", default=False, action="store_true", help=None)
	parser.add_argument("-t", "--compress-textures", default=False, action="store_true", help=None)
	parser.add_argument("-r", "--resize-textures", default=False, action="store_true", help=None)
	parser.add_argument("-a", "--astc-blocks-size", default="6x6", choices=["4x4", "5x4", "5x5", "6x5", "6x6", "8x5", "8x6", "8x8", "10x5", "10x6", "10x8", "10x10", "12x10", "12x12"], help=None)
	parser.add_argument("-x", "--format-xml", default=False, action="store_true", help=None)
	parser.add_argument("-s", "--save-method", default="replace", choices=["add", "replace"], help=None)
	parser.add_argument("-d", "--dirname", default="mapDE", choices=["map", "mapDE"], help=None)
	args = vars(parser.parse_args())
	Setup(**args)