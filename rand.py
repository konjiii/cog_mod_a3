import ccm
from ccm.lib.actr import *

log = ccm.log(html=True)


class Hanoi(ACTR):
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
    
    def repr_peg(self, peg, disks):
        out = peg + " has disks ["
        if '_' == disks[0]:
            return out + ']'
        for disk in disks:
            if disk != disks[0]:
                out += ", "
            out += disk
        return out + ']'
    
    def repr_pegs(self, a, b, c):
        print("Peg " + self.repr_peg('A', a) + ", peg " + self.repr_peg('B', b) + ", peg " + self.repr_peg('C', c) + ".\n")

    def ab(goal="A:?a B:?b C:?c A:!_ C:!123", imaginal="Prev:!BA"):
        if b == "_" or a[-1] > b[-1]:
            print("Disk {} was moved to peg b.").format(a[-1])
            a, b = self.move(a, b)
            goal.modify(A=a, B=b)
            imaginal.modify(Prev="AB")
            self.repr_pegs(a, b, c)

    def ac(goal="A:?a B:?b C:?c A:!_ C:!123", imaginal="Prev:!CA"):
        if c == "_" or a[-1] > c[-1]:
            print("Disk {} was moved to peg c.").format(a[-1])
            a, c = self.move(a, c)
            goal.modify(A=a, C=c)
            imaginal.modify(Prev="AC")
            self.repr_pegs(a, b, c)

    def ba(goal="A:?a B:?b C:?c B:!_ C:!123", imaginal="Prev:!AB"):
        if a == "_" or b[-1] > a[-1]:
            print("Disk {} was moved to peg a.").format(b[-1])
            b, a = self.move(b, a)
            goal.modify(B=b, A=a)
            imaginal.modify(Prev="BA")
            self.repr_pegs(a, b, c)

    def bc(goal="A:?a B:?b C:?c B:!_ C:!123", imaginal="Prev:!CB"):
        if c == "_" or b[-1] > c[-1]:
            print("Disk {} was moved to peg c.").format(b[-1])
            b, c = self.move(b, c)
            goal.modify(B=b, C=c)
            imaginal.modify(Prev="BC")
            self.repr_pegs(a, b, c)

    def ca(goal="A:?a B:?b C:?c C:!_ C:!123", imaginal="Prev:!AC"):
        if a == "_" or c[-1] > a[-1]:
            print("Disk {} was moved to peg a.").format(c[-1])
            c, a = self.move(c, a)
            goal.modify(C=c, A=a)
            imaginal.modify(Prev="CA")
            self.repr_pegs(a, b, c)

    def cb(goal="A:?a B:?b C:?c C:!_ C:!123", imaginal="Prev:!BC"):
        if b == "_" or c[-1] > b[-1]:
            print("Disk {} was moved to peg b.").format(c[-1])
            c, b = self.move(c, b)
            goal.modify(C=c, B=b)
            imaginal.modify(Prev="CB")
            self.repr_pegs(a, b, c)
            
    def final(goal="C:123"):
        goal.clear()
        goal.clear()


model = Hanoi()
# ccm.log_everything(model)
model.goal.set("A:123 B:_ C:_")
model.imaginal.set("Prev:")
model.run()
