from distutils.core import setup

setup(name='pfvis',
      version='1.0',
      description='Visualisation package for (MP)PFNET',
      author='Martin Zellner',
      author_email='martin.zellner@gmail.com',
      packages=['pfvis'],
      requires=['numpy',
                'PFNET',
                'mppfnet',
                'matplotlib',
                'seaborn',
                'ipyplots',
                'networkx'
                ])
