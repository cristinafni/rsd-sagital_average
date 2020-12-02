from setuptools import setup, find_packages

setup(
    name="sagital",
    version="0.1.0",
    packages=find_packages(),
    entry_points={'console_scripts': [
        'run_averages= sagital.command:process']}
)
