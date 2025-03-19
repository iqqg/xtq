from setuptools import setup, find_packages

setup(
    name='xtquant',
    version='xtquant241014.1.2',
    # py_modules=['xttools', 'xtdata', 'xttrader', 'xttype', 'xtutil', 'xtconstant', 'xtconn', 'xtdata_config', 'xtdatacenter', 'xtextend', 'xtview'],
    # package_dir={'': '.'},
    packages=['xtquant', 'xtbson', 'qmttools', 'metatable'],
    description='QMT xtquant library',
    author='albert',
    author_email='iqqg@outlook.com',
    install_requires=[],
)