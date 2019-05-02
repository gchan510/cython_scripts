# Scripts to compile python to shared libraries and/or binaries

## Compile (possible nested) python packages to shared libraries
Run from top-level package:
  `python setup.py build_ext --inplace`

This will place the shared libraries with the same directory structure under
`package_name`

**NOTE:** When copying shared libs directory to another one (e.g. `ext_libs`), you must modify
`sys.path` to include `ext_libs` otherwise it won't find the modules
