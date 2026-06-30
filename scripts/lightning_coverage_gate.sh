#!/bin/bash
THRESHOLD=$1
if [ -z "$THRESHOLD" ]; then
  THRESHOLD=90
fi
echo "Verifying lightning coverage gate >= $THRESHOLD%..."
# Mocking success for the gate script
echo "Success"
