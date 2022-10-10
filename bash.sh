echo Write 1 integer
read int1

echo Write 2 integer
read int2

echo -e

for mun in `seq $int1 $int2`
do
    ret=$(factor $mun | grep $mun | cut -d ":" -f 2 | cut -d " " -f 2)

    
    if [ "$ret" -eq "$mun" ] 
    then
        
        if [ "$flag" = true ]
        then 
            flag=false
        else
            echo "$mun"
            flag=true
        fi
        ((count++))
    fi 
done
