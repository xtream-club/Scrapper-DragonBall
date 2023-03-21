from setuptools import setup, find_packages

try:
    with open("./README.md", "r", encoding="utf8") as readme_file:
        long_description = readme_file.read()
except FileNotFoundError:
    long_description = "Descripción del proyecto no encontrada"

setup(
    name='Dragon-Ball-API',
    version='0.1',
    description='Api unoficial de dragon ball inspirado de la fandom de dragon ball',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eduardo Lopez',
    author_email='nanguelulpz@gmail.com',
    url='https://github.com/xtream-club/Dragon-Ball-API',
    download_url='https://github.com/xtream-club/Dragon-Ball-API/tarball/0.1',
    keywords=['Dragon-Ball-Api', 'Dragon Ball', 'Api Dragon Ball'],
    classifiers=[],
    license='MIT',
    packages=find_packages(),
    include_package_data=True
)
