## Geodatabase Schema designer
Here is a small portion of a completed geodatabase schema:

![Image of geoDBdiagrams](http://itsallearth.com/images/geoDBdiagrams.JPG)

### Instructions:
The Geodatabase Schema designer can create a geodatabase diagram of any ESRI database.  
The script PrintGeoDatabaseSchemas.py will create a new folder called GEOschemas in your C: drive.  Inside the GEOschemas folder there will be three new text files: domains.txt, featureClasses.txt and relationshipClasses.txt. These files contain all the domains, feature classes, tables and relational classes in your geodatabase. 

1.	When you open the python script and look at line number 7 you will see the following:  
```#7  workspace = env.workspace = r'Database Connections\GIS_MASTER.sde'```. 
    Replace r'Database Connections\GIS_MASTER.sde' with the name and path of any database that you want to diagram. 
    note: You can easily find the correct syntax for the database path by opening ArcMap, opening the Python window Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1") , then opening the catalog window and dragging your database into the Python window  %%%  you already have open. When you drag the database into the Python window the path will be copied there.  Copy that path and replace r'Database Connections\GIS_MASTER.sde' with the path you just copied.
b.	When you run the script it will create a folder called GEOschemas. Inside the GEOschemas folder you will see three text files: domains.txt, featureClasses.txt and relationshipClasses.txt. You will find the results of the script in these three files

```python
s = "Python syntax highlighting"
print s
```
1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses
