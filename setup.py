from setuptools import setup, find_packages

with open(file="README.md", mode="r") as f:
    description = f.read()

setup(
    name='tirsvadCLI-quiz_engine_4_trivia',
    version='0.0.1-alpha001',
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/TirsvadCLI",
    download_url = 'https://github.com/TirsvadCLI/Python.QuizEngine4Trivia/archive/v_01.tar.gz',
    author="Jens Tirsvad Nielsen",
    author_email="jenstirsvad@gmail.com",

    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires='>=3.10, <4',
    install_requires=[
        'requests==2.31.0',
    ],
    # extras_require = {
    #     'test': [
    #         'coverage',
    #         'pytest',
    #         'pytest-cov',
    #         'coveralls',
    #         'PyYAML',
    #     ],
    # },


)

# twine upload --repository pypitest dist/*   --config-file C:\Users\Tirsvad\.pypirc
#  twine upload -r testpypi dist/*
#
# [pypi]
# repository = https://upload.pypi.org/
# username: tirsvad
# password: pypi-AgEIcHlwaS5vcmcCJGY5MDM2NjU3LWE4M2YtNDk0MS1iMzU2LWNlMDQzOTc5ZjFjYQACKlszLCIzYTY4ZGJhNS1lMWI4LTRlZjMtYjY5Yi01NzMyZmQ5NjcxNDciXQAABiA1wHzl36fexhto4z96v7Ds2DVJCOC4t8_BAX9GhsuJUg
# keyring set https://upload.pypi.org/legacy/ tirsvad
#
# [pypitest]
# repository = https://test.pypi.org/legacy/
# username = tirsvad
# password = pypi-AgENdGVzdC5weXBpLm9yZwIkZTBmMTQ4ZDctZjM2ZS00OTY4LWE4NTAtYjRkMWE1M2Q2M2U5AAIqWzMsIjUxNjBkOGMzLTZmMzktNDFiMS1iMzhhLTFjZWM0Nzc1OTE5MCJdAAAGIJMRIbWXAH-00hGbi55RCFynN17_xbFrtEE7oBM9yeuu
# keyring set https://test.pypi.org/legacy/ tirsvad