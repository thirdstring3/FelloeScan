<?php

  $display = "none";
  $file_name = 'config.txt';
  if(isset($_POST) && !empty($_POST)){
    $file = fopen( $file_name, 'w');
    // $headers = array();
    $body = array();
    foreach($_POST as $key=>$vals){
      fputcsv($file, array($key.":".$vals.", "));
      // $headers[] = $key;
      // $body[] = $vals;
    }
// echo "<pre<",print_r($body),"</pre>";die();
    // fputcsv($file, $headers);
    // fputcsv($file, $body);
    fclose($file);
    $display = "block";
    exit;
  }
  $rows = array_map('str_getcsv', file( $file_name)); // fetch current settings
  $csv = array();

  foreach($rows as $row){
    if(isset($row[0]) && !empty($row[0])){
      $parsed = explode(":", $row[0]);
      $csv[trim($parsed[0])] = trim($parsed[1]);
    }
  }


   // echo "<pre>",print_r($csv),"</pre>";die();
  

  // $header = array_shift($rows);
  // $csv = array();
  // foreach ($rows as $row) {
  //   $csv = array_combine($header, $row);
  // }
  print_r ($csv);  
  extract($csv);
?>

<!DOCTYPE html>
<html>
  <head>
    <title>Settings</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- Just to make this demo look nicer -->
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
    <link href="css/bootstrap.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="css/custom.css">
   
  </head>
  <body>
    <div class="container">
  
      <form method="POST" action="index.php">
 
        <h1>Settings Configuration</h1>
        <h3 style="display:<?=$display?>" class='success'>Successfully updated</h3>
        <fieldset>
          <legend><span class="number">1</span>Settings 1</legend>
            <input type="text" name="settings_1" value="<?= (isset($settings_1) ?  $settings_1 : '' ) ?>" required>
          <legend><span class="number">2</span>Settings 2</legend>
            <input type="text" name="settings_2" value="<?= (isset($settings_2) ?  $settings_2 : '' ) ?>" required>
          <legend><span class="number">3</span>Settings 3</legend>
            <input type="text" name="settings_3" value="<?= (isset($settings_3) ?  $settings_3 : '' ) ?>" required>
                      
        <!--NOTE: If you will add a new field the value and name attribute of html must be a variable with the same header in the csv ,
         if you will check the csv it has settings_1 , settings_2 and settings_3 header so if you will add a new setting for example "admin_settings" the new input must look like this
            <input type="text" name="admin_settings" value="<?= (isset($admin_settings) ?  $admin_settings : '' ) ?>" required>

           -->

           
        </fieldset>             

        <!--<button class="btn btn-primary" type="submit">Save</button> -->
      </form> 
    </div>
      
    <script src="js/jquery-1.12.0.min.js"></script>
    <script>
      $(document).ready(function(){
        $('input').on('keyup',function(){
            var data_array = $('form').serializeArray();
            console.log(data_array);
            $.post('index.php',data_array,function(resp){
              console.log(resp);

            })

        });

      })
    </script>
  </body>
</html>
