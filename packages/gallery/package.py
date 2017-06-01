from spack import *

class Gallery(Package):
    homepage = "https://github.com/gartung/fnal-gallery"
    url = "https://github.com/gartung/fnal-gallery.git"
    version("8fa014a",git=url, commit="8fa014a")

    depends_on("canvas")
    depends_on("cetlib")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("larcoreobj")
    depends_on("lardataobj")
    depends_on("larsimobj")
    depends_on("nusimdata")
    depends_on("root")
    depends_on("clhep~cxx11+cxx14")
    depends_on("cetbuildtools2",type="build")
    depends_on("cmake",type="build")
    depends_on("boost")

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

