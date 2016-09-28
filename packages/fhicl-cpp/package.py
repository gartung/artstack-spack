from spack import *

class FhiclCpp(Package):
    homepage = "https://github.com/drbenmorgan/fnal-fhicl-cpp.git"

    version("dev", git="https://github.com/gartung/fnal-fhicl-cpp.git", branch="feature/modern-cmake")

    depends_on("cmake@3.5",type="build")
    depends_on("cetbuildtools2", type="build")
    depends_on("boost@1.60.0")
#    depends_on("doxygen@1.8:")
    depends_on("cetlib@dev:")
    depends_on("sqlite@3.7.15:")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

