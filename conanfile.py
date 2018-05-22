import os
from conans import ConanFile

class clang_conan_toolsConanFile(ConanFile):
    name = "clang_conan_tools"
    version = "0.1"
    description = "Common recipe scripts for clang_conan_tools module"
    url = "https://gitlab.com/Manu343726/clang-conan-packages"
    license = "MIT"
    exports = "conan_clang_tools/*.py"
    build_policy = "missing"
    generators = "virtualenv"

    def package(self):
        self.copy("*.py")

    def package_info(self):
        self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, "conan_clang_tools"))
