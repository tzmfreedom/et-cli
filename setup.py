from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name = "et-cli",
    version = "0.0.1",
    packages=['etcli'],
    description='ExactTarget CLI Tool',
    long_description=readme,
    url='https://github.com/tzmfreedom/et-cli',
    author='makoto tajitsu',
    author_email='makoto_tajitsu@hotmail.co.jp',
    license='MIT',
    scripts=['bin/et'],
    install_requires=[
        'FuelSDK',
    ],
)
