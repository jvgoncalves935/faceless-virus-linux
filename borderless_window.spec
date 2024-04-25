# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['borderless_window.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
		"tkinter"
	],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

a.datas += [
	('nicolexd.png','/mnt/c/Users/jvgon/Documents/Programming/Python/faceless-virus-linux/nicolexd.png', 'DATA'),
	('FACELESSGAMES.COM.BR_ACELERADO_BLZ.mp3','/mnt/c/Users/jvgon/Documents/Programming/Python/faceless-virus-linux/FACELESSGAMES.COM.BR_ACELERADO_BLZ.mp3', 'DATA')]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='borderless_window',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['mara.png'],
)
