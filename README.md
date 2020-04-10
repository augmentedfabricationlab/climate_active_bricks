
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


### Compas and Compas Fab Installation (via Anaconda Terminal)
    
    (base)  conda config --add channels conda-forge
    (base)  conda create -n your_env_name python=3.6 compas=0.11.4 compas_fab=0.10.1 --yes
    (base)  conda activate your_env_name
    (your_env_name) python -m compas_rhino.install -v 6.0 -p compas compas_ghpython compas_rhino compas_assembly compas_fab roslibpy
    (your_env_name) python -m compas_fab.rhino.install -v 6.0
    
### Verify Installation

    (your_env_name) python
    >>> import compas_fab
    >>> compas_fab.__version__
    '0.10.1'
    >>> exit()


## Installation and Dependencies

### Installation:

* Clone the `[climate_active_bricks](https://github.com/augmentedfabricationlab/climate_active_bricks)` repository.
* Use pip install to copy the repository to your Anaconda environment site pacakges:

        (your_env_name) pip install your_filepath_to_climate_active_bricks

* Then install dependencies and make the project accessible from Rhino by adding the src folder of the repositories to the Rhino Pyhon path.

### Dependecies:

* `[ur_online_control](https://github.com/augmentedfabricationlab/ur_online_control)` 


Credits
-------------

[@augmentedfabricationlab](https://github.com/augmentedfabricationlab)
