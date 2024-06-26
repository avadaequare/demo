from setuptools import setup, find_packages

setup(
    name='demo',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask==3.0.3',  # Adjust versions as per your requirements
        # Add other dependencies from your requirements.txt
    ],
)
