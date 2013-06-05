##################################################################
# Name: Frederick Awuah-Gyasi
# Project: HITS
# Supervisor: Dr Tim Miller
# Version:1.0.0
# Module: process
##################################################################


import re
import Part
import Product
import Product_State
import DomainClass
import cx_Oracle
import DBconnection


def ParseInventoryPart(filename): 
   """
        Purpose: For parse the inventory file into a format that can be input into the part table in the database.
        Argument(s): Inventory file
        Returns: Tuple of tuples ( Part Number, Part Description, Part type)
   """


   parts = list()
   with open(filename,'rt') as data:
       for line in data:
          if line.startswith('#'):
            continue

          if line.count('::') == 2:
             
             temp = line.split('::')
             temp1= proc_parttype(temp[0])  #retrieving part type from proc_parttype method defined below
             temp2= (temp[1],temp[2],temp1,'','','')
             if temp2 not in parts: 

                parts.append (temp2)

          if line.count('::') == 4:

             temp = line.split('::')
             temp1= proc_parttype(temp[0])  #retrieving part type from proc_parttype method defined below
             temp2= (temp[1],temp[2],temp1,'','','')
             if temp2 not in parts:
                parts.append (temp2)

          if line.count('::') == 7:
 
             temp = line.split('::')
             temp1= proc_parttype(temp[0])  #retrieving part type from proc_parttype method defined below
             temp2= (temp[2]+temp[3],temp[1],temp1,'','','')
             if temp2 not in parts:
                parts.append (temp2)
             
          if line.count('::') == 9:
             temp = line.split('::')
             temp1= proc_parttype(temp[0])  #retrieving part type from proc_parttype method defined below
             temp2= (temp[2] +temp[3],temp[1],temp1,'','','')
             if temp2 not in parts:
                parts.append (temp2)
       
          if line.count('::') == 12:
             temp = line.split('::')
             temp1= proc_parttype(temp[0])  #retrieving part type from proc_parttype method defined below
             temp2 = (temp[2] + temp[3], temp[5],temp1,'','','')
             if temp2 not in parts:
                parts.append (temp2)
   fullparts= tuple(parts)
   return fullparts   

def AddPart(filename):
   """This is to add new part to the part table
      *Note*: This uses data from 
   """
   #Doing the insert
   NewPart= Part.Part()
   fullparts = ParseInventoryPart(filename)
   for data in fullparts:NewPart.insertPart(*data)





def ParseInventoryPartType(dataline):
   """
   Purpose: This function gives the part type of every entry(line) in the inventory file. It will usually be used by other function like 'ParseInventoryPart'
   Argument(s) : A line  of data from in the inventory file
   Return(s) : String . Which will be a part: CPU,CHASSIS,MEMORY,etc
   """
    
   b=dataline.split('.') # converting dataline into a list 

   if len(b) ==1: 
      return 'CHASSIS'
   
   if len(b) == 3 and b[1] == '01':
      return 'SWITCH'

   if len (b) == 3 and b[1] =='04':
      return 'SERVER'

   if len(b) == 5 and b[3] == '00':
      return 'CPU'
   
   if len (b) == 5 and b[3] == '01':
      return 'RAM'
  
   if len (b) == 5 and b[3]== '02' :
      return 'HDD'
   else: return 'OTHER'


def ParseInventoryProduct(filename):
   """
        Purpose: This function parse the inventory file into the required columns for reconcile process.
        Argument(s): Inventory file
        Returns: Tuple of tuples (Product Serial Number, Parent product Serial number, Part number) 

   """


   products = list()
   inventory =list() # Actuall list of products to be returned. 
   with open(filename,'rt') as data:
       for line in data:
          if line.startswith('#'):
            continue

          if line.count('::') == 2:

             temp = line.split('::') # split lines into an list. 
             tempnew = temp[0].split('.') # split first element 
             tempnew1 = (tempnew[0],tempnew[1],tempnew[2]) #
             tempnew12= '.'.join(tempnew1) # reconstructing code for the blade(parent)
             #temp2= (temp[1],temp[2],'','','','')
             for product in products: 
                if product[0] == tempnew12:
                   temp2 = (temp[0],product[1] + tempnew[4],product[1],temp[1]) #creating a serial number 4 cpu using the blade serial number + cpu socket number. 
                   tempInventory = (product[1]+tempnew[4],product[1],temp[1])

                   if temp2 not in products:
                      products.append (temp2)
                   if tempInventory not in inventory: 
                      inventory.append (tempInventory)

          if line.count('::') == 4:

             temp = line.split('::')
           
             #------------------------
             tempnew = temp[0].split('.') # split first element 
             tempnew1 = (tempnew[0],tempnew[1],tempnew[2]) #
             tempnew12= '.'.join(tempnew1) # reconstructing code for the blade(parent)
            
             for product in products:
                if product[0] == tempnew12:
             #------------------------
                   temp2= (temp[0],temp[3],product[1],temp[1])
                   tempInventory = (temp[3],product[1],temp[1])   
                   if temp2 not in products:
                      products.append (temp2)
                   if tempInventory not in inventory: 
                      inventory.append (tempInventory)

          if line.count('::') == 7:

             temp = line.split('::')
             #---------------------------------------
             tempnew = temp[0].split('.') # split first element 
             tempnew1 = tempnew[0] #
             for product in products:
                if product[0] == tempnew1:
             #---------------------------------------
                   temp2= (temp[0],temp[4],product[1],temp[2]+temp[3])
                   tempInventory = (temp[4],product[1],temp[2]+temp[3])

                   if temp2 not in products:
                      products.append (temp2)
                   if tempInventory not in inventory: 
                      inventory.append (tempInventory)

          if line.count('::') == 9:
             temp = line.split('::')
             temp2= (temp[0],temp[4],'',temp[2] +temp[3])
             tempInventory = (temp[4],'',temp[2] +temp[3])
             
             if temp2 not in products:
                products.append (temp2)
             if tempInventory not in inventory: 
                inventory.append(tempInventory)

          if line.count('::') == 12:
             temp = line.split('::')
             
             tempnew = temp[0].split('.') # split first element 
             tempnew1 = tempnew[0] #
             for product in products:
                if product[0] == tempnew1:
            
                   temp2 = (temp[0],temp[4],product[1],temp[2] + temp[3])
                   tempInventory = (temp[4],product[1],temp[2] + temp[3])
                   if temp2 not in products:
                      products.append (temp2)

                   if tempInventory not in inventory: 
                      inventory.append (tempInventory)

   fullproducts = tuple(products)   #(trackingCode,Product SeialNumber,Parent Product Serial Number,PartNumber)
   fullInventory = tuple(inventory) # (Product SeialNumber,Parent Product Serial Number,PartNumber) 
   return fullInventory
   NewProduct = Product.Product()
   
  # for product1 in fullproducts:
     # NewProduct.insertProduct(*product1)

def InsertDataInventoryTBL (filename):
       '''
        Purpose: To  populate a temporary three-column( Product Serial Number, Parent Product Id,Part Number) table in 
                 the database for the reconcile process. It deletes any previously created on and recreate afresh whenever its called.
        Argument(s) : Inventory file.
        Return: 1 if succesfully created. 
       '''


       connection = DBconnection.databaseConnection()  # Connection to the database. 
       tableName = 'INVENTORYTBL'
       colnames  = ('PRODUCT_SERIAL_NUM','PARENT_PRODUCT_SERIAL_NUM','PART_NUMBER')
      
       cursor1 = connection.cursor()  # TO TRUNCATE THE INVENTORYTBL
       cursor2 = connection.cursor()  # TO DO INSET INTO INVENTORYTBL
       
       query1  = "TRUNCATE TABLE INVENTORYTBL"
       try:
   
          cursor1.execute(query1)
          connection.commit()
       except cx_Oracle.IntegrityError,exception:
          error,=exception
          print "Oracle error :" ,error.message

       InventoryDataSet = ParseInventoryProduct(filename)
       
       try: 
          cursor1.execute(query1)
          connection.commit()
          for product in InventoryDataSet: 
             query2= "INSERT INTO {0} ({1}) VALUES {2} ".format (tableName,','.join(map(str,colnames)),product)
             cursor2.execute(query2)
             connection.commit()
       except cx_Oracle.IntegrityError,exception:
          error,=exception
          print "Oracle error :" ,error.message
         
       else: return 1
      
       finally: 
          cursor1.close()
	  cursor2.close()
 
def InventorytbeToInventoryTempCopy():
   """To transfer data from Inventorytbl into InventoryTempCopy"""
   
   connection = DBconnection.databaseConnection()  # Connection to the database.
   cursor     = connection.cursor() # FOR THE TRANSFER
   table1     = "INVENTORYTBL"
   table2     = "INVENTORYTEMPCOPY"
   query      = "SELECT * FROM {0}  INTO {1} ".format(table1,table2)
   
   try: 
      cursor.exuecute(query)
      connection.commit()
   except: 
      pass 
   else: return 1

   finally: 
      cursor.close()

def InventoryTempCopyToHitsreconcile():
   """To transfer data from Inventorytbl into InventoryTempCopy"""

   connection = DBconnection.databaseConnection()  # Connection to the database.
   cursor     = connection.cursor() # FOR THE TRANSFER
   table1     = "INVENTORYTEMPCOPY"
   table2     = "HITSRECONCILE"

   query      = "SELECT * FROM {0}  INTO {1} ".format(table1,table2)
   
   try:
      cursor.exuecute(query)
      connection.commit()
   except:
      pass
   else: return 1

   finally:
      cursor.close()
     
def GetContent(table):
   """
   Purpose: TO do simple select all from the table given. 
   Returns: Tuple of tuples. 

   """
   connection = DBconnection.databaseConnection()  # Connection to the database.

   #CURSOR
   #------
   cursor = connection.cursor()

   #QUERY
   #-----
   query = "SELECT * FROM {0}".format(table)
   try:

      cursor.execute(query)
      rows = cursor.fetchall()
      return rows
   
   finally:
      cursor.close()


def DisplayContent(Products):
   """
   TO display the content of arrays to the command line interface. 
   """
   count = 1
   print "No. ","     PROUDUCT S/N      "," PARENT PRODUCT S/N", " PART NUMBER"
   print "--- ","---------------------- ","---------------------","--------------"
   for Product in Products:
      print "{0}    {1:20}    {2:20}  {3}".format (count,Product[0],Product[1],Product[2])
      count = count + 1




def GetAllCurrentActiveProducts(table = 'HITSRECONCILETBL'): 
   """
   Purpose : Provide a list of all active products according to HITS database. 
   Argument: None
   Returns : A tuple of tuples. Product Serial Number, Parent Product Serial , Part Number. 
   HITSRECONCILE is a view indatabaseConnection()  # Connection to the database. the HITS DATABASE WITH 
   """
   return GetContent(table)

   
def DisplayAllCurrentActiveProducts(): 
   """
   Purpose: This function puts the data returned by 'GetAllCurrentProducts' into a tabular form. 
            This will be useful for command Line interface representation. 
   Argument(s): None
   Returns: a Table of results. four columns ( Number, Product Serial Number, Parent Serial Number, Part Number)

  
   """
   #GETTING ALL ACTIVE PRODUCTS
   #---------------------------
   ActiveProducts = GetAllCurrentActiveProducts()
   
   #DISPLAY ACTIVE PRODUCTS TO COMMAND LINE
   #-------------------------------------
   DisplayContent(ActiveProducts)

def GetParentProductWithComponents(): 
   """
   Purspose: Provides parent components with their internal components
   Argument(s) : (Optional) Product Serial Number. if not provided all Parent products will all be listed.
   Returns: A dictionary of Parents and Children. Parent Serial Number as Key and Tuple of Children Serial number as Value.

   """
   count = 1
   print "No. ","     PROUDUCT S/N      "," PARENT PRODUCT S/N", " PART NUMBER"
   print "--- ","---------------------- ","---------------------","--------------"
   for Product in Products:
      print "{0}    {1:20}    {2:20}  {3}".format (count,Product[0],Product[1],Product[2])
      count = count + 1




def GetAllCurrentActiveProducts(table = 'HITSRECONCILE'): 
   """
   Purpose : Provide a list of all active products according to HITS database. 
   Argument: None
   Returns : A tuple of tuples. Product Serial Number, Parent Product Serial , Part Number. 
   HITSRECONCILE is a view indatabaseConnection()  # Connection to the database. the HITS DATABASE WITH 
   """
   data = GetContent(table)
   return data
   
def DisplayAllCurrentActiveProducts(): 
   """
   Purpose: This function puts the data returned by GetAllCurrentProducts into a tabular form. 
            This will be useful for command Line interface representation. 
   Argument(s): None
   Returns: a Table of results. four columns ( Number, Product Serial Number, Parent Serial Number, Part Number)

  
   """
   #GETTING ALL ACTIVE PRODUCTS
   #---------------------------
   ActiveProducts = GetAllCurrentActiveProducts()
   
   #DISPLAY ACTIVE PRODUCTS TO COMMAND LINE
   #-------------------------------------
   DisplayContent(ActiveProducts)

def GetParentProductWithComponents(): 
   """
   Purspose: Provides parent components with their internal components
   Argument(s) : (Optional) Product Serial Number. if not provided all Parent products will all be listed.
   Returns: A dictionary of Parents and Children. Parent Serial Number as Key and Tuple of Children Serial number as Value.

   """
   connection = DBconnection.databaseConnection()  # Connection to the database.
   cursor = connection.cursor()
   tableName = 'HITSRECONCILE'
   colnames  = ('PRODUCT_SERIAL_NUM','PARENT_PRODUCT_SERIAL_NUM','PART_NUM') 
   query = "SELECT PARENT_PRODUCT_SERIAL_NUM,PRODUCT_SERIAL_NUM,PART_NUM FROM {0}".format(tableName)
   parentsNComponents = {} # An empty dictionary. To contain Parents and Internal components. 
   
   try:
      cursor.execute(query)
      rows = cursor.fetchall()
      #return rows 
      #CREATING THE DICTIONARY 
      for component in rows:
         parentsNComponents.setdefault(component[0],[]).append((component[1],component[2]))
      return parentsNComponents
      #print parentsNComponents
     
   finally: 
      cursor.close()

def DisplayParentProductWithComponents():
   """
   Purspose: Provides parent components with their internal components. In a tabular form for command line display. 
   Argument(s) : (Optional) Product Serial Number. if not provided all Parent products will all be listed.
   Returns: A tabular representation of Parents and Children. 
   """
   Products = GetParentProductWithComponents()
   count1 = 1
   count2 = 1

   for x,y in Products.iteritems():
      print "---------------------------------------------------------"
      print "                 INTERNAL COMPONENT(S) OF : ",x
      print "No.           Product S/N               Part Number      "
      print "====      ======================   ======================" 
      for u in y: 
         print "{0}.      {1:20}                   {2}                   ".format(count1,u[0],u[1])
         count1= count1 + 1




def GetAllDiscrepancies():
   """
   Purpose: To execute query to return all discrepancies between HITS DB and the temporary inventory table.There will be no starts attached 

   Argument(s) : No argument 
   Returns: A dictionary: Key => discrepancies,Value=>Tuple of tuples of  : Product Serial Number , Parent Serial Number, Part Number.

   """
   
  
   #GETTING DATA FROM EXECUTION.
   #----------------------------
   newproducts = GetContent('NEWPRODUCT')
   replaced    = GetContent('REPLACED')
   relocated   = GetContent('NEWRELOCATE')
   removed     = GetContent('REMOVED')
   none        = GetContent('NONE')
    
   # THE DICTIONARY OF ALL DISCREPANCIES
   # ------------------------------------
   AllDiscrepancies = {'NEW PRODUCT':newproducts,'REPLACED':replaced,'NEWRELOCATE':relocated,'REMOVED':removed,'NONE':none}

   #RETURN
   #------
   return AllDiscrepancies


def DisplayDescrepancyWithState(): 
   """
   Purpose: List all discrepancy between HITS DB and the temporary inventory table. 
            Discrepancies types:
                  None:- For the case of no change in state. 
                  New : Case where product does not exist in HITS database. 
                  Relocated: This is the case of products with locations changed
                  Replaced: This is the case of products with identical parent, part number and part description but serial numbers have changed.
                  Removed: Product in HIT database but had no match in Inventory table. 
  Returns: Special tabular structure with 4 columns:
                                           Product Serial Number
                                           Parent Product Serial Number
                                           Part Number
                                           Discrepancy Type

 
   """
   #GETTING ALL DISCREPANCIES
   #------------------------
   AllDiscrepancies = GetAllDiscrepancies()

   #DISPLAY FOR THE COMMAND LINE INTERFACE
   #-------------------------------------------

   #============================================
   #         ALL DISCREPANCIES          
   #=============================================
   #*********************************************
   # TYPE: NEWPRODUCTS (2) 
   #----------------------------------------------
   #No.   Product S/N     Parent S/N   Part Number
   #+++   +++++++++++     ++++++++++   ++++++++++
   #1.    VMJKK22323      JIJI888388   HPH9999
   #2.    HKHHH88899      VMJKK22323   YUU9999
   #*********************************************
   # TYPE: REPLACED (1)
   #---------------------------------------------
   #No.   Product S/N     Parent S/N   Part Number
   #+++   +++++++++++     ++++++++++   ++++++++++
   #1.    VMJKK22323      JIJI888388   HPH9999
   #*********************************************
   # TYPE: RELOCATED (1)
   #----------------------------------------------
   #No.   Product S/N     Parent S/N   Part Number
   #+++   +++++++++++     ++++++++++   ++++++++++
   #1.    VMJKK22323      JIJI888388   HPH9999
   #*********************************************

   print "============================================================================"
   print "                            ALL DISCREPANCIES                               "
   print "============================================================================"
   
   for type,products in AllDiscrepancies.iteritems():
      count = 1 
      print "*****************************************************************************"
      print " TYPE : {0} ({1}) ".format(type,len(products))
      print "-----------------------------------------------------------------------------"
      DisplayContent(products)
   print "*****************************************************************************"
    




def GetAllNewProducts(): 
   """
   Purpose: List all all products found in the inventory not found in HIT database. 
   Argument(s) : None 
   Return: This returns a tuple of tuple; (Product Serial Number, Parent Serial Number, Part Number)

   """
   #RETURN ALL NEW PRODUCTS 
   #------------------------
   data =  GetContent('NEWPRODUCT')  
   return data

def DisplayAllNewProducts():
   """
    Purpose: This does same as GetAllNewProducts except that it places results in a tabular form. So can be displayed in a command line for instance. 
    Argument(s): None
    Returns: a Table of results. four columns ( Number, Product Serial Number, Parent Serial Number, Part Number)

   """
   #GETTING NEWPRODUCTS 
   #-------------------
   NewProducts = GetAllNewProducts()

   #DISPLAYING NEW PRODUCTS ON THE COMMAND LINE
   #------------------------------------------
   DisplayContent(NewProducts)


def GetAllMissingProducts():
   """
   Purpose: This function give all products that are found in HITS database but absent from from the Inventory table . 
   Argument(s): None
   Returns: Tuple of tuples ( Product Serial Number, Parent Product Serial Number, Part Number)

   """
   #GETTING ALL MISSING PRODUCTS FROM THE REMOVED VIEW
   #-------------------------------------------------
   data = GetContent('REMOVED')
   return data



def DisplayAllMissingProducts(): 
   """
   Purpose: This function puts the data returned by GetAllMissingProducts into a tabular form. This will be useful for command Line interface representation. 
   Argument(s): None
   Returns: a Table of results. four columns ( Number, Product Serial Number, Parent Serial Number, Part Number)

   """
   #MISSING PRODUCTS
   #---------------
   AllMissingProducts = GetAllMissingProducts()
   
   #DISPLAY MISSING PRODUCTS
   #------------------------
   DisplayContent(AllMissingProducts)


def GetAllRelocatedProducts():
   """
   Purpose: Gets all products which a change in location. These products are present in both inventory database and HITS database but have different location
   Argument(s): None
   Returns:Tuple of tuples ( Product Serial Number, Parent Product Serial Number, Part Number)

   """
   return GetContent('NEWRELOCATE')


def DisplayAllRelocatedProducts():
   """
   Purpose: This function puts the data returned by GetAllRelocatedProducts into a tabular form. This will be useful for command Line interface representation. 
  Argument(s): None
  Returns: a Table of results. four columns ( Number, Product Serial Number, Parent Serial Number, Part Number)

   """
   #GETTING RELOCATED PRODUCTS
   #--------------------------
   Relocated = GetAllRelocatedProducts()
   
   #DISPLAYING RELOCATED PRODUCTS
   #----------------------------
   DisplayContent(Relocated)


def GetAllReplacedProducts():
   """
   Purpose: Gets all products which a change in location. These products are present in both inventory database and HITS database but have different location
   Argument(s): None
   Returns:Tuple of tuples ( Product Serial Number, Parent Product Serial Number, Part Number,RMA)

   """

   #REPLACED PRODUCTS: THESE ARE PROJECTED TO HAVE BEEN REPLACED
   #------------------------------------------------------------
   return GetContnet('REPLACED')

def DisplayAllReplacedProducts():
   """
   Purpose: This function puts the data returned by GetAllRelocatedProducts into a tabular form. This will be useful for command Line interface representation. 
   Argument(s): None
   Returns: a Table of results. four columns ( Number, Product Serial Number, Parent Serial Number, Part Number,RMA)

   """
   #DISPLAY PROJECTED REPLACED PRODUCTS
   #-----------------------------------
   DisplayContent (GetAllReplacedProducts())

def DisplayAllLocation(): 
   """
         Purpose: List all location used by HPC and the Networking teams.
        Argument(s): None
        Return: List of locations. 
   """

   NewLocation = DomainClass.Domain('Location')
   
   Locations = NewLocation.get_all_entries()
   
   count = 1
   if ( len(Locations) != 0 ) : 
      print "***************"
      print "No.   LOCATION"
      print "---------------"
      for Location in Locations: 
         print "{0}   {1}".format(count,Location[1])
         count = count + 1

def DisplaySupportType():
   """
        Purpose: List all Support type for products.
        Argument(s): None
        Return: list of Suppport types.


   """
   #SUPPORT MODULE FOR THE SUPPORT CLASS ( TABLE )
   #----------------------------------------------
   import Support
  
   #SUPPORT OBJECT
   #--------------
   NewSupport = Support.Support()
   Supports = NewSupport.getAllSupport()

   count = 1
    
   if (len(Supports) != 0 ) : 
      print "No.   REFERENCE NO.   START DATE   END DATE   SUPPORT LEVEL"
      print "---   -------------   ----------   --------   -------------"
      for support in Supports: 
         print "{0}   {1:15}          {2:15}       {3:15}     {4}".format(count,support[1],support[2],support[3],support[4])
         count = count + 1
   


def GetProductState(statetype):
   """
   this is an auxilliary function for determining products states: RETURNED AND DISPOSED. 
   """ 
   connection = DBconnection.databaseConnection()  # Connection to the database. 
   cursor = connection.cursor()
   tableName1 = 'HITSRECONCILE'
   tableName2 = 'PRODUCT_STATE_TYPE'
   tableName3 = 'PRODUCT_STATE' 
   query =" SELECT H.PRODUCT_SERIAL_NUM,H.PARENT_PRODUCT_SERIAL_NUM,H.PART_NUM,P.PRODUCT_STATE_CHANGE_DATE FROM {0} H,{1} P WHERE H.PRODUCT_SERIAL_NUM IN(SELECT PRODUCT_SERIAL_NUM FROM PRODUCT WHERE PRODUCT_ID IN (SELECT PRODUCT_ID FROM PRODUCT_STATE WHERE PRODUCT_STATE_TYPE_ID IN ( SELECT PRODUCT_STATE_TYPE_ID FROM PRODUCT_STATE_TYPE WHERE PRODUCT_STATE_TYPE_NAME = '{2}')".format(tableName1,tableName3,statetype) 

   try: 
      cursor.execute(query)
      rows = cursor.fetchall()
      return rows
   except: 
      pass
   finally: 
      cursor.close()


def GetAllDisposedProducts():
   """
           Purpose: Gets all products which have been disposed. These products are will remain in the HITS database but with the state indicating DISPOSED.
        Argument(s): None
        Returns:Tuple of tuples ( Product Serial Number, Parent Product Serial Number, Part Number,DisposedDate)
   """ 
   return GetProductState('DISPOSED')



def GetAllReturnedProducts():
   """
           Purpose: Gets all products which have been disposed. These products are will remain in the HITS database but with the state indicating REMOVED.
        Argument(s): None
        Returns:Tuple of tuples ( Product Serial Number, Parent Product Serial Number, Part Number,ReturnDate)
   """
   return GetProductState('RETURNED')

def DisplayAllReturnedProducts(): 
   """
        Purpose: Gets all products which have been disposed. These products are will remain in the HITS database but with the state indicating RETURNED.
        Argument(s): None
        Returns: a table of results ( Product Serial Number, Parent Product Serial Number, Part Number,ReturnDate)
   """
   #Getting all returned products
   Returned = GetAllReturnedProducts()
   count = 1
   if (Returned is not None ):
      print "NO.  PRODUCT S/N   PARENT PRODUCT S/N   PART NUMBER   RETURN DATE"
      print "---  -----------   ------------------   -----------   -----------"
      for product in Returned:
         print "{0}  {1:15}        {2:15}               {3:15}        {4}".format(count,Return[0],Return[1],Return[2],Return[3])
         count = count + 1
  

def DisplayAllDisposedProducts():
   """
        Purpose: Gets all products which have been disposed. These products are will remain in the HITS database but with the state indicating RETURNED.
        Argument(s): None
        Returns: a table of results ( Product Serial Number, Parent Product Serial Number, Part Number,ReturnDate)
   """
   #Getting all Disposed products
   Returned = GetAllDisposedProducts()
   count = 1
   if (Returned is not None):
      print "NO.  PRODUCT S/N   PARENT PRODUCT S/N   PART NUMBER   DISPOSE DATE"
      print "---  -----------   ------------------   -----------   -----------"
      for product in Returned:
         print "{0}  {1:15}        {2:15}               {3:15}        {4}".format(count,Return[0],Return[1],Return[2],Return[3])
         count = count + 1


def InstallNewProduct(): 
   """
   This method callthe NewProduct View in the HITS database and if there is data present 
   it does the 
        1.insert into the product table
        2.insert into the product state table
        3.Update product state to INSTALLED
   """

   NewProducts = GetAllNewProducts() #DATA FROM NEWPRODUCTS VIEW IN HITSDB
   NewProduct = Product.Product() #OBJECT OF PRODUCT TABLE
   NewProductState = Product_State.Product_State()
   NewStateType = DomainClass.Domain('PRODUCT_STATE_TYPE') # OBJECT OF PRODUCT_STATE_TYPE TABLE

   if (NewProducts == 0): print "NO NEW PRODUCTS IN HITSDB"
   else: 
     #ABOUT TO DO PRODUCT INSERT INTO PRODUCT AND PRODUCT_STATE TABLE

      for product in NewProducts:
         temp = (product[0],'',product[2])
         NewProduct.insertProduct(*temp)
      for product in NewProducts:
         col1 = NewProduct.getKeyBySerialNum(product[0]) #GETTING PRODUCT ID USING PRODUCT SERIAL NUMBER
         col2 = NewProduct.getKeyBySerialNum(product[1]) #GETTING PARENT PRODUCT ID FROM PARENT PRODUCT NUMBER
         print "here", (col1,col2)
         if col2 is None: col2 = ''
         col3 = NewStateType.get_one_key ('PRODUCT_STATE_TYPE_NAME','INSTALLED') #GETTING INSTALLED ID FROM PRODUCT STATE TYPE
         temp1 = (col1,col2,col3)
         NewProductState.insertProductState(*temp1)
      print "NEW PRODUCTS INSERTED"


def RemovedProducts(): 
   """
   This method calls the GetAllMissingProducts() to update product removed state to REMOVED
   """
   NewProduct = Product.Product() #OBJECT OF PRODUCT TABLE
   NewStateType = DomainClass.Domain('PRODUCT_STATE_TYPE') # OBJECT OF PRODUCT_STATE_TYPE TABLE
   NewProductState = Product_State.Product_State()

   RemovedProduct = GetAllMissingProducts() # RETURNS ALL REMOVED PRODUCTS
   if (len(RemovedProduct) == 0): print "NO REMOVED PRODUCTS"
   else:
      
      connection = DBconnection.databaseConnection()  # Connection to the database.
      cursor = connection.cursor()   
      query2 = "SELECT TO_CHAR(SYSDATE,'DD-MON-YYYY') FROM DUAL" 
      cursor.execute(query2)
      row = cursor.fetchone() 
      date1 = row[0]
      col3 = NewStateType.get_one_key ('PRODUCT_STATE_TYPE_NAME','REMOVED') #GETTING REMOVED ID FROM PRODUCT STATE TYPE
      fields=('PRODUCT_STATE_CHANGE_DATE','PRODUCT_STATE_TYPE_ID')
      for product in RemovedProduct:
         col2 = NewProduct.getKeyBySerialNum(product[1]) # GETTING PRODUCT ID FROM PRODUCT TABLE USING PRODUCT SERIAL NUMBER
         productStateId = NewProductState.getKeysByProduct(product[0] )
         value = (date1,col3)
         update = (fields,value)
         NewProductState.updateProductState(productStateId[0],*update)
      print "PRODUCTS REMOVED."   

