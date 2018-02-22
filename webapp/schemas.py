#!/usr/bin/python
# encoding: iso-8859-1

""" Filename:        schemas.py
    Purpose:         Este arquivo e um agrupamento das regras
                     de validação das requisições via web service
    Requirements:    Cerberus
    Author:          Humbertho Mattar
"""

uptime_robot_alerts = {
    'monitorID': {
        'type': 'string',
        'required': True
    },
    'monitorURL': {
        'type': 'string',
        'required': True
    },
    'monitorFriendlyName': {
        'type': 'string',
        'required': True
    },
    'alertType': {
        'type': 'string',
        'required': True
    },
    'alertTypeFriendlyName': {
        'type': 'string',
        'required': True
    },
    'monitorAlertContacts': {
        'type': 'string',
        'required': True
    },
    'alertDuration': {
        'type': 'string',
        'required': False
    },
    'alertDateTime': {
        'type': 'string',
        'required': False
    },
    'alertFriendlyDuration': {
        'type': 'string',
        'required': False
    },
    'alertDetails': {
        'type': 'string',
        'required': False
    },
    'sslExpiryDate': {
        'type': 'string',
        'required': False
    },
    'sslExpiryDaysLeft': {
        'type': 'string',
        'required': False
    }
}
