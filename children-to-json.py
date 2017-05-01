'''
    Children to Json
    https://github.com/lucascassiano/cinema4d-children-to-json
    Version 1.0 - April 30, 2017

    This script exports .json files with:
    name
    objects[
        {
            name,
            position,
            rotation
        }
        ...
    ]
'''
import c4d
from c4d import documents, plugins, storage, gui

def main():
    #get selected object
    obj = doc.GetActiveObject()
    if obj is None:
        gui.MessageDialog("An object must be selected")
        return
    #finding where to save json file
    filePath = storage.LoadDialog(title="Save JSON file with Objects Positions", flags=c4d.FILESELECT_SAVE, force_suffix="json")
    if filePath is None:
        return

    #open file
    f = open(filePath,"w")

    #begin Json formatting
    f.write("{")
    #get the children
    children = obj.GetChildren()
    print obj.GetName() + " has "+ str(len(obj.GetChildren())) +" children"
    f.write('"name":'+'"'+obj.GetName()+'",\n')
    f.write('\t"objects":[\n')
    for i in range(0,len(children)):
        pos = children[i].GetAbsPos()
        rot = children[i].GetRelRot()
        name = children[i].GetName()
        print "+ " + children[i].GetName()
        print "   +Position:( "+str(pos.x) + "," + str(pos.y) + "," + str(pos.z) +")"
        print "   +Rotation:( "+str(pos.x) + "," + str(pos.y) + "," + str(pos.z) +")"
        f.write('\t{\n')
        f.write('\t\t"name":"'+name+'",')
        f.write('\n\t\t"position":['+str(pos.x)+','+ str(pos.y)+','+str(pos.z)+'],')
        f.write('\n\t\t"rotation":['+str(rot.x)+','+str(rot.y)+','+str(rot.z)+']')
        if i == len(children) - 1:
            f.write('\n\t}\n')
        else:
            f.write('\n\t},\n')
    f.write('\t]\n')
    #get path to sive file
    # Get a path to save the exported file

    #saving file
    f.write("}")
    f.close()

    c4d.CopyStringToClipboard("hi")
    gui.MessageDialog(".json file exported with success")
    pos=obj.GetRelPos()

if __name__=='__main__':
  main()
