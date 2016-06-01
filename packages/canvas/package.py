from spack import *

class Canvas(Package):
    homepage = "https://github.com/gartung/fnal-canvas.git"

    version("dev", git="https://github.com/gartung/fnal-canvas.git",branch="feature/modern-cmake")

    depends_on("cetlib")
    depends_on("fhicl-cpp")
    depends_on("messagefacility")
    depends_on("root")
    depends_on("tbb@4.4.3")
    depends_on("cmake@3.3:")
    depends_on("cetbuildtools2")
    depends_on("boost@1.60:")
    depends_on("doxygen@1.8:")

    def install(self, spec, prefix):

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        options=[source_directory]
        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug')
        else:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Release')

        options.extend(std_cmake_args)

        with working_dir(build_directory, create=True):
            options.append("-DCET_COMPILER_WARNINGS_ARE_ERRORS=OFF")
            cmake(*options)
            make()
            make("install")
