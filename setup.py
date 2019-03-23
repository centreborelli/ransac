import os
import subprocess
from codecs import open
from setuptools import setup
from setuptools.command import develop, build_py


here = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(here, 'README.md'), 'r', 'utf-8') as f:
        return f.read()


class CustomDevelop(develop.develop, object):
    """
    Class needed for "pip install -e ."
    """
    def run(self):
        subprocess.check_call("make lib", shell=True)
        super(CustomDevelop, self).run()


class CustomBuildPy(build_py.build_py, object):
    """
    Class needed for "pip install ransac"
    """
    def run(self):
        super(CustomBuildPy, self).run()
        subprocess.check_call("make lib", shell=True)
        subprocess.check_call("cp -r lib build/lib/", shell=True)



requirements = ['numpy']


setup(name="ransac",
      version="1.0a5",
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
