from spack import *

class FhiclCpp(Package):
    homepage = "https://github.com/drbenmorgan/fnal-fhicl-cpp.git"
    url = "https://github.com/gartung/fnal-fhicl-cpp/archive/4.01.00.tar.gz"
    version("4.01.00", "be3704efbf0bfc150f3e6bdd286186e6")

    depends_on("cetbuildtools2")
    depends_on("cmake")
    depends_on("boost@1.60.0")
    depends_on("cetlib@1.20.00")
    depends_on("sqlite@3.7.15:")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

