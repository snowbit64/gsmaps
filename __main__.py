import argparse
import zipfile
from pathlib import Path

root = Path(__file__).parent

class Setup:
	def __init__(self, mod, mod_version, compress_mod, compress_textures, resize_textures, astc_blocks_size, format_xml):
		self.mod = mod
		self.mod_version = mod_version
		self.compress_mod = compress_mod
		self.compress_textures = compress_textures
		self.resize_textures = resize_textures
		self.astc_blocks_size = astc_blocks_size
		self.format_xml = format_xml
		if self.mod_version == "fs22" or str(Path(self.mod).stem)[:4].lower() == "fs22":
			self.generate_setup()
		else:
			print("Set the game version or index a mod with the FS22 prefix.")

	def generate_setup(self):
		pass
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="gsmaps", description=None, epilog="Currently, the converter only supports Farming Simulator 2022 mods.")
	parser.add_argument("-m", "--mod", required=True, help=None)
	parser.add_argument("-v", "--mod-version", required=False, choices=["fs19", "fs22", "fs25"], help=None)
	parser.add_argument("-c", "--compress-mod", default=False, action="store_true", help=None)
	parser.add_argument("-t", "--compress-textures", default=False, action="store_true", help=None)
	parser.add_argument("-r", "--resize-textures", default=False, action="store_true", help=None)
	parser.add_argument("-a", "--astc-blocks-size", default="6x6", choices=["4x4", "5x4", "5x5", "6x5", "6x6", "8x5", "8x6", "8x8", "10x5", "10x6", "10x8", "10x10", "12x10", "12x12"], help=None)
	parser.add_argument("-x", "--format-xml", default=False, action="store_true", help=None)
	args = vars(parser.parse_args())
	Setup(**args)
"""
-m, --mod,
-v, --mod-version (ex: fs19, fs22, fs25) *Obs: It only accepts fs22 as it is not compatible with other versions.
-c, --compress **Obs: Compress the mod into a .gar file, not a zip file.
-t, --textures-compress
-r, --resize-textures
-a, --astc-blocks-size
"""
""" astc blocks available
4x4: 8.00 bpp        10x5: 2.56 bpp
5x4: 6.40 bpp        10x6: 2.13 bpp
5x5: 5.12 bpp         8x8: 2.00 bpp
6x5: 4.27 bpp        10x8: 1.60 bpp
6x6: 3.56 bpp       10x10: 1.28 bpp
8x5: 3.20 bpp       12x10: 1.07 bpp
8x6: 2.67 bpp       12x12: 0.89 bpp
"""