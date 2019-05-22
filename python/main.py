#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
from model.model import RenderModel
from ui.view import RenderView

import sys
import pydoc
from PySide2 import QtWidgets


class RenderApp(object):

    def __init__(self, parent=None):
        super(RenderApp, self).__init__()
        self.model = RenderModel(config)
        self.view = RenderView(parent, self.model)

        # load and init renderer_plugins
        plugin = self.load_plugin(
            self.model._RENDER_PLUGIN_NAME)
        self.renderer_plugin = plugin(self.model)

        self.init_signals()

    def load_plugin(self, module_path):
        """
        Import modules dynamically

        Parameters
        ----------
            module_path (string): Module path

        Returns
        -------
            module_class (object): Module class object

        """

        module = pydoc.locate(module_path)
        module_class = module.get_plugin()
        return module_class

    def update_picked_color(self, value):
        """
        Update model's picked color value

        Parameters
        ----------
            value (string): Hexadecimal color string

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        self.model.color_picked = value
        return True

    def init_signals(self):
        """
        Connect UI signals to controller's logic

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        # picked color has changed
        self.view.signals.picked_color_has_changed.connect(
            self.update_picked_color
        )

        # render button clicked
        self.view.signals.render_button_has_been_clicked.connect(
            self.render_asset
        )
        return True

    def render_asset(self):
        """
        Update UI, call renderer plugin's render_asset method
        and update model with new rendered data

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        # deactivate render button
        # during rendering process
        self.view.disable_render_button()

        # render new picture asset and get output log
        c = self.model.color_picked
        self.renderer_plugin.render_asset(c)

        # fetch picture and log file
        self.model.rendered_image_path = self.renderer_plugin.get_picturepath()
        self.model.output_logs = self.renderer_plugin.get_output_log()

        # update view with renderer informations
        self.view.update_view()

        # deactivate render button
        # during rendering process
        self.view.enable_render_button()
        return True

    def run(self):
        """
        Execute application

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        global app
        self.view.show()
        # Run the qt application
        app.exec_()
        return True


app = QtWidgets.QApplication(sys.argv)


def main():

    render_app = RenderApp()
    render_app.run()


if __name__ == "__main__":
    main()
