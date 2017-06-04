from setuptools import setup, find_packages
setup(
    name = "myscript",
    version = "0.1",
    packages = ['src'],
    entry_points = {
        'console_scripts' : ['myscript=src.mymodule:main']
    },
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires = ['docutils>=0.3'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Matias",
    author_email = "matiasanoniz@gmail.com",
    description = "This is an Example Package",
    license = "PSF",
    keywords = "hello world example examples",
    url = "http://www.d-image.com.ar/",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.

    # para crear un paquete debian por consola:
    # python3 setup.py --command-packages=stdeb.command bdist_deb
)
