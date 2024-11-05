from setuptools import setup, find_packages


setup(
    name='pointofpresence',
    version='0.1.0',
    author='Tu Nombre',
    author_email='rbardaji@gmail.com',
    description='A Python client library for interacting with the specific API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sci-ndp/pop-py',  # URL de tu repositorio
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
