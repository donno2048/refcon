from sys import modules
a = Analysis(['restricted-functions/ref/__main.py'],
             datas=[('restricted-functions/ref/__init__.py', '.'), (modules["site"].__file__, '.')],
             hiddenimports=['_sitebuiltins', 'sysconfig'])
exe = EXE(PYZ(a.pure, a.zipped_data), a.scripts, a.binaries, a.zipfiles, a.datas, [], name='refcon', upx=True)