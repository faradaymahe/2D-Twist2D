"""Twist2D Demo."""
#%%
# +------------+
# | Usage Demo |
# +------------+
from twist2d import *

# Create an object for t2d
twist_demo = Twist2D()

# Read in the primitive cell information of each layer(in different POSCARs)
#  - filename: the target POSCAR's path or filename(in current directory).
#  - repeat_time: the layer's repeat times, default is 2. 
twist_demo.read_primcell_of_layers('./POSCAR', 2)
# twist_demo.read_primcell_of_layers('POSCAR-BN', 1)

# Initialize the different twisted layers
#  - mult_a1p,  mult_a2p: supercell vector a1',a2' based on a1,a2
#  - layer_dis: the layer distance of this layer to next layer, default 2A.
#  - scs_x, scs_y: supercell shift in x,y direction in angstroms, default 0A.
m = 6
n = 7
#--> 1st layer
mult_a1p = [m, n]
mult_a2p = [-n, m+n]
twist_demo.init_twisted_layers(mult_a1p, mult_a2p, layer_dis=3)
#--> 2nd layer
mult_a1p = [n, m]
mult_a2p = [-m, n+m]
twist_demo.init_twisted_layers(mult_a1p, mult_a2p)
# #--> 3rd layer
# mult_a1p = [n, m]
# mult_a2p = [-m, n+m]
# twist_demo.writein_supercell_vector(mult_a1p, mult_a2p)

# Fill the cell with the layers
twist_demo.fill_twisted_layers_cell(start_z=0.1)

# (Optional) Calculate the twisted angles of each layer in degree 
twisted_angles = twist_demo.calc_layers_twist_angles()
print(twisted_angles)

# Write results to the file
twist_demo.write_res_to_poscar()
# PROGRAM END

#%%
# +-------------------+
# | Special condition |
# +-------------------+
from twist2d import *

### If you are twisting a bilayer graphene like system, 
###     you can write more simply like this:
# Twist bilayer graphene like structures
tbg_demo = TwistBGL()
tbg_demo.gen_TBG(6, 7)
# (Optional) Calculate the twisted angles of each layer in degree 
twisted_angles = tbg_demo.calc_layers_twist_angles()
print(twisted_angles)
#tbg_demo.gen_TBG(m=6, n=7, poscar_init='POSCAR', poscar_out="POSCAR.T2D.vasp", start_z=0.1, a3p_z=20.0, layer_dis=2.0, scs_x=0.0, scs_y=0.0)

#PROGRAM END

# %%