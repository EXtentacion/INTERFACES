

promeio() {
    long=$#
    sum=0

    for x in "$@"
    do
        sum=$((sum + x))
    done

    prom=$(bc -l <<< "$sum / $long")

    resultado=$prom
}

# Llamar a la función para calcular el promedio
promeio 1 2 3 4 5 6 7 8 9 10

echo "El promedio es: $resultado"





promeio() {
    long=$#
    sum=0

    for x in "$@"
    do
        sum=$((sum + x))
    done

    prom=$(bc -l <<< "$sum / $long")

    resultado=$prom
}

# Llamar a la función para calcular el promedio
promeio 1 2 3 4 5 6 7 8 9 10

echo "El promedio es: $resultado"



promeio() {
    long=$#
    sum=0

    for x in "$@"
    do
        sum=$((sum + x))
    done

    prom=$(bc -l <<< "$sum / $long")

    echo $prom
}

# Capturar el resultado del promedio en la variable directamente al llamar a la función
resultado=$(promeio 1 2 3 4 5 6 7 8 9 10)

echo "El promedio es: $resultado"



promeio() {
    long=$#
    sum=0

    for x in "$@"
    do
        sum=$((sum + x))
    done

    prom=$(bc -l <<< "$sum / $long")

    echo $prom
}

# Capturar el resultado del promedio en la variable directamente al llamar a la función
resultado=$(promeio 1 2 3 4 5 6 7 8 9 10)

echo "El promedio es: $resultado"

promeio() {
    long=$#
    sum=0

    for x in "$@"
    do
        sum=$((sum + x))
    done

    prom=$(bc -l <<< "$sum/$long")

    echo $prom
}

# Capturar el resultado del promedio en la variable directamente al llamar a la función
resultado=$(promeio 1 2 3 4 5 6 7 8 9 10)

echo "El promedio es: $resultado"


