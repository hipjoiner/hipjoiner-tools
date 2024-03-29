from setuptools import setup, find_namespace_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='hipjoiner-tools',
    version='2019.11.3',
    description='Pip-installable toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hipjoiner/hipjoiner-tools.git',
    author='John Pirie',
    author_email='john@thepiries.net',
    packages=find_namespace_packages(include=['hipjoiner.*']),
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
