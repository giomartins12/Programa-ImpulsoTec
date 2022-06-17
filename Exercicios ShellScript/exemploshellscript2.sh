#!/bin/bash
contagem=0

echo "Até que número gostaria de contar?"
read numero

echo "Iniciando contagem"

while (( $contagem <= $numero ))
do
  echo "$contagem..."
     contagem=$((contagem+1))
     if (( contagem >= numero/2 ))
        then echo "Estou quase terminando!"
  fi
done
echo "... terminei!"

