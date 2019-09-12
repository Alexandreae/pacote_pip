from setuptools import setup

setup(name='my_hello_alexandreae',
      author='Alexandre Edington',
      version='0.1',
      packages=['my_hello'],
      python_requires='>=3.6',
      classifiers=[
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3'
          ],
      install_requires=[
          'Ipython>1.0'
      ],
      scripts=['scripts/hello.py']
      )     