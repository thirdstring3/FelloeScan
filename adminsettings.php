//This page allows administrator settings to be edited

<?php 
#Load settings file into array
$adminset = csv_to_array(adminsettings.txt)
echo $adminset

#Prefill form with settings

#Autosave to settings file

#Close file on exit
fclose($myfile);

?>
