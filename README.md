## Geodatabase Schema designer
Here is a small portion of a completed geodatabase schema:

![enter image description here](http://itsallearth.com/images/gdbDBdiagrams.JPG)
###Instructions:
The Geodatabase Schema designer can create a geodatabase diagram of any ESRI database.  

The script PrintGeoDatabaseSchemas.py will create a new folder called GEOschemas in your C: drive.  Inside the GEOschemas folder there will be three new text files: domains.txt, featureClasses.txt and relationshipClasses.txt. These files contain all the domains, feature classes, tables and relational classes in your geodatabase. 

When you open the python script and look at line number 7 you will see the following:  
```python
workspace = env.workspace = r'DatabaseConnections\GIS_MASTER.sde'
```
Replace  'GIS_MASTER.sde' with the name and path of any database that you want to diagram:
```python
workspace = env.workspace = r'DatabaseConnections\YOUR_GEODATABASE_NAME.sde'
```
note: You can easily find the correct syntax for the database path by: 
1. Opening ArcMap, opening the Python window. ![alt text](http://itsallearth.com/images/littelBoxArrowSmall.png "python window Icon")
2. Then open the catalog window and dragg your database into the Python window: ![alt text](http://itsallearth.com/images/littelBoxArrowPython.png "python window Icon") that you already have open. This will paste the database path into the python window.  
3. Copy that path and replace ```r'Database Connections\GIS_MASTER.sde'``` with the path you just copied.
4. Now run the script. It will create a folder called GEOschemas. Inside the GEOschemas folder you will see three text files: domains.txt, featureClasses.txt and relationshipClasses.txt. Your results will be in these three files.

## Using the Adobe Illustrator template: geodatabaseTemplate.ait 
The process of adding the text from running the script to Adobe Illustrator is pretty streight forward, however, some experience using Adobe Illustrator will be helpful.  The geodatabaseTemplate.ait template includes all the fonts, Icons, and graphics you will need to create your geodatabase schema.  
1. Copy the contents of the three text files and paste them unto the template.  
2. Use the EyeDropper tool to copy the formatting of the sample text to the text you pasted.  
3. Copy the tables, feature classes and relationship classes (remove the sample text that is inside)
4. Paste your text onto the appropriate table, feature class, relationship class etc.

You will need to draw lines for relationships your database has.
