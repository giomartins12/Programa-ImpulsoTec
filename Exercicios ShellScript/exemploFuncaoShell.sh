 #!/bin/bash

  # Exemplo1

 minhafuncao(){
	 echo $1
	 echo $2
         printf $3   
         echo $0
         echo $$ 
 }

minhafuncao "helo" "word" "1"

#############################################################################################

 # Exemplo2

 soma(){
      total=$(($1+$2))
      return $total
}

 read -p "Digite um numero inteiro: " int1
 read -p "Digite outro numero inteiro: " int2
 soma $int1 $int2
 echo "O resultado é: " $?

