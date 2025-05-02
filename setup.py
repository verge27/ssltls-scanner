from setuptools import setup, find_packages

setup(
    name='ssltls-scanner',
    version='0.1.0',
    description='SSL/TLS vulnerability and misconfiguration scanner',
    author='Your Name',
    packages=find_packages(),
    install_requires=['pyOpenSSL'],
    entry_points={
        'console_scripts': [
            'ssltls-scan=scanner.core:main',
        ],
    },
    python_requires='>=3.7',
)
