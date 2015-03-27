# -*- mode: python -*-
a = Analysis(['test_game.py'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='test_game.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
res = Tree('res', prefix='res')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               res,
               strip=None,
               upx=True,
               name='test_game')
