# Multicolored Tea Pot Render UI:

Rendering picture of a colored teapot based on user's choice =)

The Pyside dialog that has the following elements:

  -  a view for displaying rendered image
  -  a view for displaying output log of the renderer
  -  a color picker to change the color of the objects in the scene
  -  a render button
   
When user clicks render button, the program use renderer python API to render a teapot frame to disk with user-defined color and display image and the log in the UI.


## Dependencies

  - UI : 
    -  Pyside2
    
  - Render Script: 
    -  maya
    -  mtoa
    -  arnold
    
## Setting it up

`python setup.py install`

If its not already done you may have to add to sys.path all paths associated with maya, mtoa and arnold
Otherthise you may face import errors when the script will run the rendering process in a maya standalone env.

`import sys`  

`sys.path.append("/autodesk/maya2019/bin/") # For maya`  

`sys.path.append("/opt/solidangle/mtoa/2019/scripts/") # For arnold & mtoa`

Maya working directory should be setted to the static folder where the teapot.ma is found 

## How it works

This app could be divided in 2 parts:

#### 1. The UI that store user's color choice and display rendered information

By running the following commands you'll get the shown UI:

`cd python`

`python main.py`


![picture1](/static/baseui.png)

![picture2](/static/colordialog.png)

![picture3](/static/renderui.png)


#### 2. The Arnold script that load a tea pot model scene, modify its color and render it given a color input.

The script is python/static/arnold_render_script.py it takes 3 flags as input(one/channel) and give below outputs
Picture and log file are saved in the static folder by the script and are then loaded back and displayed by the UI.

`cd python`

`python static/arnold_render_script.py -r 250 -g 0 -b 0`

![result2](/static/teapot2.png)

![result1](/static/teapot1.png)

### Comments
Had lot of issue settings up maya to work with the tools, I ended up having some segmentation fault errors while trying to run arnold renderer script in a maya.standalone context except for two times where it did works. There is something I've probably missed I think, because I've test the  code directly in maya and I was able to get rendered pictures/log file...
