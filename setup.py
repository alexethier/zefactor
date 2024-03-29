import os
from setuptools import setup

found_packages = []
found_package_dirs = {}
project_name = "zefactor"
for root, dirs, files in os.walk("." + os.path.sep + project_name, topdown=True, followlinks=False):
  for name in files:
    if(name=="__init__.py"):
      package_key = root[2:]
      #print("Found package: " + package_key)
      found_packages.append(package_key)
      found_package_dirs[package_key] = "." + os.path.sep + package_key

#print(found_packages)
#print(found_package_dirs)

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name=project_name,
  version='2.0.0',
  description='Flexible find and replace for refactoring projects.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/alexethier/zefactor',
  author='Alex Ethier',
  author_email='aethier@gmail.com',
  license='MIT',
  packages=found_packages,
  package_dir=found_package_dirs,
  install_requires=["zind", "zompt"],
  classifiers=[
      'Development Status :: 1 - Planning',
      'License :: OSI Approved :: BSD License',  
      'Operating System :: POSIX :: Linux',        
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
  ],
  entry_points={
      'console_scripts': [
          'zefactor=zefactor.run.runner_manager:main',
      ],
  },
)
