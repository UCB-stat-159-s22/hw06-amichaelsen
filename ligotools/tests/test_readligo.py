from ligotools.readligo import loaddata, read_frame
from ligotools.readligo import FileList

def test_FileList_searchdir_data():
	fl = FileList()
	hdf5_files = fl.searchdir('data/')
	assert len(hdf5_files) == 3

def test_FileList_searchdir_figures():
	fl = FileList()
	hdf5_files = fl.searchdir('figures/')
	assert len(hdf5_files) == 0
	
def test_FileList_searchdir_audio():
	fl = FileList()
	hdf5_files = fl.searchdir('figures/')
	assert len(hdf5_files) == 0
	
def test_loaddata_L_L1_LOSC_4_V2():
	fn_L1 = 'data/L-L1_LOSC_4_V2-1126259446-32.hdf5'
	strain, time, chan_dict = loaddata(fn_L1, 'H1')
	assert len(strain) == len(time)

