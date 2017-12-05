from setuptools import setup, find_packages


setup(
    name="Finger balabolka Server",
    version='1.0.8',
    description="A alfa project of flood chat.",
    long_description="A flood chat project on ptyhon 3 and PyQt5",
    author="Artem Sukharenko",
    author_email="truecyxapic@yandex.ru",
    url="https://github.com/Cyxapic/fb_server",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['Flood chat server', 'chat PyQt 5', 'server jim chat'],
    packages=find_packages('fb_server'),
    package_dir={'':'fb_server'},
    install_requires=[
        "SQLAlchemy==1.1.14",
    ],
    extras_require={
        'dev': ['flake8==3.4.1',],
        'test': ["pytest==3.2.2",
                 "pytest-cov==2.5.1",
                 "pytest-sugar==0.9.0",
                 "PyYAML==3.12",],
    },
    entry_points={
         'console_scripts': [
            'finger_server=fb_server.main:main',
        ],
    },
)