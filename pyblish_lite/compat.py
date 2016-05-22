import os
import sys


def load_pyqt5():
    import PyQt5.Qt
    sys.modules["Qt"] = PyQt5
    PyQt5.QtCore.Signal = PyQt5.QtCore.pyqtSignal
    PyQt5.QtCore.Slot = PyQt5.QtCore.pyqtSlot
    PyQt5.QtCore.Property = PyQt5.QtCore.pyqtProperty

    # Preserve reference to binding for conditional logic
    PyQt5.__binding__ = "PyQt5"

    print("Loaded PyQt5")


def load_pyqt4():
    import PyQt4.Qt
    sys.modules["Qt"] = PyQt4
    PyQt4.QtWidgets = PyQt4.QtGui
    PyQt4.QtCore.Signal = PyQt4.QtCore.pyqtSignal
    PyQt4.QtCore.Slot = PyQt4.QtCore.pyqtSlot
    PyQt4.QtCore.Property = PyQt4.QtCore.pyqtProperty
    PyQt4.__binding__ = "PyQt4"

    print("Loaded PyQt4")


def load_pyside2():
    import PySide2
    sys.modules["Qt"] = PySide2
    PySide2.__binding__ = "PySide2"
    print("Loaded PySide2")


def load_pyside():
    import PySide
    from PySide import QtGui
    PySide.QtWidgets = QtGui
    PySide.QtCore.QSortFilterProxyModel = PySide.QtGui.QSortFilterProxyModel
    sys.modules["Qt"] = PySide
    PySide.__binding__ = "PySide"
    print("Loaded PySide")


def init():
    if os.name == "nt":
        windows_taskbar_compat()

    # Support Qt 4 and 5, PyQt and PySide
    try:
        load_pyside2()
    except ImportError:
        try:
            load_pyqt5()
        except ImportError:
            try:
                load_pyside()
            except ImportError:
                try:
                    load_pyqt4()
                except:
                    sys.stderr.write("pyblish-lite: Could not find "
                                     "appropriate bindings for Qt\n")


def windows_taskbar_compat():
    """Enable icon and taskbar grouping for Windows 7+"""

    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        u"pyblish_lite")
