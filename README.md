# artstack-spack
Spack repository for FNAL's Art stack, which comprises:

- cetbuildtools/cetbuildtools2
  - [cetbuildtools2](https://github.com/drbenmorgan/cetbuildtools2.git) is
    a stripping down version of the upstream [cetbuildtools](https://cdcvs.fnal.gov/redmine/projects/cetbuildtools)
    package. It provides an identical compiler environment, but strips out
    hard coded dependencies on FNAL's UPS configuration management system,
    dependencies installed through UPS, and consequent install hierarchy.
  - Spack's packaging provides much the same functionality as UPS in terms
    of telling a build where to locate dependencies, but unlike cetbuildtools/UPS
    cetbuildtools2 has zero coupling to the package/config management system.
- [cetlib](https://github.com/drbenmorgan/fnal-cetlib/tree/feature/modern-cmake)
- [fhicl-cpp](https://github.com/drbenmorgan/fnal-fhicl-cpp/tree/feature/modern-cmake)
- [messagefacility](https://github.com/drbenmorgan/fnal-messagefacility/tree/feature/modern-cmake)
- TODO: [art](https://cdcvs.fnal.gov/redmine/projects/art)

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

