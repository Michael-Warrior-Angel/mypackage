from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python packages',
    long_description=open('README.md').read(),
    install_required=['numpy'],
    url='https://github.com/Michael-Warrior-Angel/mypackage',
    author='Michael K. Tessema',
    author_email='mikykassahun@gmail.com'
)