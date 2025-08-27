from pathlib import Path
from setuptools import setup

HERE = Path(__file__).parent
readme = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setup(
    name="xarray_parcel",
    version="1.0.0",  # <- bump as you like or wire to tags
    description="Parcel utilities (e.g. CAPE/CIN) that play nicely with xarray",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Original authors & EWN fork",
    url="https://github.com/srowe-ewn/xarray_parcel",
    license="UNKNOWN",  # <- set to the repo’s actual licence (e.g. MIT/BSD-3)
    python_requires=">=3.8",
    # We map the existing 'modules/' directory to an installable package named 'xarray_parcel'
    packages=["xarray_parcel"],
    package_dir={"xarray_parcel": "modules"},
    include_package_data=True,
    # Optional: expose a top-level shim so `import parcel_functions` still works
    py_modules=["parcel_functions"],
    install_requires=[
        "numpy>=1.20",
        "xarray>=0.20",
        "scipy>=1.6",
        "numba>=0.61.2",
        "metpy>=1.5",
        "pint>=0.20",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "License :: OSI Approved :: MIT License",  # <- adjust to match actual licence or remove
    ],
)
