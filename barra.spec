# -*- mode: python -*-

block_cipher = None


a = Analysis(['barra.py'],
             pathex=['C:\\Users\\chimi\\Desktop\\barras'],
             binaries=[],
             datas=[('C:\\Users\\chimi\\Desktop\\barras\\archivo.txt', '.') , ('C:\\Users\\chimi\\Desktop\\barras\\Generados','Generados') ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='barra',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='C:\\Users\\chimi\\Desktop\\barcode.ico',
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='barra')
