"""
Created on Tue Apr  2 21:32:28 2024

@author: craig
"""
"""
Importing packages and data 
"""

import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.feature as cfeature
"""
Building Bathymetry map
"""

bath_ds = xr.open_dataset("GMRTv4_2_20240403topo(1).grd", engine = 'netcdf4')
bath_da = bath_ds['altitude']


fig, axis = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, label = 'Bathymetry')

bath_da.plot.contourf(ax=axis, transform=ccrs.PlateCarree(), levels = 20,  cmap=mpl.cm.RdBu_r, robust = True)
axis.coastlines() 
axis.set_title('Bathymetry')
gl=axis.gridlines(draw_labels=True)
gl.right_labels=False 
gl.top_labels=False
fig.savefig('Figures\Bathymetry.png')

""" 
Building Chlorophyl map
"""


chl_ds = xr.open_dataset("ESACCI-OC-MAPPED-CLIMATOLOGY-1M_MONTHLY_4km_PML_CHL-fv5.0.nc")
chl_dss = chl_ds.sel(lat = slice(16.87141, 14.47989) ,lon = slice(51.58135986 , 54.46032715))

chl_da = chl_dss['chlor_a']
da_mean = chl_da.mean(dim='time')

fig, axis1 = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, label = 'Chlorophyll')

da_mean.plot(ax=axis1, transform=ccrs.PlateCarree(),  cmap='turbo', robust=True,
             cbar_kwargs= {'label':'Chlorophyll-a concentrations [milligram m-3]'})
axis1.set_title('Mean Annual Chlorophyll')
axis1.add_feature(cfeature.LAND)
gl=axis1.gridlines(draw_labels=True)
gl.right_labels=False 
gl.top_labels=False
fig.savefig('Figures\Annual_CHL.png')


"""
Building faceted maps

"""

da_months = chl_da.groupby('time.month').mean(dim='time')
da_months2 = da_months.reindex(month=[9,10,11,12,1,2,3,4,5,6,7,8])
da_months2.plot(col = 'month', col_wrap=4, cmap = 'turbo', robust=True
               ,label = 'Monthly variation mean Chlorophyll-a concentrations [milligram m-3]',
               cbar_kwargs= {'label':'Mean Chlorophyll-a concentrations [milligram m-3]'})


""" 
Time series data
"""

region = da_months.mean(dim=['lat', 'lon'])
point = da_months.sel(lat=15,lon=52, method='nearest')

fig,axis3 = plt.subplots()
region.plot(ax = axis3,marker='o', c = 'r', label = 'Region average', x = None)
point.plot(ax = axis3,marker='o', c = 'b', label = 'lat = 15, lon = 52', x = None)
plt.grid()
axis3.legend()
axis3.set_title('Seasonal Chlorophyll-a concentrations')
axis3.set_ylabel('Chlorophyll-a concentrations [milligram m-3]')
fig.savefig('Figures\PointvsRegion_CHL.png')
