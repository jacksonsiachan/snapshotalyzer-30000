from setuptools import setup

setup (
    name = 'Snapshotalyzer-30000',
    version = '0.1',
    author = "Jackson Chan",
    author_email = "jacksonsiachan@gmail.com",
    description = "Snapshotalyzer 30000 is a tool to manage AWS EC2 snapshots.",
    license = "GPLv3+",
    packages = ['shotty'],
    url = "https://github.com/jacksonsiachan/snapshotalyzer-30000",
    install_requires = [
        'click',
        'boto3'
    ],
    entry_points = '''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',    
)