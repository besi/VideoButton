#!/bin/bash

MINUTES=5
sleep $((MINUTES * 60))
git checkout main
UPSTREAM=origin
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")
BASE=$(git merge-base @ "$UPSTREAM")

if [ $LOCAL = $BASE ]; then
    echo "Updating software from $LOCAL to $REMOTE"
    # git reset --hard master
    git pull
    sudo systemctl restart video-button
fi
