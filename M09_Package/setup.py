from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Cameron Preasmyer',
    author_email='spc6uz@virginia.edu',
    description='A simple package for book lovers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://https://github.com/Preasmyer/M09-Packages',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
