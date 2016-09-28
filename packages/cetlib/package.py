from spack import *

class Cetlib(Package):
    homepage = "https://github.com/drbenmorgan/fnal-cetlib.git"

    version("dev", git="https://github.com/gartung/fnal-cetlib.git", branch="alt-cmake")

    depends_on("cetbuildtools2",type="build")
    depends_on("boost@1.60.0")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

