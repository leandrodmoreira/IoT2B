<html>
    <head>
        <title>Iot 2 Home</title>
    </head>
    <body>
        <?php 
            echo "<p>Lendo dados de Velocidade da Internet</p>";
            echo "ID - Data / Hora - Equipamento - Download - Upload";
            echo "<br>";

            $user = "root"; 
            $password = "@cthum@1979"; 
            $database = "iot2b"; 

            # O hostname deve ser sempre localhost 
            $hostname = "192.168.0.38";
 
            # Conexão MySQL com PHP 7
            $conexao = mysqli_connect($hostname,$user,$password);
            $banco = mysqli_select_db($conexao,$database);
            mysqli_set_charset($conexao,'utf8');
 
            $sql = mysqli_query($conexao,"select * from airData order by id desc") or die("Erro");
            
            while($dados=mysqli_fetch_assoc($sql))
                {   
                    echo $dados['id']'<br>';
                }
        ?>
    </body>
</html>