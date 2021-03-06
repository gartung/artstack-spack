from spack import *

class FhiclCpp(Package):
    homepage = "https://github.com/drbenmorgan/fnal-fhicl-cpp"
    url = "https://github.com/gartung/fnal-fhicl-cpp.git"
    version("e61f74d", git=url, commit="e61f74d")

    depends_on("cetbuildtools2")
    depends_on("cmake", type="build")
    depends_on("boost")
    depends_on("cetlib")
    depends_on("sqlite")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

