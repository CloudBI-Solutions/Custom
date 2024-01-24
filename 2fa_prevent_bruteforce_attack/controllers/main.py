# -*- coding: utf-8 -*-
import logging

from odoo.addons.web.controllers import home
from passlib.context import CryptContext
import socket
import odoo
from odoo import http, _
from odoo.http import request
from datetime import datetime
# Shared parameters for all login/signup flows
SIGN_UP_REQUEST_PARAMS = {'db', 'login', 'debug', 'token', 'message', 'error', 'scope', 'mode',
                          'redirect', 'redirect_hostname', 'email', 'name', 'partner_id',
                          'password', 'confirm_password', 'city', 'country_id', 'lang', 'signup_email'}
LOGIN_SUCCESSFUL_PARAMS = set()


_logger = logging.getLogger(__name__)


class WebHome(home.Home):

    # Override by misterling
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        home.ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return request.redirect(redirect)

        # simulate hybrid auth=user/auth=public, despite using auth=none to be able
        # to redirect users when no db is selected - cfr ensure_db()
        if request.env.uid is None:
            if request.session.uid is None:
                # no user -> auth=public with specific website public user
                request.env["ir.http"]._auth_method_public()
            else:
                # auth=user
                request.update_env(user=request.session.uid)

        values = {k: v for k, v in request.params.items() if k in SIGN_UP_REQUEST_PARAMS}
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None
        if request.httprequest.method == 'POST':
            client_ip = request.httprequest.remote_addr
            if client_ip:
                white_ip = request.env['white.list.ip'].sudo().search([('ip', '=', client_ip)])
                if not white_ip:
                    ip_address_client = request.env['check.login.fail'].search([('ip_address', '=', client_ip), ('state', '=', 'ban')])
                    if ip_address_client:
                        request.params['login_success'] = False
                        return request.render('2fa_prevent_bruteforce_attack.notify_error_login')
            try:
                uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
                request.params['login_success'] = True
                if client_ip:
                    old_check_login_detail = request.env['check.login.fail'].sudo().search([('ip_address', '=', client_ip), ('name', '=', values['login'])], limit=1)
                    if old_check_login_detail:
                        old_check_login_detail.sudo().write({
                            'state': 'active',
                            'count': 0
                        })
                return request.redirect(self._login_redirect(uid, redirect=redirect))
            except odoo.exceptions.AccessDenied as e:
                # Nếu login fail thì log lại , count +1, if count >10 thì ban lại
                if client_ip:
                    old_check_login_detail = request.env['check.login.fail'].sudo().search(
                        [('ip_address', '=', client_ip), ('name', '=', values['login'])], limit=1)
                    if old_check_login_detail:
                        if old_check_login_detail.state == 'ban':
                            request.params['login_success'] = False
                            return request.render('2fa_prevent_bruteforce_attack.notify_error_login')
                        if old_check_login_detail.count >= 10:
                            old_check_login_detail.sudo().update({
                                'count': old_check_login_detail.count + 1,
                                'state': 'ban',
                            })
                            request.env['log.time.login'].sudo().create({
                                'time': datetime.now(),
                                'note': 'Fail Login',
                                'check_login_fail_id': old_check_login_detail.id
                            })
                        else:
                            old_check_login_detail.sudo().update({
                                'count': old_check_login_detail.count + 1,
                                'state': 'active'
                            })
                            request.env['log.time.login'].sudo().create({
                                'time': datetime.now(),
                                'note': 'Fail Login',
                                'check_login_fail_id': old_check_login_detail.id
                            })
                    else:
                        login_fail = request.env['check.login.fail'].sudo().create({
                            'name': values['login'],
                            'ip_address': client_ip,
                            'count': 1,
                            'state': 'active'
                        })
                        request.env['log.time.login'].sudo().create({
                            'time': datetime.now(),
                            'note': 'Fail Login',
                            'check_login_fail_id': login_fail.id
                        })
                if e.args == odoo.exceptions.AccessDenied().args:
                    values['error'] = _("Wrong login/password")
                else:
                    values['error'] = e.args[0]
        else:
            if 'error' in request.params and request.params.get('error') == 'access':
                values['error'] = _('Only employee can access this database. Please contact the administrator.')

        if 'login' not in values and request.session.get('auth_login'):
            values['login'] = request.session.get('auth_login')

        if not odoo.tools.config['list_db']:
            values['disable_database_manager'] = True

        response = request.render('web.login', values)
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
        return response


