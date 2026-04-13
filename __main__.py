import argparse
import zipfile
from lxml import etree
from datetime import datetime
from pathlib import Path
import uuid

root = Path("/storage/emulated/0/Download/gsmaps/")
"""teste"""
class Setup:
	def __init__(self,
		mod, mod_version, 
		pack_mod, compress_textures, 
		resize_textures, astc_blocks_size, 
		format_xml, save_method, dirname
	):
		if Path(mod).absolute().exists():
			self.mod = str(Path(mod).absolute())
			self.mod_version = mod_version
			self.pack_mod = pack_mod
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

class Settings:
	def __init__(self, fs19, fs20, fs22, fs23, fs25, fs26):
		self.fs19_assets = ""
		self.fs20_assets = ""
		self.fs22_assets = ""
		self.fs23_assets = ""
		self.fs25_assets = ""
		self.fs26_assets = ""
	def check_settings(self):
		pass

class Help:
	modfile = "This is a zip file for conversion; the file name must include the game version prefix, otherwise it must be specified."
	modversion = "The version for which the mod was created, allowing you to adjust the conversion method for a specific game version. Necessary in cases where the mod does not have a version prefix."
	packaging = "Package the mod after conversion; note that only GAR can be used directly in Farming Simulator. If packaged as a zip file, it must be extracted and placed as a folder in the game."
	textcomp = "Compresses the mod's textures for GS2D, making the mod lighter and the textures optimized for mobile."
if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="gsmaps", description=None, epilog="Currently, the converter only supports Farming Simulator 2022 mods.")
	subparsers = parser.add_subparsers(dest="command", help=None)
	settings = subparsers.add_parser("settings", help=None)
	settings.add_argument("-fs19", "--fs19-assets", required=False, type=str, help=None)
	settings.add_argument("-fs20", "--fs20-assets", required=False, type=str, help=None)
	settings.add_argument("-fs22", "--fs22-assets", required=False, type=str, help=None)
	settings.add_argument("-fs23", "--fs23-assets", required=False, type=str, help=None)
	settings.add_argument("-fs25", "--fs25-assets", required=False, type=str, help=None)
	settings.add_argument("-fs26", "--fs26-assets", required=False, type=str, help=None)
	convert = subparsers.add_parser("convert", help=None)
	convert.add_argument("-m", "--mod", required=True, help=Help.modfile)
	convert.add_argument("-v", "--mod-version", required=False, choices=["fs19", "fs22", "fs25"], help=Help.modversion)
	convert.add_argument("-p", "--pack-mod", default=False, choices=["zip", "gar"], help=Help.packaging)
	convert.add_argument("-t", "--compress-textures", default=False, action="store_true", help=Help.textcomp)
	convert.add_argument("-r", "--resize-textures", default=False, action="store_true", help=None)
	convert.add_argument("-a", "--astc-blocks-size", default="6x6", choices=["4x4", "5x4", "5x5", "6x5", "6x6", "8x5", "8x6", "8x8", "10x5", "10x6", "10x8", "10x10", "12x10", "12x12"], help=None)
	convert.add_argument("-x", "--format-xml", default=False, action="store_true", help=None)
	convert.add_argument("-s", "--save-method", default="replace", choices=["add", "replace"], help=None)
	convert.add_argument("-d", "--dirname", default="mapDE", choices=["map", "mapDE"], help=None)
	args = parser.parse_args()
	if args.command == "convert":
		Setup(**vars(args))
	elif args.command == "settings":
		print(args)
"""

gsmaps settings

gsmaps converter


import argparse

def main():
    # 1. Configuração do parser principal
    parser = argparse.ArgumentParser(description="Meu app com submódulos")
    subparsers = parser.add_subparsers(dest="comando", help="Submódulos disponíveis")

    # 2. Criando o submódulo 'config'
    parser_config = subparsers.add_parser('config', help='Configurações do sistema')
    # Esta flag --user só existirá dentro de 'config'
    parser_config.add_argument('--user', type=str, help='Define o usuário')

    # 3. Criando o submódulo 'run'
    parser_run = subparsers.add_parser('run', help='Executa uma tarefa')
    # Esta flag --priority só existirá dentro de 'run'
    parser_run.add_argument('--priority', type=int, default=1, help='Nível de prioridade')

    args = parser.parse_args()

    # Lógica de execução baseada no comando escolhido
    if args.comando == 'config':
        print(f"Configurando para o usuário: {args.user}")
    elif args.comando == 'run':
        print(f"Executando com prioridade: {args.priority}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
"""