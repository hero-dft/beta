# Hessian Engineering for Atomistic Relaxation Optimization (***"HERO"***)

***HERO***   
is a toolkit to accelerate DFT structural optimization by tuning the Hessian information in the Broyden–Fletcher–Goldfarb–Shanno (BFGS) method.   

This toolkit can accelerate DFT-based structural optimization by reducing the number of force calls, and meanwhile, it maintains a DFT-level accuracy. 

This is a ***Beta Version*** developed mainly based on Atomistic Simulation Library (ASE). **Vienna Ab initio Simulation Package (VASP)** is the recommended calculator for this toolkit. 

===========================================================================

**Developed by:**  
*Li Lab at the Advanced Institute for Materials Reserarch (WPI-AIMR), Tohoku University, Japan*  
*Yang Lab at North China Electric Power University (NCEPU), China*  

**Main contributors:**  
*Mr. Mingzhe Li, NCEPU* (3rd undergraduate student; jointly supervised by Profs. Hao Li and Weijie Yang)    
*Prof. Hao Zheng, WPI-AIMR*  
*Prof. Weijie Yang, NCEPU*  
*Prof. Hao Li, WPI-AIMR*  

===========================================================================

**Requirements:**  

atomistic simulation environment (ase)==3.22.1  
cycler==0.11.0  
kiwisolver==1.3.1  
matplotlib==3.3.4  
numpy==1.19.5  
pandas==1.1.5  
Pillow==8.4.0  
pyparsing==3.0.9  
python-dateutil==2.8.2  
scipy==1.5.4  
six==1.16.0  
tornado==6.1  

===========================================================================

**Three Key Parameters**  

**(1) value (range: ≥0):**. 
Defines the force certeria (unit: eV/Å) that initializes the "Hessian engineering".

**(2) percent (range: 0-1):**  
Defines the percentage of atoms to be tuned in the Hessian matrix in the "Hessian engineering".  

**(3) value (range: ≥0):**  
"Hessian engineering" step: defines the the values set to the Hessian matrix for the selected atoms.

===========================================================================

***Important notes:***  
Before you use it for publication, **please ask for the permission** from **Prof. Hao Li (Email: li.hao.b8@tohoku.ac.jp)**

**The Website of the Hao Li Group (Digital Catalysis Lab, DigCat):**  
https://www.li-lab-cat-design.com/


![image](https://github.com/hero-dft/beta/blob/main/HERO_logo.png)
  
