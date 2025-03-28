#!/bin/bash

set -e  # Exit on error

echo "Starting Jenkins at $(date)"

# Start Jenkins
exec /usr/bin/tini -- /usr/local/bin/jenkins.sh || {
    echo "Failed to start Jenkins"
    exit 1
}