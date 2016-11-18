from spack import *

class Messagefacility(Package):
    homepage = "https://github.com/gartung/fnal-messagefacility.git"
    url = "https://github.com/gartung/fnal-messagefacility/archive/1.17.02.tar.gz"
    version("1.17.02", "b045733b12445c758dedfed240182af3")

    depends_on("cmake", type="build")
    depends_on("cetbuildtools2", type="build")
    depends_on("boost@1.60.0")
    depends_on("cetlib@1.20.00")
    depends_on("fhicl-cpp@4.01.00")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "-DBUILD_TESTING=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

