#!/bin/bash

eval $(ssh-agent -s)
ssh-add ~/.ssh/gitlab

ssh -T git@gitlab.com
