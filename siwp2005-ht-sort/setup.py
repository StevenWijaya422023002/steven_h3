from setuptools import setup, find_packages

setup(
    name='siwp2005_stevenwijaya_sorting',
    version='0.1.9',
    description='Package that includes multiple sorting methods',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/StevenWijaya422023002/steven_h3.git',
    author='Steven Wijaya',
    author_email='steven.422023002@civitas.ukrida.ac.id',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)
