#!/bin/bash

MYCROFT_CORE=

if  [ -z "$MYCROFT_CORE" ]
then
	echo "Please set the variable MYCROFT_CORE in this script"
else
	source "$MYCROFT_CORE/venv-activate.sh"
	python3 -m test.integrationtests.skills.runner
fi
