#!/bin/bash

JSON=`cat config.json`

KEYS=$(echo $JSON | jq -r 'keys[] as $k | "\($k)=\(.[$k])"')
i=0
for e in ${KEYS[@]}; do
    # キーと値を分割する
    arr=(`echo "${e}" | tr -s '=' ' '`)
    # キーを大文字に変換して変数定義する 
    export ${arr[0]^^}="${arr[1]}"
    let i++
done

echo "HOGE: ${HOGE}"
echo "FUGA: ${FUGA}"
