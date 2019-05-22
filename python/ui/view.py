# -*- coding: utf-8 -*-

from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui

import os
import sys

# UI signals class


class CustomSignal(QtCore.QObject):
    render_button_has_been_clicked = QtCore.Signal()
    picked_color_has_changed = QtCore.Signal(str)


class RenderView(QtWidgets.QWidget):
    """
    Render View class containing all UI widgets 

    """

    def __init__(self, parent=None, model=None):
        super(RenderView, self).__init__()

        self.setGeometry(800, 400, 800, 800)
        self.setWindowTitle("Render UI")

        self.model = model
        self.build_layout()
        self.signals = CustomSignal()
        self.init_signals()

        self.update_view()

    def update_view(self):
        """
        Update picture & log output widgets with new rendered datas

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """
        
        # update asset picture widget
        with open(self.model.rendered_image_path) as f:
            data = f.read()

        image = QtGui.QImage()
        image.loadFromData(data)

        pixmap = QtGui.QPixmap(
            image.scaled(400, 400, QtCore.Qt.KeepAspectRatio))
        self.asset_picture.setPixmap(pixmap)

        # update log output widget
        self.output_log.clear()

        for line in self.model.output_logs:
            self.output_log.appendPlainText(line.rstrip('\n'))

        return True

    def init_signals(self):
        """
        Connect UI widgets signals

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """
        
        # color picker button
        self.color_picker_button.clicked.connect(
            self.open_color_dialog
        )

        # color picker
        self.color_picker.colorSelected.connect(
            self.emit_picked_color_has_changed
        )

        # render button
        self.render_button.clicked.connect(
            self.emit_render_button_signal
        )
        return True

    def emit_render_button_signal(self):
        """
        Emit render_button_has_been_clicked signal

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        self.signals.render_button_has_been_clicked.emit()
        return True

    def emit_picked_color_has_changed(self, picked_color):
        """
        Emit picked_color_has_changed signal

        Parameters
        ----------
            picked_color (string): Hexadecimal color string

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        self.signals.picked_color_has_changed.emit(picked_color)
        return True

    def open_color_dialog(self):
        """
        Open color dialog modal and update picked color value

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        picked_color = str(self.color_picker.getColor().name())
        self.emit_picked_color_has_changed(picked_color)
        return True

    def disable_render_button(self):
        """
        Disable render button to ensure that we only
        have one rendering process running.

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        self.render_button.setEnabled(False)
        self.render_button.setText("Rendering...")
        return True

    def enable_render_button(self):
        """
        Enable render button once rendering is done.

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        self.render_button.setEnabled(True)
        self.render_button.setText("Render")
        return True

    def build_layout(self):
        """
        Build view UI layout

        Parameters
        ----------

        Returns
        -------
            True (Boolean): Always return True if completed

        """

        self.layout = QtWidgets.QVBoxLayout()

        # Asset picture and log box
        self.main_box = QtWidgets.QVBoxLayout()
        self.buttons_box = QtWidgets.QHBoxLayout()
        self.buttons_box.addStretch(1)

        # Asset picture
        self.asset_picture = QtWidgets.QLabel(self)
        self.asset_picture.setAlignment(QtCore.Qt.AlignHCenter)
        self.asset_picture.setMaximumHeight(800)
        self.main_box.addWidget(self.asset_picture)

        # output log display
        self.output_log = QtWidgets.QPlainTextEdit(self)
        # self.output_log.setReadOnly(True)
        self.main_box.addWidget(self.output_log)

        # color picker
        self.color_picker_button = QtWidgets.QPushButton('Change Color', self)
        self.color_picker = QtWidgets.QColorDialog(self)
        self.buttons_box.addWidget(self.color_picker_button)

        # render button
        self.render_button = QtWidgets.QPushButton('Render', self)
        self.buttons_box.addWidget(self.render_button)

        # add to layout
        self.layout.addLayout(self.main_box)
        self.layout.addLayout(self.buttons_box)

        # set Layout
        self.setLayout(self.layout)
        return True
