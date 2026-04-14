from pathlib import Path
from lxml import etree
import zipfile

class _util_pallet_convert:
    def __init__(self, filename, save): pass
    def config(self): pass
    def i3d(self): pass
    def textures(self): pass
    def shaders(self): pass
    
class FillTypes:
    def __init__(
        self,
        file=None,
        fs23=None,
        fs22=None,
        languages=None,
        convert_pallets=False,
        compress_textures=False
    ):
        self.file = file
        self.fs23 = fs23
        self.fs22 = fs22
        self.l10n = languages
        self.convert_pallets = convert_pallets
        self.compress_textures = compress_textures

    def textures(self): pass
    def images(self): pass
    def pallet(self): pass
    def translations(self): pass
    
    def assets(self, path):
        if Path(path).is_dir(): return 'dir'
        else:
            try:
                if zipfile.is_zipfile(path): return 'zip'
                else: return None
            except Exception as error: print('falha na verificações. Erro:', error)

if __name__ == '__main__':
    file = ''
    fs23 = 'D:/Documentos/fs23_data.zip'
    fs22 = 'D:/Documentos/farming simulator 2022/data/'
    languages = None
    FillTypes(file, fs23, fs22, languages, True)