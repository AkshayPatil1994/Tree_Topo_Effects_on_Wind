#!/usr/bin/env python
# coding: utf-8

from imageio.core.request import URI_FILENAME
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from scipy.interpolate import griddata
import pyvista as pv


# # COMFORT MISMATCH PLOTS
# 

print('VELOCITY DIFFERENCE') 
print(' ')

U10 = 4.97 #velocity inflow 10 m height [m/s]
kappa =0.41
z0 = 0.2 # roughness length [m]
ustar = U10*kappa/(np.log((10+z0)/z0))
Uph = ustar/kappa*np.log((1.75+z0)/z0)  

#broadleaf_im_summer conifer_im
# sampled results from postProcessing > surfaces  U_z15Normal / U_z10Normal / U_pedestrianH /U_z1Normal
surface_U1 = pv.read('./LoD2/broadleaf_im_summer/postProcessing/surfaces/752/U_pedestrianH.vtk') ###---------need to be changed---------##
surface_U2 = pv.read('./LoD2/broadleaf_ex/postProcessing/surfaces/752/U_pedestrianH.vtk')
# interpolation between the meshes for U:
U1_mesh1 = pv.PolyData(surface_U1)
U2_mesh2 = pv.PolyData(surface_U2)
# U1_mesh2 = U2_mesh2.sample(U1_mesh1)
U1_mesh2 = U2_mesh2.interpolate(U1_mesh1, sharpness=2, radius=1.0, strategy='closest_point', null_value=0,pass_cell_arrays=False, pass_point_data=False)


# Clip any dataset by a set of XYZ bounds using the pyvista.DataSetFilters.clip_box() filter.
# clip part of domain (to only zoom in at study area for the results)
# terrain + buildings outline coordinates (copied from snappyHexMeshDict):# = H = H_terrain + H_maxbuilding
## bounding box broadleaf LoD3 (21.53 1.55 0) (41.81 28.88 21.86)  ###---------need to be changed---------##

x_min = 21
y_min = 1
z_min = 0
x_max = 42
y_max = 29
z_max = 22  

## bounding box conifer LoD3 (60.48 51.17 0) (80.64 67.59 19.6)  ###---------need to be changed---------##
# x_min = 60
# y_min = 50
# z_min = 0
# x_max = 81
# y_max = 68
# z_max = 20

# bounds of clipping box specified as [xMin,xMax, yMin,yMax, zMin,zMax] of the 2 outer vertices:
 ###---------need to be changed---------##
# bounds2 = [x_min-30,x_max+30, y_min-30,y_max+170, 10.95, 10.95]
# bounds2 = [x_min-30,x_max+30, y_min-30,y_max+170, 10, 10]
bounds2 = [x_min-30,x_max+30, y_min-30,y_max+170, 1.75, 1.75] 


clippedU1 = U1_mesh2.clip_box(bounds2, invert=False)  # note: invert clip if you want to remove the box and keep everything around it 
clippedU2 = U2_mesh2.clip_box(bounds2, invert=False)

# take the norm of the velocity vector (magnitude):
clippedU1['magnitude'] = np.linalg.norm(clippedU1['U'], axis=1)
clippedU2['magnitude'] = np.linalg.norm(clippedU2['U'], axis=1)

# compute the difference
U_effect = ((clippedU2.point_arrays['magnitude'] - clippedU1.point_arrays['magnitude'])/Uph)*100
data_final_U = clippedU2
data_final_U.point_arrays['magnitude'] = U_effect 
deltaU_scalars = data_final_U.point_arrays['magnitude']

sargs = dict(
    color='k',
    font_family='courier',
    title_font_size=20,
    label_font_size=18,
    n_labels=7,
    fmt="%.1f",
    height=0.05, 
    width=0.6, 
    vertical=False, 
    position_x=0.2, 
    position_y=0.065,
    title='Relative Velocity Magnitude difference [%]',
    # n_colors=21
    )

# _______________________________________________________________________________

# plotter set-up (create 2 subplots): bad pedestrian vs. good thermal comfort 
plotter = pv.Plotter(shape=(1, 1), window_size=[800, 1200], border=False)
plotter.set_background("w")
pv.set_plot_theme("document")

# -------------
print(deltaU_scalars.min())
print(deltaU_scalars.max())

boring_cmap = plt.cm.get_cmap("RdYlBu_r", 21)
plotter.add_mesh(data_final_U, scalars=deltaU_scalars, clim=[-50,50],below_color='blue', above_color='red', scalar_bar_args=sargs, cmap=boring_cmap) #cmap="plasma_r"
plotter.show_bounds(xlabel='x [m]', ylabel='y [m]', color='black')
#plotter.add_text('VELOCITY LoD1', font='courier', font_size=9, position='upper_edge')
plotter.view_xy()   # plot the xy-plane
plotter.enable_zoom_style()   # enable to zoom in the image

# show and save the created subplots:  ###---------need to be changed---------##
plotter.show(screenshot='./screenshot/broad_LoD2_ex-im_trunk.png')
