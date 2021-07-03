<html>
    <head>
        <title>Iot 2 Home</title>
    </head>
    <body>
        <?php 
            echo "<p>Lendo dados de Velocidade da Internet</p>";
            echo "ID - Data / Hora - Equipamento - Download - Upload";
            echo "<br>";
 
            # Conexão MySQL com PHP 7
            $conexao = mysqli_connect('localhost','root','@cthum@1979','iot2b');
            mysqli_select_db($conexao,iot2b);
            mysqli_set_charset($conexao,'utf8');
 
            $sql = mysqli_query($conexao,"select * from airData") or die("Erro");
            
            while($dados=mysqli_fetch_assoc($sql))
                {   
                    echo $dados['id'].'<br>';
                }
            mysqli_close($conexao);
        ?>
    </body>
</html>