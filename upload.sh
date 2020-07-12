#!/bin/bash

# using: ./upload.sh "string comment"

#COMMENT=&{1?Error: message error}

echo "Commit's comment: '$1'"
git add .
git s
git commit -m "$1"
git push origin master
git s


