from setuptools import setup, find_packages

setup(
    name='perfectal-education',
    version='0.1.0',
    description='AI-Powered Educational Platform for Multilingual Learning',
    author='Perfectal Education Team',
    author_email='support@perfectal.edu.dz',
    url='https://perfectal.edu.dz',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'transformers>=4.30.2',
        'torch>=2.0.1',
        'flask>=2.3.2',
        'cryptography>=41.0.1',
        'sqlalchemy>=2.0.15',
        'pandas>=2.0.1'
    ],
    extras_require={
        'dev': [
            'pytest>=7.3.1',
            'black>=23.3.0',
            'flake8>=6.0.0'
        ],
        'ai': [
            'tensorflow>=2.12.0',
            'scikit-learn>=1.2.2'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Education :: Computer Aided Instruction (CAI)'
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'perfectal-cli=src.core.cli:main'
        ]
    }
)