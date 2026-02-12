import os

# Solution Issue CLIP: https://github.com/openai/CLIP/issues/528
# import pkg_resources
from packaging.requirements import Requirement # new
from setuptools import setup, find_packages

setup(
    name="clip",
    py_modules=["clip"],
    version="1.0",
    description="",
    author="OpenAI",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        # str(r)
        # for r in pkg_resources.parse_requirements(
        #     open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        # )
        str(Requirement(line)) # new
        for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read().splitlines() # new
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
