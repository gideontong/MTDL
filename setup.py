"""
MembershipTookit.com Downloader v1.0.0
======================================
Software (C) Copyright 2019 Gideon Tong
All rights reserved.

This piece of software is available to use as "free as in beer", but is 
not for redistribution, resell, remixing, reusing, or any other type
of use other than for personal use only. You can download it from the
official GitHub repository on gideontong's profile.

Its use is to download directories of information from directories hosted
on MembershipTookit.com and convert all the pages into a CSV so it
can be parsed in Excel or another program for automation.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "membership-toolkit-downloader",
    version = "1.0.0",
    author = "Gideon Tong",
    author_email = "gideon@gideontong.com",
    description = "A tool that converts MembershipToolkit.com directories to a parsable CSV.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/gideontong/MembershipToolkitDownloader",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)