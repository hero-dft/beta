# 置零，改变的是变量的本身，无返回值
import os
import shutil
from os import path

import sys
import ase.io

from ase.calculators.vasp import Vasp

from ZERO import BFGSZ,BFGSZH
from myacal import traceAtoms

vasp = Vasp(
    directory='vasp',  # output dir
    xc='pbe',  # the exchange-correlation functional

    # 下面是incar的内容
    lwave=False,
    prec='Accurate',  # MP is Accurate
    istart=0,
    isym=1,
    encut=300,
    sigma=0.1,
    algo='Fast',
    nelm=1000,
    # ediffg=-0.05,
    ediff=1e-5,
    npar=4,
    ibrion=-1,
    nsw=0,
    
)

models = ['MGH']
for model in models:
    pts = ase.io.read(model + '.vasp')
    pts = traceAtoms([i for i in pts], cell=pts.cell, pbc=True)
    pts.calc = vasp
    pts0 = pts.copy()
    if not path.exists(model):
        os.makedirs(model)
    dyn = BFGSZ(pts, trajectory='{0}.traj'.format(model), name=model)
    i = 1
    while not dyn.run(steps=i, fmax=0.05):
        i += 1


