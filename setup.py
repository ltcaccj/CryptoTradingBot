from setuptools import setup, find_packages

setup(
    name="CryptoTradingBot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ccxt",
        "pandas",
        "numpy",
        "python-binance"
    ],
    entry_points={
        'console_scripts': [
            'cryptotradingbot=main:main',
        ],
    },
    author="ltcaccj",
    author_email="your_email@example.com",
    description="A cryptocurrency trading bot for Binance",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/ltcaccj/CryptoTradingBot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
