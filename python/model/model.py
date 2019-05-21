# -*- coding: utf-8 -*-

import os


class RenderModel(object):

    def __init__(self, config):
        super(RenderModel, self).__init__()

        # config parameters
        self._DEFAULT_PICTURE_PATH = config.DEFAULT_PICTURE_PATH
        self._STATIC_FOLDER_PATH = config.STATIC_FOLDER_PATH
        self._RENDER_PLUGINS_PATH = config.RENDER_PLUGINS_PATH
        self._RENDER_PLUGIN_NAME = config.RENDER_PLUGIN_NAME
        self._MAYAPY_PATH = config.MAYAPY_PATH

        self.output_logs = ''
        self._rendered_image_path = None
        self.color_picked = "#FFFFFF"

    @property
    def rendered_image_path(self):
        """
        Evaluate if there is a rendered image file
        if so return its path, else return default picture path

        Parameters
        ----------

        Returns
        -------
            rendered_image_path (string): Rendered picture's path

        """

        if self._rendered_image_path and \
                os.path.isfile(self._rendered_image_path):
            return self._rendered_image_path
        return self._DEFAULT_PICTURE_PATH

    @rendered_image_path.setter
    def rendered_image_path(self, value):
        """
        Update rendered_image_path with the newest image path

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """
        self._rendered_image_path = value
        return True

