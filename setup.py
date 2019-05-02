import glob
import os
import numpy
import subprocess

from distutils.core import setup
from Cython.Build import cythonize

packages = []
for root, dirs, files in os.walk('.'):
    if '__init__.py' in files:
        packages.append(root)

python_files = []
for package in packages:
    for module in os.listdir(package):
        if (module.endswith('.py')):
            python_files.append(package + '/' + module)
python_files.remove('./setup.py')

# print("Files to cythonize:")
# print(python_files)

a = setup(
        ext_modules = cythonize(python_files,
            include_path = [numpy.get_include()],
            annotate=True,
            exclude_failures=True)
)

# subprocess.run(['cython', '--embed', 'main.py'])

# libs = []
# for x in python_files:
#     lib = './qiskit/' + x.replace('.py', '.cpython-36m-x86_64-linux-gnu.so')
    # subprocess.run(['cp', lib, '/u/gc14/VariationalQuantumEigensolver/ext_libs'])
    # print(lib)

# lib_dirs.append('.')
# lib_dirs = list(set(lib_dirs))
# lib_dirs = list(filter(None, lib_dirs))

# print('Libraries to link:')
# print(these_libs)
# print('Directories to search:')
# print(lib_dirs)

# compile_main = ['gcc', '-I/usr/include/python3.5m', 'main.c', '-o', 'main',
#                 '-lpython3.5m']

# for x in lib_dirs:
#     compile_main.append('-L' + x)
# for x in these_libs:
#     compile_main.append('-l:' + x)

# print(' '.join(compile_main))
# subprocess.run(compile_main)
