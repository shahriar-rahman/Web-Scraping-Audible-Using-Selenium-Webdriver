from setuptools import find_packages, setup

setup(
    name='selenium_audible',
    packages=find_packages(),
    version='1.2.0',
    description='An automated scraping tool which utilizes Selenium to parse and extract all the available books in '
                'the Audible website.',
    author='Shahriar Rahman',
    license='MIT License',
    author_email='shahriarrahman1101@gmail.com',
    install_requires=[
        'selenium',
        'pandas',
        'openpyxl',
    ],

)
