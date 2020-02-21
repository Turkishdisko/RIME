import argparse
import sys
from ctypes import *
from ctypes.util import find_library
import rime_main
import os


# this class will store data in a struct
class BinStruct(Structure):
    # does some black magic. Describe struct fields and their data types
    _fields_ = [('files', c_char_p),
                ('numFiles', c_int)]


# create parser object, which handles commandline arguments
def parse_args(sysArgs):
    parser = argparse.ArgumentParser(sysArgs)
    # options without -- are required and positional
    parser.add_argument("catalog", help="")
    parser.add_argument("rip", help="")
    parser.add_argument("output", help="")
    # options with -- are optional and can occur in any order. If a type isn't explicitly defined, they are assumed to be booleans that are set to true when enabled
    parser.add_argument("--ignore_warnings", "-i", action="store_true", help="Instead of stopping on warnings, ignore and continue")
    parser.add_argument("--netcdf4", "-n", action="store_true", help="Store output in NetCDF4 file format. Any combination of output format options can be specified simultaneously")
    parser.add_argument("--gui", "-gu", action="store_true", help="Launch RIME GUI")
    parser.add_argument("--hdf5", "-hd", action="store_true", help="Store output in HDF5 file format. Any combination of output format options can be specified simultaneously")
    parser.add_argument("--geotiff", "-g", action="store_true", help="Store output in GeoTIFF file format. Any combination of output format options can be specified simultaneously")
    parser.add_argument("--checksum", "-c", action="store_true", help="")
    parser.add_argument("--tar_netcdf4", "-tn", action="store_true", help="Automatically compress output NetCDF4 files. --netcdf4 must be enabled")
    parser.add_argument("--tar_hdf5", "-th", action="store_true", help="Automatically compress output HDF5 files. --hdf5 must be enabled")
    parser.add_argument("--tar_geotiff", "-tg", action="store_true", help="Automatically compress output GeoTIFF files. --geotiff must be enabled")
    parser.add_argument("--tar_all", "-ta", action="store_true", help="Automatically compress output for all specified output types")
    # example of specifying type and default value: parser.add_argument("--", type=float, default=1e-5, help="")

    return parser.parse_args()


def parse_params(filePath):
    paramDic = {}  # type: Dict[str, str]

    # use open convention that helps avoid weird issues if the program crashes with file open:
    with open(filePath) as paramFile:
        for line in paramFile:
            # skip comments starting with #. Otherwise, remove whitespace and split using '=' as delimiter
            if line[0] != '#':
                line = line.strip()
                # skip empty lines
                if line:
                    splitLine = line.split('=')
                    paramDic[splitLine[0].strip()] = splitLine[1].strip()

    return paramDic

# hey dummy, combine metadata and rip parse into a single method because they're super similar
def parse_metadata(filePath):
    metadataDic = {} # type: Dict[str, str]

    with open(filePath) as metadataFile:
        for line in metadataFile:
            # remove any extra whitespace
            line = line.strip()
            # skip comments and empty strings
            if line and line[0] != '#':
                splitLine = line.split(',')
                # now that we've split the line, make sure we get rid of trailing whitespace
                metadataDic[splitLine[0].strip()] = splitLine[1].strip()

    return metadataDic

if __name__ == "__main__":
    # get commandline args
    if sys.argv[1] == '--gui':
        rime_main.run()


    else:
        args = parse_args(sys.argv[1:])
        catalogPath = args.catalog
        ripPath = args.rip
        outputPath = args.output
        ignoreWarnings = args.ignore_warnings
        netcdf4 = args.netcdf4
        #gui = args.gui
        hdf5 = args.hdf5
        geotiff = args.geotiff
        checksum = args.checksum
        tarNet = args.tar_netcdf4
        tarHdf = args.tar_hdf5
        tarGeo = args.tar_geotiff
        tarAll = args.tar_all

        '''
        # load C .so library to get access to parseDir()
        parseLib = CDLL('../c/parserlib.so')
        # debug print statement.. delete me later!
        print(parseLib)
        # specify C types of input args and return value
        parseLib.parseDir.argtypes = [c_wchar_p]
        parseLib.parseDir.restypes = [c_void_p]

        # the C function returns a struct- throw it into a class with the same values and print to see if it's right
        p1 = BinStruct.from_address(parseLib.parseDir('.'))
        print(p1.files)
        '''

        testDic = parse_params(os.path.dirname(__file__) + "/test/test_rip.txt")
        for key in testDic.keys():
            print('%s : %s' % (key, testDic[key]))

        if netcdf4:
            None
            #Run conv

        if hdf5:
            None
            #run conv

        if geotiff:
            None
            #run conv

        if tarAll:
            None
        else:
            if tarNet:
                None
            if tarGeo:
                None
            if tarHdf:
                None

        if checksum:
            None
            #checksum stuff




