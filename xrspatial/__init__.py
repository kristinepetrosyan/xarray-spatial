from xrspatial.slope import slope  # noqa
from xrspatial.aspect import aspect  # noqa
from xrspatial.terrain import generate_terrain  # noqa
from xrspatial.bump import bump  # noqa
from xrspatial.focal import mean  # noqa
from xrspatial.hillshade import hillshade  # noqa
from xrspatial.perlin import perlin  # noqa
from xrspatial.proximity import proximity  # noqa
from xrspatial.proximity import great_circle_distance  # noqa
from xrspatial.proximity import euclidean_distance  # noqa
from xrspatial.proximity import manhattan_distance  # noqa
from xrspatial.viewshed import viewshed  # noqa
from xrspatial.ndvi import ndvi  # noqa
from xrspatial.zonal import stats as zonal_stats  # noqa
from xrspatial.zonal import apply as zonal_apply  # noqa
from xrspatial.zonal import crosstab as zonal_crosstab  # noqa
from xrspatial.curvature import curvature  # noqa


__version__ = '0.0.1'


def test():
    """Run the xarray-spatial test suite."""
    import os
    try:
        import pytest
    except ImportError:
        import sys
        sys.stderr.write("You need to install py.test to run tests.\n\n")
        raise
    pytest.main([os.path.dirname(__file__)])
