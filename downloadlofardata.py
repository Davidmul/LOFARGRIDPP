####Grid-pp LOFAR downloader####
####D.D.Mulcahy 20.02.2017#####
####To download data, already staged,
####at the LOFAR archive and save it to the grid


import os
import glob


######input file

list_name = sys.argv[1]
original_list = open(list_name)
lines = len(original_list.readlines())
original_list.close()
original_list = open(list_name)


for i in range(lines):
    temp = original_list.readline()[:-1]
    outfile = open('html_temp.txt','w')
    outfile.write(str(temp))
    outfile.close()
    os.system('wget -ci html_temp.txt')
    tarname = glob.glob('*.tar')[0]
    outname = tarname.split("%")[-1]
    os.rename(tarname, outname)
    os.system('rm -rf html_temp.txt')
    os.system('dirac-dms-add-file /skatelescope.eu/user/m/david.mulcahy/tmp/'+str(outname)+' '+str(outname)+' UKI-NORTHGRID-MAN-HEP-disk')
    os.system('rm -rf html_temp.txt')

original_list.close()
