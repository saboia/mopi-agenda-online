# coding: utf-8
#!/usr/bin/env python

import logging,smtplib, simplejson

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


EMAIL = {
    "endereco":"Agenda <noreply@globo.com>",
    "subject":"Entre em campo com o Cartola FC",
    "server":"smtpar.globoi.com",
    "port":25,
    "retorno":"http://cartolafc.local.globoi.com:8180",
    "img_domain":"http://s.glbimg.dev.globoi.com",
}


class EmailHelper:

    @staticmethod
    def mensagem(destinatario=None,corpo=None,subject=None,strFrom=None):

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject or EMAIL['subject']
        msgRoot['From'] = strFrom or EMAIL['endereco']
        msgRoot['To'] = destinatario
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        msgText = MIMEText(corpo.encode('utf-8'), 'html')
        msgAlternative.attach(msgText)

        return msgRoot.as_string()

    @staticmethod
    def enviar(mensagem=None,destinatario=None):

        sender = 'noreply@globo.com'
        receivers = []

        #suporta varios destinararios
        receivers.append(destinatario)

        server = smtplib.SMTP(EMAIL['server'], EMAIL['port'])
        server.sendmail(sender, receivers, mensagem)
        server.quit()
