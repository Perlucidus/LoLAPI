from setuptools import setup, find_packages

setup(name='lolapi',
      version='1.0.1',
      description='League of Legends API',
      url='https://github.com/Perlucidus/LoLAPI',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['requests'],
      license='MIT'
      )
