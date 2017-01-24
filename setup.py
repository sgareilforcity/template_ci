# -*- coding: utf-8 -*-
"""setup.py."""

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

with open("README.rst") as readme_f:
    README = readme_f.read()

setup(name="template Testing",
      version="0.0.1",
      description="Template - testing",
      long_description=README,
      license='Proprietary License',
      author="ForCity Platform",
      author_email="support@forcity.io",
      url="https://github.com/sgareilforcity/template_ci",
      packages=["module_to_test"],
      install_requires=[
          "invoke",
          "hypothesis",
          "tox",
          "yapf",
      ],
      tests_require=[
      ],
      extras_require={
      },
      cmdclass={'test': Tox},
      classifiers=[
          "Development Status :: 1 - Planning",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: Other/Proprietary License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python 2",
          "Programming Language :: Python :: Implementation :: CPython",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Scientific/Engineering",
      ],
      zip_safe=False, )
