#!/bin/bash

# using: ./upload.sh "string comment"
# chmod +x upload.sh

#COMMENT=&{1?Error: message error}

echo "Commit's comment: '$1'"
git add .
git status
git commit -m "$1"
git push origin master
git status


