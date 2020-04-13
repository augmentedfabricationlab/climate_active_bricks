
# Climate Active Bricks


**This project examines the microclimate effects of differentiated robotically fabricated brick facades.** ...

![Brickwall Example 2](/docs/images/brickwall_ex2.jpg)


## Requirements

* Operating System: **Windows 10 Pro**
* [Rhinoceros 3D 6.0](https://www.rhino3d.com/)
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.x
* Git: [official command-line client](https://git-scm.com/) and visual GUI (e.g. [Github Desktop](https://desktop.github.com/))
* [VS Code](https://code.visualstudio.com/) with the following `Extensions`:
  * `Python` (official extension)


## Getting started

### Compas and Compas Fab Installation 
(via your Anaconda Terminal)
    
    (base)  conda config --add channels conda-forge
    (base)  conda create -n your_env_name python=3.6 compas=0.11.4 compas_fab=0.10.1 --yes
    (base)  conda activate your_env_name
    (your_env_name) python -m compas_rhino.install -v 6.0 -p compas compas_ghpython compas_rhino compas_fab roslibpy
    (your_env_name) python -m compas_fab.rhino.install -v 6.0
    
### Verify Installation

    (your_env_name) python
    >>> import compas_fab
    >>> compas_fab.__version__
    '0.10.1'
    >>> exit()


## Installation and Dependencies - Geometry and Fabrication

### Installation climate_active_bricks:

* Clone the [climate_active_bricks](https://github.com/augmentedfabricationlab/climate_active_bricks) repository into your project workspace.
* Use pip install to copy the repository to your Anaconda environment site packages: 

`(your_env_name) pip install your_filepath_to_climate_active_bricks`        

* Make the project accessible from Rhino by adding the `src` folder of the repositories (e.g., C:\Users\yourname\workspace\projects\climate_active_bricks\src) to the Rhino Pyhon path (via >> EditPythonScript >> Tools >> Options >> Add to search path).

### Installation ur_online_control:

* Install Ironpython 2.7.9. via following this [link](https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.9)
* Clone the current version of the [ur_online_control repository](https://github.com/augmentedfabricationlab/ur_online_control) 
into your project workspace.
* Make the project accessible from Rhino by adding the following two directories to the Rhino Pyhon path (via >> EditPythonScript >> Tools >> Options >> Add to search path):
    1. Ironpython Path, e.g., C:\Program Files\IronPython 2.7\Lib
    2. Parent folder of ur_online_control repository, e.g., C:\Users\yourname\workspace\projects

### Dependecies:

* shapely: `(your_env_name) conda install shapely`


## Installation and Dependencies - Climate Analysis and Optimization


## Example files

You find the various example files in the `rhino` folder.


Credits
-------------

[@augmentedfabricationlab](https://github.com/augmentedfabricationlab)
