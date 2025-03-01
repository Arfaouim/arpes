from arpes.io import load_without_dataset
from arpes.plotting.qt_ktool import ktool

from pathlib import Path

data_path = (Path(__file__).parent.parent / 'tests' / 'resources'
             / 'datasets' / 'basic' / 'data' / 'main_chamber_cut_0.fits')

data = load_without_dataset(str(data_path.absolute()), location='ALG-MC')

ktool(data)
