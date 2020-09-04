from os import path
from setuptools import setup, find_packages


def readme():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name='moodle-dl',
    version='1.9.1',
    description='A Moodle downloader that downloads course content fast from Moodle (eg. lecture pdfs)',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/C0D3D3V/Moodle-Downloader-2',
    author='C0D3D3V',
    license='GPL-3.0',
    packages=find_packages(),
    entry_points={'console_scripts': ['moodle-dl = moodle_dl.main:main',],},
    python_requires='>=3.6',
    install_requires=[
        'sentry_sdk>=0.13.5',
        'colorama>=0.4.3',
        'readchar>=2.0.1',
        'youtube_dl>=2020.5.29',
        'certifi>=2020.4.5.2',
        'html2text>=2020.1.16',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Utilities',
    ],
    zip_safe=False,
)