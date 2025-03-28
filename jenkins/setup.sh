#!/bin/bash

# Start Jenkins
exec /usr/bin/tini -- /usr/local/bin/jenkins.sh
