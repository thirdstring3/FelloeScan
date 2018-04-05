<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Motor Control</title>
</head>
        <body>
        Rotate Control:
        <form method="get" action="scan.php">
                <input type="submit" value="Enable" name="m_enable">
                <input type="submit" value="Disable" name="m_disable">
		<input type="submit" value="Rotate" name="m_rotate">
        </form>
        <?php
        $setmode17 = shell_exec("gpio mode 11 out");
	$theta = 30;
	$m_stepsPerRevolution = 3200;
	$numSteps = ($theta / 360) * $m_stepsPerRevolution;
        if(isset($_GET['m_enable'])){
                $gpio_on = shell_exec("gpio write 11 1");
		echo "Motor is $check";
		echo $numSteps;
        }
        else if(isset($_GET['m_disable'])){
                $gpio_off = shell_exec("gpio write 11 0");
                echo "Motor is off";
        }
	else if(isset($_GET['m_rotate'])){
		$gpio_rotate = shell_exec("gpio -g write 7 1");
		echo "Rotating";
	}
        ?>
        </body>
</html>
