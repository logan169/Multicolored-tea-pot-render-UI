# -*- coding: utf-8 -*-

import os

#### config ####

# Static folder
STATIC_FOLDER_PATH = os.path.abspath('static')

# default picture path
DEFAULT_PICTURE_PATH = os.path.join(
    STATIC_FOLDER_PATH,
    "images",
    "default.png"
)

# Renderer plugins module informations
RENDER_PLUGINS_PATH = ("renderer_plugins")
RENDER_PLUGIN_NAME = '.'.join(
    [
        RENDER_PLUGINS_PATH,
        "arnold_renderer_plugin"
    ]
)

# Mayapy path
MAYAPY_PATH = "/usr/autodesk/maya2017/bin/mayapy"
