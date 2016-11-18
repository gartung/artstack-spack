from spack import *

class Canvas(Package):
    homepage = "https://github.com/gartung/fnal-canvas.git"
    url = "https://github.com/gartung/fnal-canvas/archive/1.04.01.tar.gz"
    version("1.04.01", "70c0b91d02aa1edde33afeb7ec4d0a5a")


    depends_on("cetlib@1.20.00")
    depends_on("fhicl-cpp@4.01.00")
    depends_on("messagefacility@1.17.02")
    depends_on("root@6.06.04")
    depends_on("clhep@2.3.2.2+cxx14~cxx11")
    depends_on("cppunit")
    depends_on("tbb@20151115oss")
    depends_on("boost@1.60.0")
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
