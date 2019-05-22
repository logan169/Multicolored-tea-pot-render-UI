# -*- coding: utf-8 -*-

from base_renderer_plugin import BaseRendererPlugin
import os
import subprocess

class ArnoldRendererPlugin(BaseRendererPlugin):

    def __init__(self, model=None):
        super(ArnoldRendererPlugin, self).__init__(model)

    def render_asset(self, hex_color):
        """
        Render the asset to a file

        Parameters
        ----------
            hex_color (string): Hexadecimal color value

        Returns
        -------
            file_path (string): File path of the rendered picture

        """

        # Format hexadecimal to RGB
        color_string = hex_color.lstrip("#")
        r, g, b = tuple(str(int(color_string[i:i+2], 16)) for i in (0, 2, 4))

        print "Rendering asset with {}".format((r, g, b))

        cmd_lines = [
            self.model._MAYAPY_PATH,
            os.path.join(
                self.model._STATIC_FOLDER_PATH,
                "arnold_render_script.py"
            ),
            "-r {}".format(r),
            "-g {}".format(g),
            "-b {}".format(b)
        ]

        print " ".join(cmd_lines)

        rendering_process = subprocess.Popen(cmd_lines)
        rendering_process.communicate()

        return True

    def get_picturepath(self):
        """
        Return rendered picture path

        Parameters
        ----------

        Returns
        -------
            file_path (string): 
                Rendered picture file path or None if there is no file

        """
        picture_filepath = self.find_file_by_ext(
            self.model._STATIC_FOLDER_PATH,
            'teapot'
        )

        if not picture_filepath:
            return None

        return picture_filepath

    def get_output_log(self):
        """
        Return rendered process output log

        Parameters
        ----------

        Returns
        -------
            output_log (list): Output log messages by line

        """
        log_file = self.find_file_by_ext(
            self.model._STATIC_FOLDER_PATH,
            '.log'
        )

        if not log_file:
            return ''

        with open(log_file, "rb") as f:
            return f.readlines()

    def find_file_by_ext(self, folder_path, ext):
        """
        Return filepath list of all files
        matching a given extension

        Parameters
        ----------
            folder_path (string): Folder path to scan
            ext (string): Extension format

        Returns
        -------
            filepaths_list (list/boolean): Files list that matched or False

        """

        for root, dirs, filenames in os.walk(folder_path):
            for filename in filenames:
                if ext in filename:
                    return os.path.join(root, filename)

        return False


def get_plugin():
    return ArnoldRendererPlugin
