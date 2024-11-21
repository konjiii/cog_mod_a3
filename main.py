import ccm
from ccm.lib.actr import *

log = ccm.log(html=True)


class Hanoi(ACTR):
    goal = Buffer()
    memory = Buffer()

    def mem_add(self, mem, item):
        # add the item to the front of memory
        if mem == "_":
            mem = str(item)
        else:
            mem = str(item) + "," + mem

        # modify the memory buffer
        self.memory.modify(mem=mem)

    def mem_retrieve(self, mem):
        # get the first entry from the memory
        if mem.count(",") > 0:
            hd, tl = mem.split(",", 1)
        else:
            hd = mem
            tl = "_"
        # get the action and dest from the first entry
        action, dest = hd.split("|")

        # modify the memory buffer to remove the entry from memory
        self.memory.modify(mem=tl)

        return action, dest

    def move(goal="discs:?discs discs:!CCC", memory="mem:?mem"):
        # get the current subgoal from memory
        action, dest = self.mem_retrieve(mem)
        a_idx = int(action) - 1

        # if the disc is on the destination already don't do anything and go
        # to the next subgoal
        if discs[a_idx] != dest:
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
                # add the biggest blocking disc with the new destination as the
                # next subgoal to the memory
                self.mem_add(mem, "{}|{}".format(str(min(blocking) + 1), new_dest))
            else:
                # if nothing is blocking this subgoal move the disc to location
                # dest
                discs = discs[:a_idx] + dest + discs[a_idx + 1 :]
                goal.modify(discs=discs)
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
        memory.clear()


model = Hanoi()
# ccm.log_everything(model)
# schijf 123 op locatie A
#       "123"
discs = "AAA"
a = [disc + 1 for disc, loc in enumerate(discs) if loc == "A"]
b = [disc + 1 for disc, loc in enumerate(discs) if loc == "B"]
c = [disc + 1 for disc, loc in enumerate(discs) if loc == "C"]
print("Peg A has disks {}, peg B has disks {}, peg C has disks {}.\n".format(a, b, c))
# set the initial disc confguration
model.goal.set("discs:{}".format(discs))
# set the subgoals needed to finish the game
model.memory.set("mem:1|C,2|C,3|C")
model.run()
