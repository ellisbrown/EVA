from setuptools import setup, find_packages

setup(
    name='eva_clip',
    version='0.1',
    packages=find_packages(where='rei'),
    package_dir={'': 'rei'},
    install_requires=[
        # You can automatically capture your dependencies from the requirements.txt file:
        line.strip() for line in open('requirements.txt', 'r').readlines()
    ],
    include_package_data=True,
)
