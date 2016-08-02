from spack import *

class Cetbuildtools2(Package):
    homepage = "https://github.com/gartung/cetbuildtools2"
    url = "https://github.com/gartung/cetbuildtools2/archive/0.1.tar.gz"

    version("0.1", )

    depends_on("cmake@3.3:",type="build")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["../"]
            cmake(*cmake_args)
            make()
            make("install")

