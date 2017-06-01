from spack import *

class CetlibExcept(Package):
    homepage = "https://github.com/drbenmorgan/fnal-cetlib_except"
    url = "https://github.com/gartung/fnal-cetlib_except.git"

    version("8f48b7e",git=url, commit="8f48b7e")

    depends_on("cetbuildtools2",type="build")
    depends_on("cmake",type="build")
    depends_on("boost")
    depends_on("sqlite")
    depends_on("openssl")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

