
# -*- coding: utf-8 -*-
import jinja2
from docxtpl import DocxTemplate, RichText

# from jinja2 import Environment, FileSystemLoader

################### example1 ############################
# file_loader = jinja2.FileSystemLoader('templates')

# env = jinja2.Environment(loader=file_loader)

# template = env.get_template('hello_world.txt')

# content = {'name': 'Yoni', 'lastname': 'gg'}
# output = template.render(data=content)
# print(output)

################## example 2 #############################

doc = DocxTemplate("Fishman_Daily_Check_FORMAT.docx")
# Where the magic happens

rt = RichText()

# rt.add("\u2713", color='#008000')
rt.add("\u2717", color='#FF0000')
context = {
    "current_date": "01/01/20",
    "DC2008": rt,
    "MEGA_PDC": rt,
    "Newdc": rt,
    "Cluster": rt,
    "ESXi01": rt,
    "ESXi02": rt,
    "ESXi03": rt,
    "ESXi04": rt,
    "ESXi05": rt,
    "ESXi06": rt,
    "Datastore2": rt,
    "Datastore3": rt,
    "Datastore4": rt,
    "Datastore5": rt,
    "Reduxio_Datastore1": rt,
    "Reduxio_Datastore2": rt,
    "Reduxio_Datastore3": rt,
    "Reduxio_Datastore4": rt,
    "Database_Mount": rt,
    "Logs": rt,
    "MailFlow": rt,
    "fishman_sme": rt,
    "snapmirror": rt,
    "toys_sme": rt,
    "BARCELONA": rt,
    "newexchange": rt,
    "TOYS_SQL": rt,
    "FASHION_SQL_SMS": rt,
    "toys_fileserver": rt,
    "Tele_Fileserver": rt,
    "Filserver_Fishman": rt,
    "HyperV": rt,
    "fishman_sql": rt,
    "fishman_dc": rt,
    "fishman_cert": rt
}


# context = {'status': rt, "date": "other Tomer123"}

doc.render(context)
doc.save("generated_doc.docx")
