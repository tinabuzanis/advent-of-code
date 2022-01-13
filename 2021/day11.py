import numpy as np
from scipy import ndimage as ndi
from scipy import signal
file = open('_inp.txt')
a = np.array([[int(c) for c in line.strip()] for line in file])

fc = 0
cmat = np.ones((3,3))
cmat[1,1] = 0
for step in range(1000):
    a = a + 1
    f = a > 9
    cont = True
    while(cont):
        nf = signal.convolve(f, cmat, mode='same').round(0).astype(int)
        _a = a + nf
        _f = _a > 9
        cont = (_f & ~f).sum().sum() > 0
        f = _f
    a = _a
    a[f] = 0
    #fc += _f.sum().sum()
    if f.all().all():
        print(step + 1)





def run_part_1(energy):
    flash_count = 0
    n_steps = 100
    convolve_matrix = np.ones((3, 3))
    convolve_matrix[1, 1] = 0
    for step in range(n_steps):
        energy = energy + 1
        flashes = energy > 9
        need_to_continue = True
        while need_to_continue:
            neighbour_flashes = signal.convolve(flashes, convolve_matrix, mode='same').round(0).astype(int)
            new_energy = energy + neighbour_flashes
            new_flashes = new_energy > 9
            need_to_continue = (new_flashes & ~flashes).sum().sum() > 0
            flashes = new_flashes
        energy = new_energy
        energy[flashes] = 0
        flash_count += new_flashes.sum().sum()
    return flash_count = np.where(a!=5,0
