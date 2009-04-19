#! /bin/sh

echo "CGI START"
#sleep 5
for var in DOCUMENT_ROOT SCRIPT_NAME SCRIPT_FILENAME REQUEST_URI QUERY_STRING PATH_INFO; do
    echo "  $var : ${!var}"
done
echo "CGI END"
exit 0
