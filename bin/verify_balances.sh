#!/bin/sh

TOKEN_MARIO=`curl --silent -X POST -H "API-Key: $POSTBANK_API_KEY" -F "username=$POSTBANK_USERNAME" -F "password=$POSTBANK_PASSWORD" https://hackathon.postbank.de/bank-api/gold/postbankid/token | jq .token | sed -e 's/^"//' -e 's/"$//'`
echo "Balances Jan-Paul:"
BALANCE_MARIO=`curl --silent -H "API-Key: $POSTBANK_API_KEY" -H "x-auth: $TOKEN_MARIO" https://hackathon.postbank.de:443/bank-api/gold/postbankid/?refreshCache=true | jq .accounts | grep amount\"`
echo $BALANCE_MARIO

TOKEN_MARIU=`curl --silent -X POST -H "API-Key: $POSTBANK_API_KEY" -F "username=$POSTBANK_ORGA_USERNAME" -F "password=$POSTBANK_PASSWORD" https://hackathon.postbank.de/bank-api/gold/postbankid/token | jq .token | sed -e 's/^"//' -e 's/"$//'`
echo "Balances Axel:"
BALANCE_MARIU=`curl --silent -H "API-Key: $POSTBANK_API_KEY" -H "x-auth: $TOKEN_MARIU" https://hackathon.postbank.de:443/bank-api/gold/postbankid/?refreshCache=true | jq .accounts | grep amount\"`
echo $BALANCE_MARIU
