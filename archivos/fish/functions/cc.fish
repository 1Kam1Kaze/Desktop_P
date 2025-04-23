#Ejecutador de c

function cc
    # Verifica si el directorio 'ejecutables' existe, si no, lo crea
    if not test -d "$PWD/ejecutables"
        mkdir "$PWD/ejecutables"
    end
    # Obtén el nombre del archivo sin la extensión '.c'
    set filename (basename $argv[1] .c)
    # Compila el archivo C y guarda el ejecutable en 'ejecutables'
    gcc $argv[1] -o "$PWD/ejecutables/$filename"
    # Da permisos de ejecución al archivo ejecutable
    chmod +x "$PWD/ejecutables/$filename"
    # Verifica si el archivo ejecutable tiene permisos de ejecución
    if test -x "$PWD/ejecutables/$filename"
        eval "$PWD/ejecutables/$filename"
    else
        echo "Error: El archivo ejecutable $filename no tiene permisos de ejecución"
    end
end
