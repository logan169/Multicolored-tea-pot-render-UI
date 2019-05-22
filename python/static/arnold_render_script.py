# -*- coding: utf-8 -*-
# This file should stay in static folder



import os
import argparse
import maya.cmds as cmds

from mtoa.cmds.arnoldRender import arnoldRender
from arnold import AiBegin, AiMsgInfo, AiMsgSetConsoleFlags, AI_LOG_INFO, AiEnd

import maya.standalone
maya.standalone.initialize("Python")



def open_teapot_file(maya_scene_file):
    """
        Import teapot model scene in Maya

        Parameters
        ----------
            maya_scene_file (string):

        Returns
        -------
            Exception: Raise an exception if maya_scene_file is unimportable
            True (Boolean): Always return True if completed

    """
    try:
        # open original maya scene
        opened_file = cmds.file(
            maya_scene_file,
            i=True,
            namespace="root"
        )
    except:
        raise Exception(
            "Error: No able to import {} in Maya".format(maya_scene_file)
        )

    return True


# update tea pot color
def update_obj_color(r, g, b):
    """
        Update tea pot object color

        Parameters
        ----------
            r (integer): Red channel (0-255)
            g (integer): Green channel (0-255)
            b (integer): Blue channel (0-255)

        Returns
        -------
            Exception: Raise an exception if material is not foundable
            True (Boolean): Always return True if completed

    """
    try:
        # get lambert
        material = cmds.ls(type="lambert")[0]
    except:
        raise Exception(
            "Error: No able to found any material in the current scene".format(
                node_name)
        )

    # format color
    r, g, b = map(lambda x: float(x)/255, [r, g, b])

    # set new color
    cmds.setAttr(material + ".color", r, g, b)

    return True


def focus_cam_object(node_name, cam_name="persp"):
    """
        Focus on an object with specified camera

        Parameters
        ----------
            node_name (string): Maya node name
            cam_name (string): Maya camera name

        Returns
        -------
            Exception: Raise an exception if node_name is not foundable
            True (Boolean): Always return True if completed

    """
    try:
        cmds.select(node_name)
    except:
        raise Exception(
            "Error: No able to found {} in the current scene".format(
                node_name)
        )

    # center perspective camera on it
    cmds.viewFit("persp", node_name)

    return True


def arnold_render_picture():
    """
        Render tea pot to png file and create a log file.

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

    """

    AiBegin()

    AiMsgSetConsoleFlags(AI_LOG_INFO)

    AiMsgInfo('Starting Rendering ')

    # set output file format & prefix
    cmds.setAttr("defaultArnoldDriver.ai_translator", "png", type="string")
    cmds.setAttr("defaultArnoldDriver.pre", "teapot", type="string")

    # set output log filename path
    cmds.setAttr("defaultArnoldRenderOptions.log_filename",
                 os.path.join(
                     os.path.dirname(__file__),
                     "logs/arnold.log"
                 ),
                 type="string")

    # render frame
    arnoldRender(400, 400, True, True, 'persp', ' -layer defaultRenderLayer')

    AiMsgInfo('Rendering complet ! ')

    AiEnd()
    return True


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Arnold colored teapot render')
    parser.add_argument('-r', '--red', help='red channel', required=True)
    parser.add_argument('-g', '--green', help='green channel', required=True)
    parser.add_argument('-b', '--blue', help='blue channel', required=True)
    args = vars(parser.parse_args())

    # files path
    curr_dir_path = os.path.dirname(".")
    maya_scene_file = os.path.join(curr_dir_path, "teapot.ma")

    # open model teapot file
    open_teapot_file(maya_scene_file)

    # update color
    update_obj_color(
        args["red"],
        args["green"],
        args["blue"])

    # focus to teapot
    teapot = cmds.ls(type="mesh")[0]
    cmds.viewFit("persp", teapot)

    # render picture
    arnold_render_picture()
