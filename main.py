import ccm
from ccm.lib.actr import *

log = ccm.log(html=True)


class Hanoi(ACTR):
    goal = Buffer()
    imaginal = Buffer()

    def move(goal="discs:?discs discs:!CCC", imaginal="action:?action dest:?dest"):
        a_idx = int(action) - 1
        # if the disc is on the destination already go to the next biggest disc
        if discs[a_idx] == dest:
            imaginal.modify(action=a_idx + 2, dest=dest)
        else:
            # look for all blocking discs
            blocking = []
            for disc, loc in enumerate(discs):
                if disc > a_idx and (loc == discs[a_idx] or loc == dest):
                    blocking.append(disc)

            if len(blocking) > 0:
                # The destination of the smaller disc is the destination that
                # is not the destination and the current location of the
                # previous disc and the
                locs = list("ABC")
                locs.remove(discs[a_idx])
                locs.remove(dest)
                new_dest = locs[0]
                # move the biggest blocking disc to the new destination
                imaginal.modify(action=str(min(blocking) + 1), dest=new_dest)
            else:
                # move the disc to location dest
                discs = discs[:a_idx] + dest + discs[a_idx + 1 :]
                goal.modify(discs=discs)
                imaginal.modify(action=1, dest="C")
                print("Disk {} was moved to peg {}.".format(action, discs[a_idx]))
                A = [disc + 1 for disc, loc in enumerate(discs) if loc == "A"]
                B = [disc + 1 for disc, loc in enumerate(discs) if loc == "B"]
                C = [disc + 1 for disc, loc in enumerate(discs) if loc == "C"]
                print(
                    "Peg A has disks {}, peg B has disks {}, peg C has disks {}.\n".format(
                        A, B, C
                    )
                )

    def final(goal="discs:CCC"):
        goal.clear()
        imaginal.clear()


model = Hanoi()
# ccm.log_everything(model)
# schijf 123 op locatie A
#       "123"
discs = "AAA"
a = [disc + 1 for disc, loc in enumerate(discs) if loc == "A"]
b = [disc + 1 for disc, loc in enumerate(discs) if loc == "B"]
c = [disc + 1 for disc, loc in enumerate(discs) if loc == "C"]
print("Peg A has disks {}, peg B has disks {}, peg C has disks {}.\n".format(a, b, c))
model.goal.set("discs:{}".format(discs))
model.imaginal.set("action:1 dest:C")
model.run()