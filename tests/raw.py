import netCDF4
import numpy as np
from netCDF4 import ma
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def main(db_pth=".", fmodel="clm"):
    # fetch_mask
    g = netCDF4.Dataset(db_pth + "/land_water_mask/LandWaterMask_Global_CRUNCEP.nc", "r")
    mask = g.variables["land_water_mask"]
    mask = mask[:].swapaxes(0, 1)

    # load_data
    f = netCDF4.Dataset(db_pth + "/NEE_first_year.nc", "r")
    data = f.variables["NEE"]
    data = data[:]
    data = data.swapaxes(0, 2)
    adj = 60 * 60 * 24 * (365 / 12) * 1000
    data = data * adj

    # standardize_with_mask
    native = data.mean(2)
    latShape = mask.shape[0]
    logShape = mask.shape[1]
    for x in range(latShape):
        for y in range(logShape):
            if mask[x, y] == 1 and ma.getmask(native[x, y]) == 1:
                for index in range(data.shape[2]):
                    data[x, y, index] = 0

    # simple_diagnose
    plt.imshow(np.mean(data, 2))
    plt.xlabel("Mean 1982-2010 NEE [gC/m2/mon]")
    plt.title(fmodel + ":BG1")
    pp = PdfPages("result_NEE.pdf")
    pp.savefig()
    pp.close()
