#! usr/bin/python3
# -*- coding: utf-8 -*-
#
# Flicket - copyright Paul Bourne: evereux@gmail.com

from flask import (flash,
                   redirect,
                   url_for,
                   request,
                   render_template,
                   g)
from flask_login import login_required

from . import flicket_bp
from application import app
from application.flicket.forms.flicket_forms import CreateTicketForm
from application.flicket.models.flicket_models_ext import FlicketTicketExt


# create ticket
@flicket_bp.route(app.config['FLICKET'] + 'ticket_create/', methods=['GET', 'POST'])
@login_required
def ticket_create():
    form = CreateTicketForm()

    if form.validate_on_submit():

        new_ticket = FlicketTicketExt.create_ticket(title=form.title.data,
                                                    user=g.user,
                                                    content=form.content.data,
                                                    category=form.category.data,
                                                    priority=form.priority.data,
                                                    files=request.files.getlist("file"))

        flash('New Ticket created.', category='success')

        return redirect(url_for('flicket_bp.ticket_view', ticket_id=new_ticket.id))

    return render_template('flicket_create.html', title='Flicket - Create Ticket', form=form)
