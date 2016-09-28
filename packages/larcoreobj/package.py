from spack import *

class Larcoreobj(Package):
    homepage = "https://github.com/gartung/fnal-larcoreobj.git"

    version("dev", git="https://github.com/gartung/fnal-larcoreobj.git",branch="alt-cmake")

    depends_on("canvas")
    depends_on("cetlib")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("root@6.06.02")
    depends_on("clhep+cxx14~cxx11")
    depends_on("cetbuildtools2",type="build")
    depends_on("boost@1.60.0")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["../"]
            cmake_args += ["-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF"]
            cmake_args += ["-DALT_CMAKE=1"]
            cmake_args += ["-DCMAKE_CXX_FLAGS=-std=c++14"]
            cmake_args += ["-DROOT_VERSION=6"]
            cmake_args += ["-DHAVE_ROOT6=1"]
            cmake(*cmake_args)
            make("VERBOSE=1")
            make("install")

