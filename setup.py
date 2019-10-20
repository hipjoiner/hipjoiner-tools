import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hipjoiner',
    version='2019.10.19',
    author='John Pirie',
    author_email='john@thepiries.net',
    description='Pip-installable toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hipjoiner/tools',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'ppath = hipjoiner.tools.ppath:pretty_path',
            'which = hipjoiner.tools.which:which',
        ],
    }
)
