from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[Extension("meme",["memewrapper.pyx","llr.c","likelihood.c"])]

setup(name = "MEME app",cmdclass = {"build_ext": build_ext},ext_modules = ext_modules)
