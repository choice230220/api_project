# setup.py ㅍ파일이 있으면 pip로 설치 가능
from setuptools import setup

setup(
    name = 'myapi', # 이 이름으로 패키지가 설치됨
    version = '0.0.1',
    description= 'my api lib',
    url = 'https://github.com/sfdjkd/api_project.git',
    author = 'sfhui',
    author_email= 'chgml9326@hanyang.ac.kr',
    packages= ['my_api'],
    install_requires = [
        'requests'
    ]
)