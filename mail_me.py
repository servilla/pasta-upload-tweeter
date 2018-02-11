#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: mail_me

:Synopsis:
    Send email message using verified gmail account
 
:Author:
    servilla

:Created:
    2/10/18
"""

import logging
import smtplib

import daiquiri

import properties

logger = daiquiri.getLogger(__name__)

def mail_me(status='INFO', msg=None, to=None):
    subject = 'Subject: pasta-upload-tweeter ' + status + '...\n'
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(properties.GMAIL_NAME, properties.GMAIL_PASSWORD)
        smtpObj.sendmail(properties.GMAIL_NAME, to, subject + msg)
        smtpObj.quit()
        response = 'Sending email to ' + to + ' succeeded'
        logger.info(response)
        return response
    except Exception as e:
        response = 'Sending email failed - ' + str(e)
        logger.error(response)
        return response


def main():
    return 0


if __name__ == "__main__":
    main()