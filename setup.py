from setuptools import setup, find_packages

##Read requirements.txt, ignore comments
try:
    REQUIRES = list()
    f = open("requirements.txt", "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[: line.find("#")].strip()
        if line:
            REQUIRES.append(line)
except:
    print("'requirements.txt' not found!")
    REQUIRES = list()



# with open("README.md") as f:
#     readme = f.read()

# setup(
#     name="pgportfolio",
#     version="1.0.0",
#     description="",
#     long_description=readme,
#     author="Zhengyao Jiang, Dixing Xu, Jinjun Liang",
#     author_email="",
#     packages=find_packages(exclude=("tests", "docs"),
#                            include=("matplotlib", "tensorflow", "tflearn", "pandas",
#                                     "pandas", "cvxopt", "scipy")))


"""

"""



setup(
    name="rlportfolio",
    version="0.1",
    # include_package_data=True,
    author="bibo feng",
    author_email="bibofeng@gmail.com",
    description="package from https://github.com/liangzp/Reinforcement-learning-in-portfolio-management-.git",
    url="https://github.com/bibofeng/Reinforcement-learning-in-portfolio-management-.git",
    license="unlicense",
    package_dir={"": "src"},  # package directory,
    packages=find_packages(where="src"),
    package_data={'': ['../main.py']}, ## include non py files
    include_package_data=True,
    install_requires=REQUIRES
    + ["pyfolio @ git+https://github.com/bibofeng/pyfolio.git"],
    # install_requires=REQUIRES
    zip_safe=False,
)                                    