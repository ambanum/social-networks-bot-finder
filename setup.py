import setuptools

# https://www.freecodecamp.org/news/build-your-first-python-package/

VERSION = "0.0.1"
DESCRIPTION = "CLI tool to help detecting if a twitter account is a bot"

with open('requirements.txt') as f:
    required = f.read().splitlines()
    
setuptools.setup(
    name="social-networks-bot-finder",
    description=DESCRIPTION,
    version=VERSION,
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
    use_scm_version=True,
    install_requires=required,
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
