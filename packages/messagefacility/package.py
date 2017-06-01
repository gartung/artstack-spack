from spack import *

class Messagefacility(Package):
    homepage = "https://github.com/drbenmorgan/fnal-messagefacility"
    url = "https://github.com/gartung/fnal-messagefacility.git"
    version("e61f74d",git=url ,commit="e61f74d")

    depends_on("cmake", type="build")
    depends_on("cetbuildtools2", type="build")
    depends_on("boost")
    depends_on("cetlib")
    depends_on("fhicl-cpp")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "-DBUILD_TESTING=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

