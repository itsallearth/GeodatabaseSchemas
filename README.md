## Geodatabase Schema designer
Here is a small portion of a completed geodatabase schema:

![enter image description here](http://itsallearth.com/images/gdbDBdiagrams.JPG)
## Instructions:
The Geodatabase Schema designer can create a geodatabase diagram of any ESRI geo-database.  

The script **PrintGeoDatabaseSchemas.py** will create a new folder called GEOschemas in your C: drive.  Inside the GEOschemas folder there will be three new text files: domains.txt, featureClasses.txt and relationshipClasses.txt. These files contain all the domains, feature classes, tables and relational classes in your geodatabase. 

When you open the python script and look at line number 7 you will see the following:  
```python
db = r'C:\Users\Bruce\Documents\ArcGIS\Default.gdb'
```
Replace  'C:\Users\Bruce\Documents\ArcGIS\Default.gdb' with the name and path of any database that you want to diagram:
```python
db = r'DatabaseConnections\YOUR_GEODATABASE_NAME.sde'
```
note: Here is an easy way to find the correct path for your geodatabase: 
1. Open ArcMap and then open the Python window ![alt text](http://itsallearth.com/images/littleBoxArrow-.png "python arrow Icon").
2. Then open the catalog window and drag your database into the Python window that you already have open ![alt text](http://itsallearth.com/images/littelBoxArrowPython.png "python window Icon") . This will paste the database path into the python window.  
3. Copy that path and replace ```r'Database Connections\GIS_MASTER.sde'``` with the path you just copied.
4. Run the script and a folder will be created in your C:/ called GEOschemas. Inside the GEOschemas folder there will be three text files: domains.txt, featureClasses.txt and relationshipClasses.txt. These are where you will find all the schema inforation for your geodatabase.

## Using the Adobe Illustrator template:
5. Open the **geodatabaseTemplate.ait** template in Adobe Illustrator. This template includes all the fonts, Icons, and graphics you will need to create your geodatabase schema.
6. Copy the contents of the three text files that the script created and paste them unto the template.
7. Use Adobe Illustrators EyeDropper tool, copy the formatting of the sample text to the text you pasted in step 2.
8. Copy the graphical tables, feature classes and relationship classes (without the sample text).
9. Now paste the text you formatted in step 3 onto the appropriate graphical tables, feature classes and relationship classes.
10. You will need to draw lines that represent the schema relationships.
