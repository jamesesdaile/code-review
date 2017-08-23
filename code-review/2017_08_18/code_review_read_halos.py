#read_halos.py
import numpy as np

Om_m = 0.2715
Mp = Om_m*2.775*10**11*(21000./8192.)**3

masses = np.array([])
#Loop through files and read in number of halos, then number of particles in halo
for i in range(4200):
	file_num = "%05d" % (i,)
	box_file = np.fromfile('halo_files/21000_8192_z0/fof_boxlen21000_n8192_lcdmw7_masst_'+str(file_num),'<i4')#<i4 for boxlen_21000, i>4 for boxlen_5184
	nhalo = box_file[1]
	halos = box_file[3:].reshape((nhalo,8))
	nparts = halos[:,3]
	M = nparts*Mp
	masses = np.append(masses,M)

#write out ascii formatted file of halo masses
file = open("mass_simulations_z0",'w')
for i in range(len(masses)):
	file.write("%E\n"%masses[i])
file.close()