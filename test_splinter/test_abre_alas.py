# coding: utf-8
#!/usr/bin/env python

from test_splinter.base import BaseAcceptanceSplinterTestCase

from test_splinter.emailhelper import EmailHelper

from datetime import datetime


class AbreTestCase(BaseAcceptanceSplinterTestCase):

    def test_login_mopi(self):
        login = 'barreto2008@escola24horas.com.br'
        senha = 'barreto'

        self.doLogin(login=login, senha=senha)

        self.browser.visit('http://www.mopi.com.br/secretaria/age-impressao.cfm?order=data_inicio,COD_MSG&noprinter=1')
        corpo = self.browser.find_by_id('listaagenda_efaf')

        mensagem=EmailHelper.mensagem(destinatario='saboia@gmail.com,karinaafreire@gmail.com,freire.lucas07@gmail.com',corpo=corpo.first.html,subject="Agenda Online do dia %s" % datetime.now() )
        EmailHelper.enviar(mensagem=mensagem,destinatario='saboia@gmail.com')
        EmailHelper.enviar(mensagem=mensagem,destinatario='karinaafreire@gmail.com')
        EmailHelper.enviar(mensagem=mensagem,destinatario='freire.lucas07@gmail.com')