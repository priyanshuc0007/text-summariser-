from setuptools import setup, find_packages

setup(
    name='text-summariser',
    version='0.1.0',
    packages=find_packages(),  # Automatically find all packages in the project

    # Metadata
    author='priyanshu',
    author_email='priyanshuc111@gmail.com',
    description='Text Summarizer',
    long_description=open('README.md').read(),  # Read the README file for long description
    long_description_content_type='text/markdown',
    url='https://github.com/priyanshuc0007/text-summariser',
    license='MIT',  # Choose an appropriate license
)
