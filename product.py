##################################################################
# Name: Frederick Awuah-Gyasi
# Project: HITS
# Supervisor: Dr Tim Miller
# Version:1.0.0
# Class: Product
##################################################################

import cx_Oracle
import DBconnection

class Product:
   """
   The class for the Product table 
   
   Columns: 
   
          1.PRODUCT_ID
          2.PRODUCT_SERIAL_NUM
          3.SUPPORT_ID
          4.PART_ID


        Actions
        getKeyBySerialNum
        getKeysByStateType====> Find this function under the Product_state table
        getKeysBySupportLevel
        getKeysBySupportRefNum
        getKeysByPO
        insertProduct
            Arguments
                [string] identity label (optional)
                [string] serial number
                [string] part number
                [string] support information (refnum)

   """

   def __init__(self):
       """
       The initialization of the class with connection, table name and column names 
       """
       self.tabblename='PRODUCT'
       self.colname = ('PRODUCT_ID','PRODUCT_SERIAL_NUM','SUPPORT_ID','PART_ID')
       self.connection= DBconnection.databaseConnection()



   def getKeyBySerialNum(self,serial_num):
       """
       To get the product Id giving the product id of the product 
       Arguement: [string] Product_serial number
       Returns: Product_id
       """
      
       #cursor
       cursor= self.connection.cursor()
      
       #query
       query= "SELECT {0} FROM PRODUCT WHERE {1} = '{2}'".format(self.colname[0],self.colname[1],serial_num)
   
       try: 
          cursor.execute(query)
          row = cursor.fetchone()
          return row[0]
       except: 
          pass
       finally: 
          cursor.close()
  
   
   def getKeysBySupportLevel(self,supportLevel):
       """
       Get the keys of products with a given support level
       Argument: [string]  supportLevel
       Returns: Keys of products witht the given support level
       """
       # cursor
       cursor= self.connection.cursor()
       
       #Query
       query ="SELECT PRODUCT_ID FROM PRODUCT WHERE SUPPORT_ID IN (SELECT SUPPORT_ID FROM SUPPORT WHERE SUPPORT_LEVEL_ID IN (SELECT SUPPORT_LEVEL_ID FROM SUPPORT_LEVEL WHERE SUPPORT_LEVEL_NAME ='{0}'))".format(supportLevel)

       try: 
          cursor.execute(query)
          rows=cursor.fetchall()
          return rows
       except: 
          pass
       finally: 
          cursor.close()

   def getKeysBySupportRefNum(self,supportRefNum):
       """
       To get the Product Id from the Product using the support reference number: 
       Argument: string support refNum
       returns : tuple of keys with the provided support ref
   
       """
       #Cursor
       cursor=self.connection.cursor()
       #Query
       query= "SELECT PRODUCT_ID FROM PRODUCT WHERE SUPPORT_ID IN (SELECT SUPPORT_ID FROM SUPPORT WHERE SUPPORT_REF_NUM = '{0}')".format(supportRefNum)

       try: 

          cursor.execute(query)
          rows=cursor.fetchall()
          return rows
       except:
          pass
       finally:
          cursor.close()
   
   def getKeysByPO(self,po_num):
       """ 
       THis is to track product assosciated with a particular purchase order: 
       Arguement: string PurchaseOrder Number
       Returns the Pord
       """

       #cursor
       cursor=self.connection.cursor()
       
       #query
       query="SELECT PRODUCT_ID FROM PRODUCT WHERE PART_ID IN (SELECT PART_ID FROM PART FROM WHERE PART_ID IN (SELECT PART_ID FROM UNIT WHERE UNIT_ID IN (SELECT UNIT_ID FROM QUOTE1_UNIT WHERE QUOTE1_ID IN (SELECT QUOTE1_ID FROM QUOTE1 WHERE QUOTE1_ID IN (SELECT QUOTE1_ID FROM PURCHASE_ORDER WHERE PO_NUM = '{0}')))))".format(po_num)

       try:
          cursor.execute(query)
          rows = cursor.fetchall()
          return rows
       except:
          pass
       finally:
          cursor.close()
 
  
  
 
 
   def insertProduct(self,*insert):

       """
       Arguemnt: [Tuple ] insert (product_serial_num,support_ref_num,part_num)
       Returns : Product_id

       """
  
       #Cursor
       cursor=self.connection.cursor()
       cursor1=self.connection.cursor()
       cursor2=self.connection.cursor()
       cursor3=self.connection.cursor()

       #Query
       query1="SELECT TRANSACTION_PK_SEQUENCE.NEXTVAL FROM DUAL"
       query2="SELECT PART_ID FROM PART WHERE PART_NUM = '{0}'".format(insert[2])
       query3="SELECT SUPPORT_ID FROM SUPPORT WHERE SUPPORT_REF_NUM ='{0}'".format(insert[1])
       
       #ProductId
       cursor1.execute(query1)
       key=cursor1.fetchone()
       Product_id=key[0]
       #PartId
       cursor2.execute(query2)
       key1 = cursor2.fetchone()
       Part_id=key1[0]
       #SupportID
       #cursor3.execute(query3)
       #key2 = cursor3.fetchone()
       #print "Key2", key2
       
       #Support_id=key2[0]
       Support_id=''
       tempinsert=list(insert)
       tempinsert[1]=Support_id
       tempinsert[2]=Part_id
       tempinsert.insert(0,Product_id)
       
       actualInsert=tuple(tempinsert)
       
       query="INSERT INTO PRODUCT ({0}) VALUES {1} ".format(','.join(map(str,self.colname)),actualInsert)
       print query
       try:
          cursor.execute(query)
          self.connection.commit()

       except cx_Oracle.IntegrityError,exception:
          error,=exception
          print "Oracle error message :" ,error.message
      
       finally:
          cursor.close()
          cursor1.close()
          cursor2.close()
          cursor3.close()

 
def testProduct():
    """
    A test for the Product Class
        Methods: 
        1.getKeyBySerialNum
        2.getKeysByStateType====> Find this function under the Product_state table
        3.getKeysBySupportLevel
        4.getKeysBySupportRefNum
        5.getKeysByPO
        6.insertProduct
    """
    NewProduct= Product()
    
    Data1=(('Product1','SUPREF2','Partnum1'),('Product2','SUPREF3','Partnum2'),('Product3','SUPREF4','PartNum3'),('Product4','SUPREF5','Partnum2'),('Product5','SUPREF2','Partnum1'))


    for data in Data1:
       NewProduct.insertProduct(*data)
    print "Inserts done!!"

    key1=NewProduct.getKeyBySerialNum('Product1')
    print "SerialNum: Product1 has key , " , key1

    key2= NewProduct.getKeysBySupportLevel('9x5xNBD')
    print "Products with 9X5xNBD are : ", key2

    key3= NewProduct.getKeysBySupportRefNum('SUPREF2')
    print "Products with Supportref2 are : ", key3

    key4=NewProduct.getKeysByPO('P0007244')
    print "Product purchased by P0007244 are : ", key4

if __name__=="__main__" :testProduct()

