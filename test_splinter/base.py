# coding: utf-8
#!/usr/bin/env python

import unittest

from splinter import Browser
from time import sleep

from datetime import date, datetime


class BaseAcceptanceSplinterTestCase(unittest.TestCase):

    domain = 'http://www.mopi.com.br/barra'

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('firefox')
        #cls.browser = Browser('chrome')

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def visit(self, url, title=None, status_code=None):
        self.browser.visit('%s%s' % (self.domain, url))
        if status_code:
            assert self.browser.status_code.is_success()
            assert self.browser.status_code.code == status_code

        if title:
            assert self.browser.title == title


    def doLogin(self, login=None, senha=None):

        self.visit('/')

        sleep(1)

        self.browser.fill('login', login)
        self.browser.fill('senha', senha)

        self.browser.find_by_css(
                '.botao-ok').first.click()
        sleep(1)

    


