from setuptools import setup, find_packages

setup(
    name='xtquant',
    version='24.10.14',
    author='albert',
    author_email='iqqg@outlook.com',
    description='QMT xtquant library',
    packages=find_packages(include=['xtquant', 'xtquant.*']),
    package_data={
        'xtquant': [
            '*.pyd',
            '*.dll',
            '*.ini',
            '*.log4cxx',
            # 如果你需要包含子目录中的文件，可以进一步指定，例如：
            # 'config/*',
            # 'doc/*',
            # 'metatable/*',
            # 'qmttools/*',
            # 'xtbson/*'
        ]
    },
    install_requires=[
        # 列出该包依赖的其他 Python 包，例如：
        # 'numpy',
        # 'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
    