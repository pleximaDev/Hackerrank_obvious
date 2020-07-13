#!/bin/bash

# using: ./upload.sh "string comment"
# chmod +x upload.sh

#COMMENT=&{1?Error: message error}

echo "Commit's comment: '$1'"
git add .
git status

if [$1 == ""]
	then git commit -m "Default commit."
else
	git commit -m "$1"
fi

git push origin master
git status


