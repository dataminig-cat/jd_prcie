# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
              pathex=['E:\\�����ھ���Ŀ\\����������\\jd_price','C:\\Users\\33171\\AppData\\Local\\Programs\\Python\\Python37'],
             binaries=[],
             datas=[(r'data\python.ico',r'.\data'),(r'data\c08f5b9802f56855.jpg',r'.\data'),
             (r'setting.json','.')],
             hiddenimports=['pymysql','numpy.core._dtype_ctypes','crawler.spiders','crawler.pipeline'], # �޷��Զ�����İ�
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
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,icon="data/python.ico")
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='run')
