<html>
<head>
    <title>Kevin Gamez:TOP.100.NYSE</title>
    <style>
    	table
    	{
    		font-family:sans;
    	}
    	td,th
    	{
    		text-align:center;
    		border:1px solid #ddd;
    		padding:.5em;
    	}
		tr:nth-child(even)
		{
			background-color:#ddd;
		}
    </style>
</head>
<body>
	<!--
		path: /var/www/html/
	-->
	<table align="center" border="1">
		<tr>
			<th>Exchange</th>
			<th>Symbol</th>
			<th>Company</th>
			<th>Volume</th>
			<th>Price</th>
			<th>Price Difference</th>
		</tr>
		<?php
			//using sqli
			//$cnx = new mysqli('localhost', 'username', 'pass', 'db');
		
			
			//using postgreSQL
			$cnx= pg_connect("host=localhost dbname= user= password=")
			or die('Could Not Connect: ' . cnx_last_error());
			
			$query = 'SELECT * FROM data';
			#$cursor = $cnx->query($query);
			$res = pg_query($query) or die('Query failed: '. preg_last_error());

			while ($row = pg_fetch_assoc($res)) 
			{
				echo '<tr style="text-align:center">';
				echo '<td>' . $row['exchange'] . '</td><td>' . $row['symbol'] . '</td><td align="right">' . $row['company'] .'</td><td>' . $row['volume'] . '</td><td>' . $row['price'] . '</td><td>' . $row['diff'] . '</td>';
				echo '</tr>';
			}
			#$cnx->close();
			pg_close($cnx);
		?>
	</table>
</body>
</html>
