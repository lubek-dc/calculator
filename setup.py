from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/myusername/my_library_name',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of my library',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        # list any dependencies here
    ],
)