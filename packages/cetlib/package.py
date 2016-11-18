from spack import *

class Cetlib(Package):
    homepage = "https://github.com/drbenmorgan/fnal-cetlib.git"
    url = "https://github.com/gartung/fnal-cetlib/archive/1.20.00.tar.gz"

    version("1.20.00", "5b5dae01c77fb242a91a77acd5d079f4")

    depends_on("cetbuildtools2",type="build")
    depends_on("cmake",type="build")
    depends_on("boost@1.60.0")
    depends_on("sqlite@3.12.2")
    depends_on("openssl")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["-DALT_CMAKE=1", "-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF", "../"]
            cmake(*cmake_args)
            make()
            make("install")

