from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="signupgenius-export",
    version="1.0.2",
    description="Export SignUpGenius signup data to CSV",
    author="Robert Ruddy",
    packages=find_packages(),
    py_modules=["export_signup"],
    install_requires=requirements,
    license="GPL-3.0-only", 
    entry_points={
        "console_scripts": [
            "signupgenius-export=export_signup:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)