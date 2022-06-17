#!/bin/bash
echo $BASH # Contém o caminho completo dointerpretador de comandos para scripts Bash
echo $BASH_VERSION # Contém a versão de lançamento do bash da máquina usada atualmente
echo $HOME # Contém o caminho relativo do diretórioinicial
echo $LOGNAME # Contém o nome da conta do usuário atual conectado 
echo $OSTYPE # Contém uma string que descreve o sistema operacional da máquina usada
echo $PATH # Contém um caminho absoluto separado por dois pontos dos arquivos executáveis no linux
echo $PWD # Mantém o diretório de trabalho atual do shell
echo $SHELL # Funciona de forma semelhante ao LOGNAME. Ele contém o nome da conta do usuário atualmenteconectado
echo $_ # Contém o nome do comando usado recentemente no shell
# comando "env" mostar todas as variaveis de ambiente
#####################################################################################################################

# Exemplo1:

echo "Primeiro nome: "
read nome
read -p "Sobrenome: " sobrenome
echo " olá $nome $sobrenome ! Eu estou aprendendo a criar shell scripts!"

#####################################################################################################################

# Exemplo2

read -p "Informe o primeiro numero:" a
read -p "Informe o segundo numero:" b
echo $((a+b))
c=$a+$b # Concatenação de scripts.Não é operação aritimética
echo $c

####################################################################################################################

# Exemplo3

 ls # Lista o diretorio atual
 if [ -e arquivo_descomplicado.sh ]
 then
    echo "O arquvo descomplicado existe!"
 else
    echo "O arquivo descomplicado não existe!"
 fi    

####################################################################################################################

#Exemplo4

 read -p "Primeira string: " str1
 read -p "Segunda string: " str2
 if [ -z "$str1" ]
 then
    echo "A primeira string é nula"
 elif [ -z "$str2" ]
 then 
    echo "A segunda string é nula"
 else
    if [ $str1 == $str2 ] 
    then
       echo "As strings são iguais!" 
    else
       echo "As strings não são iguais"
    fi
 fi

######################################################################################################################

#Exemplo5

 read -p "Digite um número: " int1
 if [ $int1 -eq 0 ] # (( $int1 == 0 ))
 then
    echo "numero zero"
elif [ $int1 -lt 0 ] # (( $int1 < 0 ))
 then
    echo "numero negativo"
 else
	 if [ $((int1%2)) -eq 0 ] # (( $((int1%2)) == 0 ))
    then
       echo "numero par"
    else
       echo "numero impar"
   fi
 fi

#######################################################################################################################

# Exemplo5

 echo "Fala comigo!"
 echo 
 read fala
 case $fala in
   "Bom dia!")
   	echo "Bom dia!"
        ;;
   "Boa tarde!")
        echo "Boa tarde"
        ;;
   "Boa noite!")
        echo "Boa noite"
        ;;
   *)
        echo "desculpa não entendi!"
        ;;
 esac
 echo
 echo " Por hj é só pessoal!" 

##########################################################################################################################

# Exemplo6

 resultado=0;
 entrada=0;
 for var in 1 2 3 4 5 6 7 8 9 10
 do
     printf "Entre com um número inteiro %d : " $var
     read entrada
     resultado=$((resultado+entrada))
 done
 echo "A soma é " $resultado 

 ##########################################################################################################################

 # Exemplo7

 lista="diretorio1 diretorio2 diretorio3 diretorio4"
 var=""
 mkdir descomplica
 cd descomplica
 echo "Criando diretórios..."
 for var in $lista
 do
     mkdir $var
 done     
 cd descomplica | ls | sort

########################################################################################################################## 
 
# Exemplo8 

 diretorios=$(cat lista) # especifcando o arquivo ou atribuir o valor a variavel lista
 echo "Criando diretórios...."
 for var in $diretorios
 do
     mkdir $var 
 done

#########################################################################################################################
 
 # Exemplo9

  resultado=0
  entrada=0
  for((var=1;var<=5;var++))
  do
    printf "Entre com um valor inteiro %d : " $var
    read entrada
    result=$((resultado+entrada))    
  done  
  echo $resultado

##########################################################################################################################
 
 # Exemplo10

 entrada=0
 resultado=0
 var=1
 while ((var <= 5)) # [ $var -le 5 ]
 do
   printf "Entre com um valor inteiro %d : " $var
   read entrada
   result=$((resultado+entrada))
 done     
 echo "Resultado: " $resultado

###########################################################################################################################

 # Exemplo11

 # Until ( oposto do comando while) 

############################################################################################################################
 
 # Exemplo12 




