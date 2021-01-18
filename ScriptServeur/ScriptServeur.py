# -*- coding: utf-8 -*-
# Copyright (c) 2020, Guerbadot Alexandre and contributors
# For license information, please see license.txt

Document = frappe.get_doc(dict(doctype="History Of Passage"))

def insert_document():
	"""
	Insert a document in the doctype History Of Presence
	"""
	badge = frappe.db.get_list('Badge Management Settings',fields= ['name'])
	unit = frappe.db.get_value('Badge Management Settings',badge[0].name,'default_unit')
	item = frappe.db.get_value('Badge Management Settings',badge[0].name,'default_item')
	allUnpairPassage = frappe.db.get_list('History Of Passage',
	filters={
	'is_paired' : 0,
	'date' : ['>', frappe.utils.nowdate()]
	},
	fields= ['name','date','customer','user'],
	)
	user = frappe.db.get_value("History Of Passage",allUnpairPassage[0].name,'user')
	customer = frappe.db.get_value("History Of Passage",allUnpairPassage[0].name,'customer')
	unpairedDoc = frappe.db.get_list('History Of Passage',
	filters={
	'customer' : customer,
	'is_paired' : 0,
	'date' : ['>',frappe.utils.nowdate()],
	'user' : user},
	fields= ['name', 'date'])
	if len(unpairedDoc)==2:
		doc = frappe.get_doc({
			'doctype' : 'History Of Presence',
			'user' : frappe.db.get_value("History Of Passage",unpairedDoc[0].name,'user'),
			'customer' : frappe.db.get_value("History Of Passage",unpairedDoc[0].name,'customer'),
			'start_date' : frappe.db.get_value("History Of Passage",unpairedDoc[1].name,'date'),
			'start_date_document' : unpairedDoc[1].name,
			'end_date' : frappe.db.get_value("History Of Passage",unpairedDoc[0].name,'date'),
			'end_date_document' : unpairedDoc[0].name,
			'item' : item,
			'unit' : unit
		})
		doc.insert(ignore_permissions=True)
		frappe.db.set_value('History Of Passage', unpairedDoc[0].name,'is_paired', 1)
		frappe.db.set_value('History Of Passage', unpairedDoc[1].name,'is_paired', 1)
	
insert_document()