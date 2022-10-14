import setuptools

# read the contents of your README file
with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()
exec(open('st_vizzu/version.py').read())
setuptools.setup(
    name="st_vizzu",
    version=__version__,
    author="Avratanu Biswas",
    author_email="avrab.yt@gmail.com",
    description="ipyvizzu wrapper for intuitive usage with Streamlt embed support.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/avrabyt/Streamlit-ipyvizzu",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=["streamlit >= 0.63", "ipyvizzu","pandas"],
)