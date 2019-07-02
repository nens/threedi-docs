Schematisation Checker
======================

The schematization checker analyses your 3Di model database (.sqlite file) for completeness and consistency between tables. With the checker you can make sure most model errors are caught before sending the model to the INP server for model generation. 


Usage
^^^^^

1. Start *QGIS*
2. Add a connection to the model database (*Layer* -> *Data Source Manager*, Select *SpatiaLite* on the left and create a *'New’* connection or connect to an existing connection)
3. Open the schematization checker by opening the *Toolbox* in the 3Di Plugin, select *Step 1: check data*, select *schematisation_checker.py*
4. Select the SpatiaLite connection of the model database and the location where to store the output of the schematisation checker. Click *run* to run the schematisation checker. Click *open* to open the output.