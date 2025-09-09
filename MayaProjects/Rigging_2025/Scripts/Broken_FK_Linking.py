import maya.cmds as cmds  # type: ignore

# Get selection, separate parent and child control
sels = cmds.ls(sl=True)
parent_ctrl = sels[0]
child_ctrl = sels[1]

# Get the parent control of the child group
child_ctrl_grp = cmds.parentConstraint(parent_ctrl, parent=True)[0]

# Create contraints
p_constraint1 = cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipRotate=['x', 'y', 'z'], weight=1)[0]
p_constraint2 = cmds.parentConstraint(parent_ctrl, child_ctrl_grp, mo=True, skipTranslate=['x', 'y', 'z'], weight=1)[0]
cmds.scaleConstraint(parent_ctrl, child_ctrl_grp, weight=1)

# Create attributes
if not cmds.attributeQuery('FollowTranslate', node=child_ctrl, exists=True):
    cmds.addAttr(child_ctrl, ln='FollowTranslate', at='double', min=0, max=1, dv=1)
    cmds.setAttr('%s.FollowTranslate' % (child_ctrl), e=True, keyable=True)

if not cmds.attributeQuery('FollowRotate', node=child_ctrl, exists=True):    
    cmds.addAttr(child_ctrl, ln='FollowRotate', at='double', min=0, max=1, dv=1)
    cmds.setAttr('%s.FollowRotate' % (child_ctrl), e=True, keyable=True)

# Connect attributes
cmds.connectAttr('%s.FollowTranslate' % (child_ctrl), '%s.w0' % (p_constraint1), f=True)
cmds.connectAttr('%s.FollowRotate' % (child_ctrl), '%s.w0' % (p_constraint2), f=True)