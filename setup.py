import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'm_stats',
  packages = ['m_stats'],
  version = '0.1.3',
  license='MIT',
  description = 'A statistics and probability library for Python',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = 'Miguel Angel Velez',
  author_email = '',
  url = 'https://github.com/mvelezg99/m_stats',
  download_url = 'https://github.com/mvelezg99/m_stats/archive/0.1.3.tar.gz',
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