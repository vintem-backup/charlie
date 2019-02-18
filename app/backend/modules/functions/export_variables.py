#!/usr/bin/env python3

#Importing Libraries

import sys
import os

#Exporting environment variables

def export_env_var(path_to_config):
    '''
    Export environmet variables on config file. Input: path_to_config
    '''
    config = open(path_to_config).readlines()
    
    for i in range(1,len(config)-1):
        if ('=' in config[i]):
            key=config[i].split('=')[0]
            value=config[i].split('=')[1].split()[0]
            os.environ[key] = value
            print (f'Exported: {key} = {value}\n')