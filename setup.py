import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME="Kidney_Disease_Classification_DL"
AUTHOR_NAME="dipdregan"
SRC_REPO="CNN_Classifier"
AUTHOR_Email="dipendrapratap155@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_Email,
    description="this is sensor fault prediction project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    
    project_urls={
                  
    "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",  
                  
                 },
    package_dir={"":"CNN_Classifier"},
    packages=setuptools.find_packages(where="CNN_Classifier"),
)


