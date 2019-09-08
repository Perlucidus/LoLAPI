from setuptools import setup, find_packages

setup(name='lolapi',
      version='1.0',
      description='League of Legends API',
      url='https://github.com/Perlucidus/LoLAPI',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      requires=['requests'],
      license='MIT'
      )
