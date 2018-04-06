from distutils.core import setup

setup(
  name = 'pymediawiki',
  packages = ['pymediawiki'], 
  version = '0.1',
  description = 'Python Wrapper for MediaWiki API',
  author = 'Simon De Greve',
  author_email = 'degrevesim@gmail.com',
  url = 'https://github.com/Yoiro/pymediawiki', 
  download_url = 'https://github.com/Yoiro/pymediawiki/archive/0.1.tar.gz', 
  keywords = ['mediawiki', 'api', 'wiki'], 
  classifiers = [
    'Intended Audience :: Developers',
    'License :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  install_requires=[
    'requests>=2.18.4',
  ],
  python_requires='>=3',
)
