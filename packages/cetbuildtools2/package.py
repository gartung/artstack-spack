from spack import *

class Cetbuildtools2(Package):
    homepage = "https://github.com/gartung/cetbuildtools2"
    url = "https://github.com/gartung/cetbuildtools2/archive/0.1.tar.gz"

    version("0.1", "52b4f84b9fb3dc2ac8dee960c6adbca8")
    version("0.2", "40b9f8ab9cc51ac08e81fecacbca9954")
    version("0.3", "5acab9ad40edf4eb494db3dda4385f89")

    def install(self, spec, prefix):
        with working_dir('build', create=True):
            cmake_args = std_cmake_args
            cmake_args += ["../"]
            cmake(*cmake_args)
            make()
            make("install")

