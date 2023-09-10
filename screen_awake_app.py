import keyboard
import time
import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QStyle
from PyQt5.QtCore import QTimer


def keep_awake():
    while True:
        keyboard.press_and_release("up")
        time.sleep(590)  # 9 min 50 secs
        # time.sleep(10) test period of time


def main():
    app = QApplication(sys.argv)

    # Create the icon and set its properties
    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(app.style().standardIcon(QStyle.SP_ComputerIcon))
    tray_icon.setVisible(True)
    tray_icon.showMessage(
        "Screen app",
        "The screen will be awake while program is running",
        QSystemTrayIcon.Information,
        3000,
    )

    # Creat the menu
    tray_menu = QMenu()

    # Create exit option and add it to the menu
    exit_action = QAction("Exit", tray_menu)
    exit_action.triggered.connect(app.quit)
    tray_menu.addAction(exit_action)

    tray_icon.setContextMenu(tray_menu)

    # Show the icon
    tray_icon.show()

    # Timer that execute the keep_awake method in certain period of time
    timer = QTimer()
    timer.timeout.connect(keep_awake)
    timer.start(590_000)  # 9 minutes and 50 seconds
    # timer.start(10_000) # 10 seconds test period of time

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()