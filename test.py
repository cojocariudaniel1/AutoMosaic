from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGraphicsRectItem, QMenu
from PySide6.QtGui import QBrush, QPen, QPainter
from PySide6.QtCore import Qt, QPointF


class ActionNode(QGraphicsRectItem):
    def __init__(self, name, position):
        super().__init__(-30, -30, 60, 60)  # Adjust size as needed
        self.setPos(position)
        self.setBrush(QBrush(Qt.lightGray))
        self.setPen(QPen(Qt.black))
        self.name = name
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    def contextMenuEvent(self, event):
        menu = QMenu()
        edit_action = menu.addAction("Edit Action")
        delete_action = menu.addAction("Delete Action")
        action = menu.exec(event.screenPos())

        if action == edit_action:
            self.edit_action()
        elif action == delete_action:
            self.scene().removeItem(self)

    def edit_action(self):
        # Open dialog for editing action parameters
        print(f"Editing {self.name}")


class DiagramView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.Antialiasing)

        # Add example nodes
        self.add_action_node("Action 1", QPointF(50, 50))
        self.add_action_node("Action 2", QPointF(200, 200))

    def add_action_node(self, name, position):
        node = ActionNode(name, position)
        self.scene().addItem(node)


app = QApplication([])
view = DiagramView()
view.setWindowTitle("Flow Diagram")
view.resize(800, 600)
view.show()
app.exec()
