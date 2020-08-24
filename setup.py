from setuptools import setup  # type: ignore[import]

setup(
    name="name",
    version="0.5.6",
    packages=["name"],
    package_data={
        "name": ["__init__.py", "py.typed"],
    },

    zip_safe=False,
    author="Alan Cristhian",
    author_email="alan.cristh@gmail.com",
    description="A library with a base class that "
                "stores the assigned name of an object.",
    license="MIT",
    keywords="data structure",
    url="https://github.com/AlanCristhian/name",
)
