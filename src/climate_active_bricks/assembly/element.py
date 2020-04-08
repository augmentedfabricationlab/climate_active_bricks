from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


from ur_online_control.assembly import Element

import json

from compas.geometry import Frame
from compas.geometry import Transformation
from compas.geometry import Rotation
from compas.geometry import Translation
from compas.geometry import Point
from compas.geometry import Box
from compas.datastructures import Mesh
from compas.datastructures import mesh_transform


__all__ = ['Element']


class BrickElement(Element):
    """Data structure representing a discrete element of an assembly.

    Attributes
    ----------
    frame : :class:`compas.geometry.Frame`
        The frame of the element.

    Examples
    --------
    >>> from compas.datastructures import Mesh
    >>> from compas.geometry import Box
    >>> element = Element.from_box(Box(Frame.worldXY(), ))

    """

    def __init__(self, frame):
        super(BrickElement, self).__init__(frame)

    
    @classmethod
    def from_dimensions(cls, length=240, width=115, height=50, typology="full", gripping_frame=None):
        """Construct an element with a box primitive with the given dimensions.

        Parameters
        ----------
        length : float
            length of the brick.
        width : float
            width of the brick.
        height : float
            height of the brick.
        typology : "string"
            type of the brick, "full" or "half"
        gripping_frame : :class:`Frame`
            frame for robot gripping.

        Returns
        -------
        :class:`Element`
            New instance of element.
        """
        if not gripping_frame:
            gripping_frame = Frame([0, 0, height], [1, 0, 0], [0, -1, 0]) #frame for robot gripping
        
        box_frame = Frame([-length/2., -width/2., 0.], [1, 0, 0], [0, 1, 0]) #center of the box frame
        box = Box(box_frame, length, width, height)
        
        element = cls(gripping_frame) # element initialisation
        element.id = typology
        element._source = box

        return element

    def copy(self):
        """Returns a copy of this element.

        Returns
        -------
        Element
        """
        elem = BrickElement(self.frame.copy())
        if self._gripping_frame:
            elem.gripping_frame = self.gripping_frame.copy()
        if self._source:
            elem._source = self._source.copy()
        if self.id:
            elem.id = self.id
        return elem

    def get_pose_quaternion(self):
        """ formats the element's frame to a pose quaternion and returns the pose"""
        return list(self.frame.point) + list(self.frame.quaternion)


