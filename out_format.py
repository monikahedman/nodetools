import hou

red = hou.Color((0.8, 0.016, 0.016))

# Iterate if that name already exists
def setNodeName(iter=0):
    try:
        n.setName(f'OUT_{name}') if iter == 0 else n.setName(f'OUT_{name}{iter}')
    except:
        setNodeName(iter+1)

for n in hou.selectedNodes():
    # Set node color
    n.setColor(red)
    # Set node shape
    n.setUserData("nodeshape", "pointy")
    # Set name
    name = n.name()
    if not "OUT_" in name:
        setNodeName()
