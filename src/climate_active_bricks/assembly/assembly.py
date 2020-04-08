from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ur_online_control.assembly import Assembly

from compas.geometry import Frame
from compas.geometry import Transformation
from compas.geometry import Rotation
from compas.geometry import Translation

import math


class BrickAssembly(Assembly):
    """A data structure for discrete element assemblies for human robot collaboration
    """

    def __init__(self,
                 elements=None,
                 attributes=None,
                 default_element_attribute=None,
                 default_connection_attributes=None):

        super(BrickAssembly, self).__init__()

        self.network.default_vertex_attributes.update({
            'A_is_open': True,
            'B_is_open': True
        })

