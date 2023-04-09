# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['../../src/pymapconv.py'],
    pathex=['../../src'],
    binaries=[],
    datas=[
        ('../../resources/*', 'resources'),
        ('../../LICENSE', '.'),
        ('../../README.md', '.')
    ],
    hiddenimports=list(stdlib_list.stdlib_list()),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
a.exclude_system_libraries()
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pymapconv',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='pymapconv',
)
