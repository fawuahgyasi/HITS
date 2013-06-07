HITS
====

Final Masters Project

1  Introduction: 

Technology drives every educational institution and Wake Forest University, using state of the art technology, is of no exception. The Networking and High Performance Computing (HPC) teams in the Wake Forest Information Systems department (IS) are responsible for the reliability and accessibility of the components on which Wake Forest's technology operates.  The HPC team manages the clusters which support research from the Reynolda and Bowman Gray Medical School . The Reynolda network is managed by the Networking team at IS. These components number on the order of ten thousand.

To curb the difficulty in efficiently managing and tracking these overwhelming number of technology components, the teams require a robust application that is secure and efficient. The data entry process should also be easy and efficient.

2  Project Description:

The goal of the Hardware Inventory Tracking System (HITS) project is to develop a system, HITS, to assist the HPC and Networking teams in maintaining an accurate inventory of the hardware components used at Wake Forest. This system will contain enough functionality to accurately determine: 

(a) Where and when hardware was installed or removed,
(b) Support information, such as response time, start and end dates for support, and support contract information for a given piece of hardware,
(c) Tracking what components have been returned and their replacement, as well as those removed and disposed
(d) When inventory is nearing the end of its lifetime or its lease term.

This HITS project will provide the foundation for future essential functionality needed for increasing operational efficiencies.  In order to provide a robust framework, we must consider future functionality that we are already considering integrating with the HITS system in future projects. Known capabilities on the product road map are:
Automated service configuration - by expanding the database schema to include tables that identify systems as belonging to specific services, scripts will be generated to automatically populate service configuration files (DNS and DHCP, for example).
Configuration Management planning tools - determining what components are dependent on others, both at a hardware level and a service level.
Automated auditing of HITS contents - use external scripting to dynamically determine hardware information via SNMP and compare with contents of the database. This process defines what will be later referred to in this document as the reconcile process. 

3  Design recommendations:
Currently, the desired method of interaction with the HITS project is via command line tools.  Careful thought should be given to the design so that an easy HTML presentation overlay (via CGI) can be developed to re-utilize as much code infrastructure as possible.

HITS is a database application that will be powered by the Python scripting language and an Oracle database back end. The choice of technologies was driven by the skill set present within the Information Systems department as well as the learning objectives for this project.  Oracle is the de facto database standard for IS making it readily available for use by HPC. HITS will benefit from IS’s Oracle expects.

Related to the learning objectives and duration of this project, the programming language chosen had to be easy to learn, provide robust integration of documentation, and lend itself to code maintainability and extension.This language had to be powerful and versatile so as to fully cover the needs or scope of this project. Python as an open source, object oriented, high-level, general purpose interpreted language meets all these requirements of the programming language needed for HITS. 

This project is estimated to be up and running before the end of Spring 2013. The software development methodology adopted for the development of HITS is the Waterfall Model.

# NOT ALL FILES IN THIS PROJECT ARE PERMITTED IN GITHUB AND IDEA OF THE OTHER FILES CAN BE GOT FROM THE IMPORTED FILES WHICH WERE ALL CODED FROM SCRATCH.
