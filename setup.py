#!/usr/bin/env python3
# setup.py

import setuptools
from distutils.core import setup, Extension
from distutils.command.build import build
from setuptools.command.build_py import build_py as _build_py

class build_py(_build_py):
    def run(self):
        self.run_command("build_ext")
        return super().run()



colgraph_module = Extension('libcolgraph.libcc._libcolgraph',
                            sources=['libcolgraph/libcc/libcolgraph.i'],
                            include_dirs = ['libcolgraph/libcc/*.h'],
                            swig_opts=['-c++'],
                            extra_compile_args=['-std=gnu++11'])

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(name='libcolgraph',
      cmdclass = {'build_py': build_py},
      ext_modules=[colgraph_module],
      # py_modules=['libcolgraph', 'libcolgraph.libcc',
      #             'libcolgraph.libcc.libcolgraph', 'libcolgraph.libpy'],
      package_data =
        {'libcolgraph.libcc._libcolgraph': ['libcolgraph/libcc/*.h',
                                            'libcolgraph/libcc/*.cpp']},
      packages = setuptools.find_packages(),
      version='0.0.1.post7',
      description='this library provides support to construct graphs and their '
                  'coloring graphs. a coloring graph is a metagraph '
                  'representing all the valid colorings of a graph. each '
                  'vertex of a coloring graph represents a coloring of the '
                  'base graph.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/aalok-sathe/coloring-graphs.git',
      author='Coloring Graphs lab, Univeristy of Richmond',
      author_email='aalok.sathe@richmond.edu',
      license='GPL-3',
      install_requires = ['tqdm>=4.32.1',
                          'networkx>=2.1',
                          'matplotlib>=2.2.2',
                          'typing>=3.6.6'],
      python_requires='>=3.4',
      classifiers=[
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 '
                                      'or later (GPLv3+)',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Python Modules'],)
