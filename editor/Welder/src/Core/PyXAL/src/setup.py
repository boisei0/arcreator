from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

XAL_ext = Extension(
    "_PyXAL",  # name of extension
    ["_PyXAL.pyx"],  # our Cython source "PyXAL.pyx"
    language="c++",  # causes Cython to create C++ source
    include_dirs=[r".\include", r"C:\Python27\include", r"C:\Python27\PC", r'./include'],  # list of paths to search for header files
    library_dirs=[r".\bin", r".\lib", r"C:\Python27\libs", 'C:\Python27\PCbuild', r'./bin'],  # list of paths to search for libraries at link time
    libraries=["libhltypes",  "libxal"],                 # list of libraries to link to
    extra_compile_args=[],
    extra_link_args=[],
)


setup(
    name="_PyXAL",
    ext_modules=[XAL_ext],
    cmdclass={'build_ext': build_ext},
)