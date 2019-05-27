from setuptools import setup, find_packages

setup(
    name='psp',
    version='1.1',
    author='Parshuram S. Patil',
    author_email='parasharam_patil@ymail.com',
    description='Learning python App',
    long_description=open('README.md').read(),
    # py_modules=['python_core.main'],   # used if command file is at root level
    packages=find_packages(),   # this ex. also works with py_modules
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        # main=python_core.main:cli
        psp=python_core.main:psp
    ''',
)
