from distutils.core import setup
import setuptools

def read (filename):
  file = open(filename)
  text = file.read()
  file.close()
  return text

setup(
  name = 'vkhealth',
  version = '0.6',
  description = 'Module that shows the current health of the VKontakte platform',
  long_description=read('README.rst'),
  packages=setuptools.find_packages(),
  author = 'Daniil Chizhevskij',
  author_email = 'daniilchizhevskij@gmail.com',
  url = 'https://github.com/DaniilChizhevskii/vkhealth',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
  ],
)