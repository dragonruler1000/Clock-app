# -*- mode: python ; coding: utf-8 -*-
import os, sys


a = Analysis(
    ['gui-main.py'],
    pathex=[],
    binaries=[],
    datas=[('themes', 'themes')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

if sys.platform.startswith('linux'):
    a.binaries = [b for b in a.binaries if not b[0].startswith('libfontconfig')]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='clock-app-' + os.environ.get('MATRIX_NAME', 'local'),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
