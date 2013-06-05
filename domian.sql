/******************************************************************************
 * NAME:     SIZE1
 *
 * PURPOSE:  This script provides DDL for the SIZE table. SIZE1 table
 *           is a domain table with all the possible size values of a product.
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 
 
 CREATE TABLE SIZE1 (
 SIZE1_ID NUMBER NOT NULL,
 SIZE1_WIDTH NUMBER(3) NOT NULL,
 SIZE1_HEIGHT NUMBER(3) NOT NULL,
 SIZE1_DEPTH NUMBER(3) NOT NULL,
 SIZE1_RU NUMBER(2) NOT NULL
 );
 
 COMMENT ON COLUMN SIZE1.SIZE1_RU IS 'RU: RACK UNITS';
 
 CREATE UNIQUE INDEX PK_SIZE1 ON SIZE1 (SIZE1_ID);
 
 ALTER TABLE SIZE1 ADD (CONSTRAINT PK_SIZE1 PRIMARY KEY (SIZE1_ID) USING INDEX PK_SIZE1);
 ALTER TABLE SIZE1 ADD (CONSTRAINT UNIQUE_SIZE1 UNIQUE (SIZE1_WIDTH,SIZE1_HEIGHT,SIZE1_DEPTH,SIZE1_RU));
 
 
 /******************************************************************************
 * NAME:     PART_TYPE
 *
 * PURPOSE:  This script provides DDL for the PART_TYPE table. This table
 *           is a domain table with all the possible TYPES of a product.
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 
CREATE TABLE PART_TYPE(
PART_TYPE_ID NUMBER NOT NULL,
PART_TYPE_NAME VARCHAR2(20) NOT NULL
);

COMMENT ON COLUMN PART_TYPE.PART_TYPE_NAME IS 'NAME: THE NAME OF THE PART';

CREATE UNIQUE INDEX PK_PART_TYPE ON PART_TYPE (PART_TYPE_ID);  

ALTER TABLE PART_TYPE ADD (CONSTRAINT PK_PART_TYPE PRIMARY KEY (PART_TYPE_ID) USING INDEX PK_PART_TYPE);

ALTER TABLE PART_TYPE ADD (CONSTRAINT UNIQUE_PART_TYPE UNIQUE (PART_TYPE_NAME));



/******************************************************************************
 * NAME:     POWER1
 *
 * PURPOSE:  This script provides DDL for the POWER1 table. This table
 *           is a domain table with all the possible power specifications of a product.
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 

CREATE TABLE POWER1(
POWER1_ID NUMBER NOT NULL,
POWER1_OUTPUT_WATTS NUMBER(5) NOT NULL,
POWER1_INPUT_VOLTAGE NUMBER(5) NOT NULL,
POWER1_INPUT_CURRENT NUMBER(5) NOT NULL,
POWER1_CONNECTOR VARCHAR2(30) NOT NULL
);

COMMENT ON COLUMN POWER1.POWER1_CONNECTOR IS 'CONNECTOR: THE TYPE OF POWER CONNECTOR ';

CREATE UNIQUE INDEX PK_POWER1 ON POWER1 (POWER1_ID);

ALTER TABLE POWER1 ADD (CONSTRAINT PK_POWER1 PRIMARY KEY (POWER1_ID) USING INDEX PK_POWER1);

ALTER TABLE POWER1 ADD (CONSTRAINT UNIQUE_POWER1 UNIQUE (POWER1_OUTPUT_WATTS,POWER1_INPUT_VOLTAGE,POWER1_INPUT_CURRENT,POWER1_CONNECTOR));

/******************************************************************************
 * NAME:     SUPPORT_LEVEL
 *
 * PURPOSE:  This script provides DDL for the SUPPORT_LEVEL table. THIS table
 *           is a domain table with all the possible support levels for a product.
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 CREATE TABLE SUPPORT_LEVEL(
 SUPPORT_LEVEL_ID NUMBER NOT NULL,
 SUPPORT_LEVEL_NAME VARCHAR2(30) NOT NULL
 );
 
 
 CREATE UNIQUE INDEX PK_SUPPORT_LEVEL ON SUPPORT_LEVEL(SUPPORT_LEVEL_ID);
 
 ALTER TABLE SUPPORT_LEVEL ADD (CONSTRAINT PK_SUPPORT_LEVEL PRIMARY KEY (SUPPORT_LEVEL_ID) USING INDEX PK_SUPPORT_LEVEL);
 
 ALTER TABLE SUPPORT_LEVEL ADD (CONSTRAINT UNIQUE_SUPPORT_LEVEL_NAME UNIQUE (SUPPORT_LEVEL_NAME));
 
 /******************************************************************************
 * NAME:     PURCHASE_TYPE
 *
 * PURPOSE:  This script provides DDL for the PURCHASE_TYPE table. This table
 *           is a domain table with all the possible type of puchases of a purchase order.
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 
 
CREATE TABLE PURCHASE_TYPE(
PURCHASE_TYPE_ID NUMBER NOT NULL,
PURCHASE_TYPE_NAME VARCHAR2(20) NOT NULL
);


COMMENT ON COLUMN PURCHASE_TYPE.PURCHASE_TYPE IS 'PURHCASE_TYPE : COULD BE A BUY OR A LEASE';

CREATE UNIQUE INDEX PK_PURCHASE_TYPE ON PURCHASE_TYPE(PURCHASE_TYPE_ID);

ALTER TABLE PURCHASE_TYPE ADD (CONSTRAINT PK_PURCHASE_TYPE PRIMARY KEY (PURCHASE_TYPE_ID) USING INDEX PK_PURCHASE_TYPE);

ALTER TABLE PURCHASE_TYPE ADD (CONSTRAINT UNIQUE_PURCHASE_TYPE_NAME UNIQUE (PURCHASE_TYPE_NAME) );

/******************************************************************************
 * NAME:     LEASE_TYPE
 *
 * PURPOSE:  This script provides DDL for the LEASE_TYPE table. This table
 *           is a domain table with all the possible LEASE TYPES OF PURCHASE ORDER .
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 

CREATE TABLE LEASE_TYPE(
LEASE_TYPE_ID NUMBER NOT NULL,
LEASE_TYPE_NAME VARCHAR2(30) NOT NULL
);

COMMENT ON COLUMN LEASE_TYPE.LEASE_TYPE IS 'TYPE: FML/DBO';

CREATE UNIQUE INDEX PK_LEASE_TYPE ON LEASE_TYPE(LEASE_TYPE_ID);

ALTER TABLE LEASE_TYPE ADD (CONSTRAINT PK_LEASE_TYPE PRIMARY KEY (LEASE_TYPE_ID) USING INDEX PK_LEASE_TYPE);

ALTER TABLE LEASE_TYPE ADD (CONSTRAINT UNIQUE_LEASE_TYPE_NAME UNIQUE(LEASE_TYPE_NAME));




/******************************************************************************
 * NAME:     PRODUCT_STATE_TYPE
 *
 * PURPOSE:  This script provides DDL for the PRODUCT_STATE_TYPE table. PRODUCT_STATE_TYPE table
 *           is a domain table with all the possible STATES TYPES a product.
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 
CREATE TABLE PRODUCT_STATE_TYPE(
PRODUCT_STATE_TYPE_ID NUMBER NOT NULL,
PRODUCT_STATE_TYPE VARCHAR2(20) NOT NULL
);

COMMENT ON COLUMN PRODUCT_STATE_TYPE.PRODUCT_STATE_TYPE IS 'TYPES: RETURNED,INSTALLED,DISPOSED,REPLACED,REMOVED';

CREATE UNIQUE INDEX PK_PRODUCT_STATE_TYPE ON PRODUCT_STATE_TYPE(PRODUCT_STATE_TYPE_ID);

ALTER TABLE PRODUCT_STATE_TYPE ADD (CONSTRAINT PK_PRODUCT_STATE_TYPE PRIMARY KEY (PRODUCT_STATE_TYPE_ID) USING INDEX PK_PRODUCT_STATE_TYPE);

ALTER TABLE PRODUCT_STATE_TYPE ADD (CONSTRAINT UNIQUE_PRODUCT_STATE_TYPE UNIQUE (PRODUCT_STATE_TYPE) );



/******************************************************************************
 * NAME:     LOCATION
 *
 * PURPOSE:  This script provides DDL for the LOCATION table. LOCATION table
 *           is a domain table with all the possible PHYSICAL LOCATIONS a product.
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/

CREATE TABLE LOCATION(
LOCATION_ID NUMBER NOT NULL,
LOCATION_DESCRIPTION VARCHAR2(30) NOT NULL
);


CREATE UNIQUE INDEX PK_LOCATION ON LOCATION(LOCATION_ID);

ALTER TABLE LOCATION ADD ( CONSTRAINT PK_LOCATION PRIMARY KEY (LOCATION_ID) USING INDEX PK_LOCATION);

ALTER TABLE LOCATION ADD (CONSTRAINT UNIQUE_LOCATION UNIQUE(LOCATION_DESCRIPTION));



/******************************************************************************
 * NAME:     QUOTE1
 *
 * PURPOSE:  This script provides DDL for the QUOTE table. QOUTE table
 *           is a  table with all the possible QUOTE info. .
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       06/19/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 CREATE TABLE QUOTE1(
 QUOTE1_ID NUMBER NOT NULL,
 QUOTE1_NUM VARCHAR2(30 CHAR),
 QUOTE1_DATE DATE NOT NULL,
 QUOTE1_TOTAL_SHIPPING_PRICE NUMBER(13,2) NOT NULL
 );
 
 CREATE UNIQUE INDEX PK_QUOTE1 ON QUOTE1(QUOTE1_ID);
 
 ALTER TABLE QUOTE1 ADD ( CONSTRAINT PK_QUOTE1 PRIMARY KEY (QUOTE1_ID) USING INDEX PK_QUOTE1);
 
 ALTER TABLE QUOTE1 ADD (CONSTRAINT UNIQUE_QUOTE1 UNIQUE (QUOTE1_NUM,QUOTE1_DATE,QUOTE1_TOTAL_SHIPPING_PRICE));




/******************************************************************************
 * NAME:     DOMAIN_PK_SEQUENCE
 *
 * PURPOSE:  This script provides DDL for the SEQUENCE table. THIS table
 *           is a  table FOR GENERATING PRIMARY KEYS FOR ALL DOMAIN TABLES 
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       07/11/2012  Frederick Awuah-Gyasi  SEQUENCE Creation
 *
 *****************************************************************************/

CREATE SEQUENCE DOMAIN_PK_SEQUENCE
  START WITH 1
  MAXVALUE 9999999999
  MINVALUE 1
  NOCYCLE
  CACHE 10
;


/******************************************************************************
 * NAME:     DOMIAN_TEST
 *
 * PURPOSE:  THIS TEST TABLE IS TO CHECK IF ALL METHOD IN THE DOMAINCLASS.PY WORK
 *           EXCEPT THE NAME ITS JUST LIKE THE QUOTE1 TABLE
 *
 * MODIFICATION HISTORY:
 * Version    Date       Author                 Description
 * -------------------------------------------------------------------------
 * 1.0       07/20/2012  Frederick Awuah-Gyasi  Initial Creation
 *
 *****************************************************************************/
 CREATE TABLE DOMAIN_TEST(
 DOMAIN_TEST_ID NUMBER NOT NULL,
 DOMAIN_TEST_NUM VARCHAR2(30 CHAR),
 DOMAIN_TEST_DATE DATE NOT NULL,
 DOMAIN_TEST_PRICE NUMBER(13,2) NOT NULL
 );
 
 CREATE UNIQUE INDEX PK_DOMAIN_TEST ON DOMAIN_TEST(DOMAIN_TEST_ID);
 
 ALTER TABLE DOMAIN_TEST ADD ( CONSTRAINT PK_DOMAIN_TEST PRIMARY KEY (DOMAIN_TEST_ID) USING INDEX PK_DOMAIN_TEST);
 
 ALTER TABLE DOMAIN_TEST ADD (CONSTRAINT UNIQUE_DOMAIN_TEST UNIQUE (DOMAIN_TEST_NUM,DOMAIN_TEST_DATE,DOMAIN_TEST_PRICE));







 