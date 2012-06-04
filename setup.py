from setuptools import setup

setup(name='python-unpack',
      description='Python module to unarchive, decompress, and flatten folders',
      author='Mike Jensen',
      author_email='jjensen.mike@gmail.com',
      url='https://github.com/jjensenmike/python-unpack',
      version='0.1',
      py_modules=['unpack'],
      license='PSF',
      install_requires=["python-magic >= 0.4.1","python-unpack >= 0.1","rarfile"],
      )
