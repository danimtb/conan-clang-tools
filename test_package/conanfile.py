from conans import ConanFile, tools


class clang_conan_toolsConanTestFile(ConanFile):

    def build(self):
        from common import extract_from_url
        extract_from_url("https://github.com/conan-io/conan/archive/1.3.3.zip")

    def test(self):
        from common import extract_from_url
        extract_from_url("https://github.com/conan-io/conan/archive/1.3.3.zip")
