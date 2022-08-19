import hou

yellow = hou.Color((1.0, 0.725, 0))

# Iterate if that name already exists
def setNodeName(iter=0):
    try:
        n.setName('CTRL') if iter == 0 else n.setName(f'CTRL{iter}')
    except:
        setNodeName(iter+1)

for n in hou.selectedNodes():
    # Set node color
    n.setColor(yellow)
    # Set node shape
    n.setUserData("nodeshape", "circle")
    # Set name
    setNodeName()
