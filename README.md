# artstack-spack
Spack repository for FNAL's Art stack, which comprises:

- cetbuildtools/cetbuildtools2
- cetlib
- fhicl-cpp
- TODO: messagefacility
- TODO: art

At present, forks of these packages are used which provide near full compatibility
across Linux/GCC and Mac/Clang. This means that only dev versions are used, so no
version tracking is present. This is because the fork follows the master branch
of upstream and also that the version dependency structure isn't fully derived
yet.

Using this Repository in Spack
==============================
Get [spack](https://github.com/llnk/spack) and the repository set up like:

```console
$ cd /somewhere
$ git clone https://github.com/LLNL/spack.git
$ git clone https://github.com/HEP-SF/hep-spack.git
$ cd spack
$ ./bin/spack compilers
$ ./bin/spack repo add $(pwd)/hep-spack
```

Setup the basic spack environment:

```console
$ . share/spack/setup-env.sh
```

Try building something:

```console
... On OSX with native clang ...
$ spack install fhicl-cpp %clang
... or, on Linux with gcc
$ spack install fhicl-cpp
```

Note that the packages don't yet fully specify compiler requirements,
though the builds will fail if the Clang/GCC in use do not support
the requisite features.

