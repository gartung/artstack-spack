from spack import *

class Canvas(Package):
    homepage = "https://github.com/drbenmorgan/fnal-canvas"
    url = "https://github.com/gartung/fnal-canvas.git"
    version("dc1c810", git=url, commit="dc1c810")


    depends_on("cetlib")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("root")
    depends_on("clhep~cxx11+cxx14")
    depends_on("cppunit")
    depends_on("tbb")
    depends_on("boost")
    depends_on("cetbuildtools2",type='build')
    depends_on("cmake",type='build')

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
