#!/bin/bash
set -e
set -u

# ARTIFACTS_KEY should be set as env variable in the travis UI.
# TRAVIS_BRANCH is set automatically by travis
ARTIFACT=lizard-docs.zip
PROJECT=lizard-docs

curl -X POST \
     --retry 3 \
     -H "Content-Type: multipart/form-data" \
     -F key=${ARTIFACTS_KEY} \
     -F artifact=@${ARTIFACT} \
     -F branch=${TRAVIS_BRANCH} \
     https://artifacts.lizard.net/upload/${PROJECT}/
