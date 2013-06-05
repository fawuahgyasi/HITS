#################################################################
# Name: Frederick Awuah-Gyasi
# Project: HITS
# Supervisor: Dr Tim Miller
# Version:1.0.0
# Module: HITSCLI
##################################################################


import sys

from optparse import OptionParser
import process

use = "Usage: %HITS [options] argument(s)"
parser = OptionParser (usage = use)

parser.add_option ('-o', '--output', dest = 'write', metavar ="FILE", help = "write output to FILE" )
parser.add_option ("-i", "--input" , dest = "read", metavar = "FILE", help = "read input from FILE " )
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")


options, args = parser.parse_args()

arguments = ('reconcile',       # Reconcile
             'addSupport',      # Add Support
             'addLocation',     # Add Location
             'addPartType',     # Add Part type
             'listCurActPP',    # List Current Active Parent Products
             'listPPWC',        # List current Parent Products and Components
             'listAllDiscrep',  # List all discrepancies
             'listDisposedPdt', # List Disposed Products
             'listReturnedPdt', # List Returned Products
             'listRemovedPdt',  # List Removed  Products
             'listLocation',    # List Locations
             'listSupport',     # List Support types
             'listReplaced',    # List Replaced Products
             'listNewPdt',      # List New Products
             'removeMissingPdt',# Remove Missing Products from HITS Database
             'installNewPdt'    # Install New Products. 

             )
def printCommands(): 
   """ prints commands """
   print "COMMANDS              DESCRIPTION"
   print "========              ==========="
   print "reconcile             Reconcile  "
   print "addSupport            Add Support"
   print "addLocation           Add Location"
   print "addPartType           Add Part type"
   print "listCurActPP          List Current Active Parent Products"
   print "listPPWC              List current Parent Products and Components"
   print "listAllDiscrep        List all discrepancies"
   print "listDisposedPdt       List Disposed Products"
   print "listReturnedPdt       List Returned Products"
   print "listRemovedPdt        List Removed  Products"
   print "listLocation          List Locations"
   print "listSupport           List Support types"
   print "listReplaced          List Replaced Products"
   print "listNewPdt            List New Products"
   print "removeMissingPdt      Remove All missing Products from HITS Database"
   print "installNewPdt         Install New Products"

def testargs(args): 
   """test arguments """
   for i in args:
      if i not in arguments:
         print "'{0}' command not recognized\n".format(i)
         parser.print_help()
         exit(-1)
def noargs():
   """ if no arguments """
   
def main(): 
   """ HITS COMMAND LINE INTERFACE"""
   testargs(args)
   #IF NO ARGUMENT IS GIVEN
   #-----------------------
   if len(args)==0:
      parser.print_help()
      printCommands()
      exit(-1)
   
   if options.write:
      sys.stdout = open(options.write, 'w')

   # RECOCILE 
   #---------
   if args[0] == 'reconcile' and not options.read:
      print "{0} requires an input file".format(args[0])
      parser.print_help()
      printCommands()
      exit(-1)
   if args[0] == 'reconcile' and options.read:
      if(process.InsertDataInventoryTBL(options.read)== 1):
         print "reconcile done!!!"
      exit(-1)

   # DISPLAY ALL DISCREPANCIES: Display is to stdout. 
   #------------------------------------------------ 
   if args [0] == 'listAllDiscrep':

      process.DisplayDescrepancyWithState()
      exit(-1)

   # GET ALL DISCREPANCIES: Output to a file. 
   #-----------------------------------------
   if (args [0] == 'listAllDiscrep' and (option.write or option.versbose)):
      process.GetAllDiscrepancies()

   # DISPLAY ALL CURRENT ACTIVE PRODUCTS: Display to stdout: 
   #-------------------------------------------------------

   if args [0] == 'listCurActPP':
      process.DisplayAllCurrentActiveProducts()
      exit(-1)

   # GET ALL CURRENT ACTIVE PRODUCTS : OUTPUT TO A FILE
   #---------------------------------------------------
   if (args [0] == 'listCurActPP' and (option.write or option.versbose)):
      process.GetAllCurrentActiveProducts()

   # DISPLAY PARENT PRODUCTS WITH COMPONENTS: DISPLAY TO STDOUT
   #-----------------------------------------------------------

   if args [0] == 'listPPWC':
      process.DisplayParentProductWithComponents()
      exit(-1)

   # GET ALL PARENT PRODUCTS WITH COMPONENTS: OUTPUT TO A FILE
   #----------------------------------------------------------
   if (args [0] == 'listPPWC' and (option.write or option.versbose)):
      process.GetParentProductWithComponents()
      exit(-1)

   # DISPLAY ALL SUPPORT
   #--------------------

   if args [0] == 'listSupport':
      process.DisplaySupportType()
      exit (-1)

   # DISPLAY ALL LOCATIONS
   #----------------------
   if args[0] == 'listLocation':
      process.DisplayAllLocation()
      exit(-1)



   # DISPLAY ALL DISPOSED PRODUCTS
   #------------------------------

   if args[0] == 'listDisposedPdt':
      process.DisplayAllDisposedProducts()
      exit (-1)

   # DISPLAY ALL RETURNED PRODUCTS
   #------------------------------
   if args[0] == 'listReturnedPdt':
      process.DisplayAllReturnedProducts()
      exit (-1)


   # DISPLAY ALL REMOVED PRODUCTS
   #-----------------------------

   if args[0] == 'listRemovedPdt':
      process.DisplayAllMissingProducts()
      exit (-1)

   # DISPLAY ALL RELOCATED PRODUCTS
   #-------------------------------

   if args[0] == 'listRelocatedPdt':
      process.DisplayAllRelocatedProducts()
      exit(-1)

   # DISPLAY ALL REPLACED PRODUCTS
   #------------------------------   
   if args [0] == 'listReplacedPdt':
      process.DisplayAllReplacedProducts()
      exit (-1)

   # DISPLAY ALL NEW PRODUCTS
   #-------------------------

   if args[0] == 'listNewPdt':
      process.DisplayAllNewProducts()
      exit(-1)

   # INSTALL NEW PRODUCTS
   #---------------------
   if args[0] == 'installNewPdt':
      responds = raw_input ("Do you want to install all newly discoved products after the RECONCILE? (y/n)? ")
      if responds not in ('y','n','N','Y','NO','YES','no','yes'):
         responds = raw_input ("Enter y/n")
      if responds in ('y','Y','YES','yes','Yes'):
         process.InstallNewProduct()
         exit (-1)
      if responds in ('n','N','NO','no','No'):
         exit(-1)


   # REMOVE MISSING PRODUCTS
   #------------------------
   if args[0] == 'removeMissingPdt':
      responds = raw_input ("Do you want to remove all missing products after the RECONCILE? (y/n)? ")
      if responds not in ('y','n','N','Y','NO','YES','no','yes'):
         responds = raw_input ("Enter y/n")
      if responds in ('y','Y','YES','yes','Yes'):
         process.RemovedProducts()
         exit (-1)
      if responds in ('n','N','NO','no','No'):
         exit(-1)

if __name__ == '__main__':
    main()                   

