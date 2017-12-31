import arcpy, os, sys
from arcpy import env

reload(sys)
sys.setdefaultencoding('utf-8')

workspace = env.workspace = r'Database Connections\GIS_MASTER.sde'

#Prints all Feature Datasets, their feature classes and fields inside them

textFile = open(r"C:\GEOschemas\featureClasses.txt","w")

def writeDatasets():
	datasets = arcpy.ListDatasets()
	datasets.sort()	
	for ds in datasets:
		for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
			#fc.sort()
			path = os.path.join(workspace, ds, fc)
			print "\n"
			#print "Path: "+path
			print path.split("GISOWN.", 1)[1]
			fcName1 = path.split("GISOWN.", 1)[1]
			fcName2 = fcName1.split("GISOWN.", 1)[1]
			textFile.write(fcName2+"\n")
			fields = arcpy.ListFields(path)
			for field in fields:
				print("{0}\t\t{1}\t\t{2}\t\t{3}\t{4}\t\t{5}\t{6}".format(field.name, field.type, field.isNullable, field.defaultValue, field.domain, field.precision, field.length))
				textFile.write("{0}\t\t{1}\t\t{2}\t\t{3}\t{4}\t\t{5}\t{6}".format(field.name, field.type, field.isNullable, field.defaultValue, field.domain, field.precision, field.length))
				textFile.write("\n")
			textFile.write("\n")
		textFile.write("\n\n")

def writeAllFC_notDsets(plp):
	fcList = arcpy.ListFeatureClasses(feature_type = plp)
	fcList.sort()
	for fc in fcList:
		db = r'Database Connections\GIS_MASTER.sde'
		fullName = db+"\\"+fc
		justTheName = fc		
		print "\n"	
		try:
			print justTheName.split("GISOWN.", 1)[1]
		except:
			print justTheName

		textFile.write("\n")
		try:
			textFile.write("\tFeature Class")
			textFile.write("\n\t"+justTheName.split("GISOWN.", 1)[1]+"\n")
			textFile.write("\n")
		except:
			textFile.write("\tFeature Class")
			textFile.write("\n\t"+justTheName)
			textFile.write("\n")
		fields = arcpy.ListFields(justTheName)
		textFile.write("{0}\t\t{1}\t\t{2}\t{3}\t{4}\t\t\t{5}\t{6}".format("Field name", "Data type", "Allow nulls", "Default Value", "Domain", "Precision", "  Length \n"))
		for field in fields:
			print("{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t{6}".format(field.name, field.type, field.isNullable, field.defaultValue, field.domain, field.precision, " "+str(field.length)))
			textFile.write("{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t\t{5}\t{6}".format(field.name, field.type, field.isNullable, field.defaultValue, field.domain, field.precision, "  "+str(field.length)))
			textFile.write("\n")
		textFile.write("\n\n")
	#textFile.close()	
	print "done"

def writeAllTables():
	tables = arcpy.ListTables()
	tables.sort()
	for table in tables:
		print table
		db = r'Database Connections\GIS_MASTER.sde'
		fullName = db+"\\"+table
		justTheName = table		
		print "\n"	
		try:
			print justTheName.split("GISOWN.", 1)[1]
		except:
			print justTheName
		textFile.write("\n")
		try:
			textFile.write("\tTable")
			textFile.write("\n\t"+justTheName.split("GISOWN.", 1)[1]+"\n")
			textFile.write("\n")
		except:
			textFile.write("\tTable")
			textFile.write("\n\t"+justTheName+"\n")
			textFile.write("\n")
		fields = arcpy.ListFields(justTheName)
		textFile.write("{0}\t\t{1}\t\t{2}\t{3}\t{4}\t\t\t{5}\t{6}".format("Field name", "Data type", "Allow nulls", "Default Value", "Domain", "Precision", "  Length \n"))
		for field in fields:
			print("{0}\t\t{1}\t\t{2}\t\t{3}\t{4}\t\t{5}\t{6}".format(field.name, field.type, field.isNullable, field.defaultValue, field.domain, field.precision, "  "+str(field.length)))
			textFile.write("{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t\t{5}\t{6}".format(field.name, field.type, field.isNullable, field.defaultValue, field.domain, field.precision, "  "+str(field.length)))
			textFile.write("\n")
		textFile.write("\n\n")
	#textFile.close()	
	print "done"

	
#-Start Formatted Domains -----------------------------------------------------------

def writeDomainsFormatted():
	textDomains = open(r"C:\GEOschemas\domains.txt","w")
	domains = arcpy.da.ListDomains(r'Database Connections\GIS_MASTER.sde')
	for domain in domains:
		print domain.domainType + ' Domain'
		print domain.name
		textDomains.write(domain.domainType + ' Domain'+'\n')
		textDomains.write(domain.name)
		textDomains.write('\n')
		print ' Description: ' + domain.description
		textDomains.write(' Description: ' + domain.description + '\n')
		print '    Field Type: ' + domain.type
		textDomains.write('  Field Type: ' + domain.type + '\n')
		print '   Split policy: ' + domain.splitPolicy
		textDomains.write('Split policy: ' + domain.splitPolicy + '\n')
		print 'Merge policy: ' + domain.mergePolicy
		textDomains.write('Merge policy: ' + domain.mergePolicy + '\n')
		textDomains.write('\t Code \t \t Description \n')
		if domain.domainType == 'CodedValue':
			coded_values = domain.codedValues
			for val, desc in coded_values.iteritems():
				print('\t {0} \t \t {1}'.format(val, desc))
				textDomains.write('\t {0} \t \t {1}'.format(val, desc) + '\n')
		elif domain.domainType == 'Range':
			print('Min: {0}'.format(domain.range[0]))
			textDomains.write('Min: {0}'.format(domain.range[0]) + '\n')
			print('Max: {0}'.format(domain.range[1]))
			textDomains.write('Max: {0}'.format(domain.range[1]) + '\n')
		print '\n'
		textDomains.write('\n \n')
	textDomains.close()

#-Start Relatinship Classes -----------------------------------------------------------

def detectRelationship():
	R_textFile = open(r"C:\GEOschemas\relationshipClasses.txt","w")
	rc_list = [c.name for c in arcpy.Describe(workspace).children if c.datatype == "RelationshipClass"]
	for rc in rc_list:
		rc_path = workspace + "\\" + rc
		des_rc = arcpy.Describe(rc_path)
		typ = des_rc.isComposite
		cardnty = des_rc.cardinality
		origin = des_rc.originClassNames
		destination = des_rc.destinationClassNames
		notice = des_rc.notification
		
		R_textFile.write("Retationship Class:")
		print "\tRetationship Class:"
		#R_textFile.write("Retationship Class:")
		rcf = rc.split("GISOWN.", 1)[1]
		#Relationship class name:
		print rcf 
		R_textFile.write("\n")
		R_textFile.write(rcf)
		#Type:
		if typ == True:
			fpLbl = des_rc.forwardPathLabel
			print "Type: Composite\t\t\tForward label: "+fpLbl
			R_textFile.write("Type: Composite\t\t\tForward label: "+fpLbl)
		else:
			fpLbl = des_rc.forwardPathLabel
			R_textFile.write("\n")	
			print "Type: Simple \t\t\tForward label: "+fpLbl
			#R_textFile.write("\n")
			R_textFile.write("Type: Simple\t\t\tForward label: "+fpLbl)

		R_textFile.write("\n")
		print "Cardinality: " + cardnty
		R_textFile.write("Cardinality: " + cardnty)
		print "Notification: " + notice + "\t\tBackward label:"+ des_rc.backwardPathLabel
		R_textFile.write("\n")
		R_textFile.write("Notification: " + notice + "\t\tBackward label: "+ des_rc.backwardPathLabel)
		print "Origin feature class\t\tDestination Feature Class"
		R_textFile.write("\n")
		R_textFile.write("Origin feature class\t\tDestination Feature Class")

		ocn = str(des_rc.originClassNames)
		ocnf = ocn.split("GISOWN.", 1)[1]
		ooo = ocnf.split("'",1)[0]

		dcn = str(des_rc.destinationClassNames)		
		dcnf = dcn.split("GISOWN.", 1)[1]
		ddd = dcnf.split("'",1)[0]

		print "Name: "+ooo+"\t\tName: "+ddd
		R_textFile.write("\n")
		R_textFile.write("Name: "+ooo+"\t\tName: "+ddd)

		origClassNm = des_rc.originClassNames
		R_textFile.write("\n")
		print "Primary key: "+des_rc.originClassKeys[0][0]+"\tForeign key: "+des_rc.originClassKeys[1][0]
		R_textFile.write("Primary key: "+des_rc.originClassKeys[0][0]+"\tForeign key: "+des_rc.originClassKeys[1][0])
		R_textFile.write("\n")
		R_textFile.write("\n")
		
		print("\n")
		print("\n")
	R_textFile.close()
	
textFile.write("\n")
textFile.write("----------------------------------------------------------------------------------------- \n")
textFile.write("All Tables: \n")
textFile.write("-----------------------------------------------------------------------------------------")
textFile.write("\n \n")

writeAllTables()

textFile.write("\n")
textFile.write("----------------------------------------------------------------------------------------- \n")
textFile.write("All Feature Classes that are contained in feature datasets: \n")
textFile.write("-----------------------------------------------------------------------------------------")
textFile.write("\n \n")

writeDatasets()

textFile.write("\n")
textFile.write("\n")

textFile.write("\n")
textFile.write("----------------------------------------------------------------------------------------- \n")
textFile.write("All POINT Feature Classes that are NOT contained in feature datasets): \n")
textFile.write("-----------------------------------------------------------------------------------------")
textFile.write("\n \n")

writeAllFC_notDsets('Point')

textFile.write("\n")
textFile.write("\n")

textFile.write("\n")
textFile.write("----------------------------------------------------------------------------------------- \n")
textFile.write("All LINE Feature Classes that are NOT contained in feature datasets): \n")
textFile.write("-----------------------------------------------------------------------------------------")
textFile.write("\n \n")

writeAllFC_notDsets('Line')

textFile.write("\n")
textFile.write("\n")

textFile.write("\n")
textFile.write("----------------------------------------------------------------------------------------- \n")
textFile.write("All POLYGON Feature Classes that are NOT contained in feature datasets): \n")
textFile.write("-----------------------------------------------------------------------------------------")
textFile.write("\n \n")

writeAllFC_notDsets('Polygon')

textFile.write("\n")
textFile.write("\n")

textFile.write("\n")
textFile.write("----------------------------------------------------------------------------------------- \n")
textFile.write("All ANNOTATION Feature Classes that are NOT contained in feature datasets): \n")
textFile.write("-----------------------------------------------------------------------------------------")
textFile.write("\n \n")

writeAllFC_notDsets('Annotation')

#textFile.write("\n")
#textFile.write("\n")

#textFile.write("\n")
#textFile.write("----------------------------------------------------------------------------------------- \n")
#textFile.write("All Feature Classes that are NOT contained in feature datasets): \n")
#textFile.write("-----------------------------------------------------------------------------------------")
#textFile.write("\n \n")

textFile.close()

#textDomains = open(r"C:\GEOschemas\domains.txt","w")
#textDomains.write("\n")
#textDomains.write("----------------------------------------------------------------------------------------- \n")
#textDomains.write("All Feature Domains: \n")
#textDomains.write("-----------------------------------------------------------------------------------------")
#textDomains.write("\n \n")
#textDomains.close()

writeDomainsFormatted()

#R_textFile = open(r"C:\GEOschemas\RelationshipClasses.txt","w")
#R_textFile.write("\n")
#R_textFile.write("----------------------------------------------------------------------------------------- \n")
#R_textFile.write("All Relationship Classes: \n")
#R_textFile.write("-----------------------------------------------------------------------------------------")
#R_textFile.write("\n \n")
#R_textFile.close()

detectRelationship()