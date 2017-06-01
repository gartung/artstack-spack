from spack import *

class Cetlib(Package):
    homepage = "https://github.com/drbenmorgan/fnal-cetlib"
    url = "https://github.com/gartung/fnal-cetlib.git"

    version("8f918f7", git=url, commit="8f918f7")

    depends_on("cetbuildtools2",type="build")
    depends_on("cmake",type="build")
    depends_on("boost")
    depends_on("sqlite")
    depends_on("openssl")
    depends_on("cetlib-except")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

