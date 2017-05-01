# cinema4d-children-to-json
Cinema 4D (Python) plugin to export name, position and rotation of all children objects of a selected object

## Get Started
To use the script you just need to download it from the github page and open the script **children-to-json.py** with Cinema 4D Script manager
![](https://github.com/lucascassiano/cinema4d-children-to-json/raw/master/docs/how-to-use.gif)
## Json Structure 
  {
  
   name
    objects[
        {
            name,
            position,
            rotation
        }
        ...
    ]
   }

# References
[1] https://developers.maxon.net/docs/Cinema4DPythonSDK/html/index.html
[2] http://www.andrewnoske.com/wiki/Cinema_4D_-_Python_scripts
