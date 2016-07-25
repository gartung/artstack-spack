from spack import *

class Cetbuildtools2(Package):
    homepage = "https://github.com/drbenmorgan/cetbuildtools2"

    version("dev", git="https://github.com/gartung/cetbuildtools2.git",branch="master")

    depends_on("cmake@3.3:",type="build")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["../"]
            cmake(*cmake_args)
            make()
            make("install")

