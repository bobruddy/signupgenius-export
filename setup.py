from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="signupgenius-export",
    version="1.0.4",
    description="Export SignUpGenius signup data to CSV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bobruddy/signupgenius-export",
    author="Robert Ruddy",
    packages=find_packages(),
    py_modules=["export_signup"],
    install_requires=["requests"],
    license="GPL-3.0-only", 
    project_urls={
        "Homepage": "https://github.com/bobruddy/signupgenius-export",
        "Issues": "https://github.com/bobruddy/signupgenius-export/issues",
        "Repository": "https://github.com/bobruddy/signupgenius-export",
    },
    keywords=["signupgenius", "export", "csv", "api", "volunteer", "signup"],
    entry_points={
        "console_scripts": [
            "signupgenius-export=export_signup:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
