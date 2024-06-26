from setuptools import setup, find_packages

setup(
    name='calculator_package',
    version='0.1',
    packages=find_packages(),
    author='Giraj',
    author_email='girajneema1345@gmail.com',
    description='Basic calculator package in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/giraj736/calculator_package',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
