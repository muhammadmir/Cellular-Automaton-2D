from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/storborg/funniest',
      author='Muhammad Mir',
      author_email='mmir@drew.edu',
      license='MIT',
      packages=['2DCellularAutomaton'],
      install_requires=[
          'bitarray',
          'Pillow'
      ],
      zip_safe=False)
