function cc-psword
    # Verifica si el directorio 'ejecutables' existe, si no, lo crea
    if not test -d "$PWD/ejecutables"
        mkdir -p "$PWD/ejecutables"
    end

    # Verifica si el archivo de entrada existe
    if not test -f $argv[1]
        echo "Error: El archivo $argv[1] no existe."
        return 1
    end

    # Obtén el nombre del archivo sin la extensión '.c'
    set filename (basename $argv[1] .c)

    # Compila el archivo C con OpenMP si está disponible
    set compile_command "gcc -o $PWD/ejecutables/$filename $argv[1] -Wall -O2"
    # Si OpenMP está habilitado, añade la bandera -fopenmp
    if type -q gcc
        set compile_command "$compile_command -fopenmp"
    end

    # Compila el archivo
    eval $compile_command

    # Verifica si la compilación fue exitosa
    if test -f "$PWD/ejecutables/$filename"
        # Da permisos de ejecución
        chmod +x "$PWD/ejecutables/$filename"
        # Ejecuta el archivo compilado
        echo "Ejecutando $filename..."
        eval "$PWD/ejecutables/$filename"
    else
        echo "Error: Fallo la compilación de $argv[1]."
        return 1
    end
end
