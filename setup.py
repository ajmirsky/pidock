from setuptools import setup

setup(name='pidock',
      version='0.1',
      description='Create raspberry pi disk images with a Dockerfile',
      url='https://github.com/eringr/pidock',
      author='Flying Circus',
      author_email='hens0093@gmail.com',
      license='GNU General Public License v3',
      packages=['pidock'],
      scripts=['bin/pidock'],
      zip_safe=False,
      include_package_data=True
      )
