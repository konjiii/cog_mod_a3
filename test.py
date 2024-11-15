import ccm
from ccm.lib.actr import *

log = ccm.log(html=True)

class Hanoi(ACTR):
    actions = ["AB", "AC", "BC", "BA", "CA", "CB"]
    goal = Buffer()
    imaginal = Buffer()

    def move(self, x, y):
        if y == "_":
            y = x[-1]
        else:
            y += x[-1]

        x = x[:-1]

        if x == "":
            x = "_"

        return x, y

    def choose(goal="action:choose", imaginal="A:?a B:?b C:?c"):
        if C[0] == "_":
            if A[-1] == "3":
                goal.modify(action="AB")
            elif B[-1] == "3":
                goal.modify(action="AB")

    def ab(goal="action:?act action:AB", imaginal="A:?a B:?b C:?c"):
        a, b = self.move(a, b)
        imaginal.modify(A=a, B=b)
        goal.modify(action="choose")

    def ac(goal="action:?act action:AC", imaginal="A:?a B:?b C:?c"):
        a, c = self.move(a, c)
        imaginal.modify(A=a, C=c)
        goal.modify(action="choose")

    def bc(goal="action:?act action:BC", imaginal="A:?a B:?b C:?c"):
        b, c = self.move(b, c)
        imaginal.modify(B=b, C=c)
        goal.modify(action="choose")

    def ba(goal="action:?act action:BA", imaginal="A:?a B:?b C:?c"):
        b, a = self.move(b, a)
        imaginal.modify(B=b, A=a)
        goal.modify(action="choose")

    def ca(goal="action:?act action:CA", imaginal="A:?a B:?b C:?c"):
        c, a = self.move(c, a)
        imaginal.modify(C=c, A=a)
        goal.modify(action="choose")

    def cb(goal="action:?act action:CB", imaginal="A:?a B:?b C:?c"):
        c, b = self.move(c, b)
        imaginal.modify(C=c, B=b)
        goal.modify(action="choose")

    def final(imaginal="C:123"):
        print "done"
        imaginal.clear()
        goal.clear()

model = Hanoi()
ccm.log_everything(model)
model.imaginal.set("A:321 B:_ C:_")
model.goal.set("action:AC")
model.run()
