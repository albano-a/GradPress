# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['kraken.py'],
    pathex=['C:/Users/Icarl/Documents/GitHub/pressao/kraken.py'],
    binaries=[],
    datas=[('uploads', 'uploads'), ('img', 'img'), ('utility', 'utility')
    ('C:\Users\Icarl\AppData\Local\Programs\Python\Python312\Lib\site-packages\scienceplots\styles', '_internal\\scienceplots\\styles')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    win_no_refer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    exclude_binaries=True,
    name='kraken_v0.1.1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Icarl\\Documents\\GitHub\\pressao\\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='kraken_v0.1.1',
)
