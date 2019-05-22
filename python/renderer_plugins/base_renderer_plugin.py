# -*- coding: utf-8 -*-

import abc
ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})


class BaseRendererPlugin(ABC):
    """
    This class is the renderer base plugin
    all renderer plugins class inherit from it

    App will only communicate with renderer
    throughy this class abstractmethod
    We just need to create those methods
    to add new renderer plugins

    """

    def __init__(self, model):

        self.model = model

    @abc.abstractmethod
    def render_asset(self, color_string):
        """
        Render the asset to a file

        Parameters
        ----------
            color_string (string): Hexadecimal color value

        Returns
        -------
            file_path (string): File path of the rendered picture

        """
        pass

    @abc.abstractmethod
    def get_output_log(self):
        """
        Return rendered process output log

        Parameters
        ----------

        Returns
        -------
            output_log (string): Output log messages

        """
        pass
    
    @abc.abstractmethod
    def get_picturepath(self):
        """
        Return rendered picture path

        Parameters
        ----------

        Returns
        -------
            file_path (string): Rendered picture file path

        """
        pass
