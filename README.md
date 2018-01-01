## Geodatabase Schema designer
Here is a small portion of a completed geodatabase schema:

![Image of geoDBdiagrams](http://itsallearth.com/images/geoDBdiagrams.JPG)

### Instructions:
The Geodatabase Schema designer can create a geodatabase diagram of any ESRI database.  
The script PrintGeoDatabaseSchemas.py will create a new folder called GEOschemas in your C: drive.  Inside the GEOschemas folder there will be three new text files: domains.txt, featureClasses.txt and relationshipClasses.txt. These files contain all the domains, feature classes, tables and relational classes in your geodatabase. 

1.	When you open the python script and look at line number 7 you will see the following:  
#7  workspace = env.workspace = r'Database Connections\GIS_MASTER.sde'. 
    Replace r'Database Connections\GIS_MASTER.sde' with the name and path of any database that you want to diagram. 
    note: You can easily find the correct syntax for the database path by opening ArcMap, opening the Python window %%%  , then opening the catalog window and dragging your database into the Python window  %%%  you already have open. When you drag the database into the Python window the path will be copied there.  Copy that path and replace r'Database Connections\GIS_MASTER.sde' with the path you just copied.
b.	When you run the script it will create a folder called GEOschemas. Inside the GEOschemas folder you will see three text files: domains.txt, featureClasses.txt and relationshipClasses.txt. You will find the results of the script in these three files.
