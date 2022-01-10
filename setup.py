import setuptools

# https://www.freecodecamp.org/news/build-your-first-python-package/

exec(open('botfinder/version.py').read())

setuptools.setup(
    name="social-networks-bot-finder",
    description="CLI tool to help detecting if a twitter account is a bot",
    version=__version__,
    author="Ambanum",
    url="https://github.com/ambanum/social-networks-bot-finder",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["botfinder"],
    setup_requires=["setuptools_scm"],
    use_scm_version=False,
    include_package_data=True,
    install_requires=[
        "click==8.0.3",
        "joblib==1.1.0",
        "pandas==1.3.5",
        "shap==0.40.0",
        "scikit-learn==0.24.2",
    ],
    dependency_links=[
        "git+https://github.com/JustAnotherArchivist/snscrape.git"
    ],
    python_requires="~=3.8",
    extras_require={
        "test": ["coverage"],
    },
    entry_points={
        "console_scripts": [
            "botfinder=botfinder.cli:main",
        ],
    },
)
