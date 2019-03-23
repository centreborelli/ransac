import os
import subprocess
from codecs import open
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.build_py import build_py


here = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(here, 'README.md'), 'r', 'utf-8') as f:
        return f.read()


class CustomDevelop(develop):  # needed for "pip install -e ."
    def run(self):
        subprocess.check_call("make lib", shell=True)
        super().run()


class CustomBuildPy(build_py):  # needed for "pip install ransac"
    def run(self):
        super().run()
        subprocess.check_call("make lib", shell=True)
        subprocess.check_call("cp -r lib build/lib/", shell=True)


requirements = ['numpy']


setup(name="ransac",
      version="1.0a3",
      description="Python wrapper of Enric Meinhardt's RANSAC implementation",
      long_description=readme(),
      long_description_content_type="text/markdown",
      url="https://github.com/cmla/ransac",
      author="Carlo de Franchis",
      author_email="carlo.de-franchis@ens-cachan.fr",
      py_modules=["ransac"],
      install_requires=requirements,
      cmdclass={'develop': CustomDevelop,
                'build_py': CustomBuildPy})
