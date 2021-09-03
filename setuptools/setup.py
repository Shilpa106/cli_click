from setuptools import setup
setup(
    name='test',
    version='0.1.0',
    py_modules=['test'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'test = test:cli',
        ],
    },

)