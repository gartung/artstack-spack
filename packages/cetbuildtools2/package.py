from spack import *

class Cetbuildtools2(Package):
    homepage = "https://github.com/drbenmorgan/cetbuildtools2"
    url = "https://github.com/gartung/cetbuildtools2.git"

    version("416bd82", git=url, commit="416bd82")

    depends_on('cmake@3.5:', type='build')

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["../"]
            cmake(*cmake_args)
            make()
            make("install")

