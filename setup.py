from distutils.core import setup
setup(
  name = 'm_stats',
  packages = ['m_stats'],
  version = '0.1.1',
  license='MIT',
  description = 'A statistics and probability library for Python',
  author = 'Miguel Angel Velez',
  author_email = 'mvelezg99@gmail.com',
  url = 'https://github.com/mvelezg99',
  download_url = 'https://github.com/mvelezg99/m_stats/archive/0.1.1.tar.gz',
  keywords = ['Python', 'statistics', 'probability', 'm_stats'],
  install_requires=[
          'numpy',
          'm_stats',
          'scipy',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)