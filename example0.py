
# -*- coding: utf-8 -*-
#! /usr/bin/env python

from lib import pypinterest

"""Naive use of this library"""
if __name__ == '__main__':

	#create a client instance, make sure hte email address, user name and password are correct
	myclient = pypinterest.Client('hidu72@gmail.com', 'vitasunsetcom', 'Violeta23')

	#create a board
#	print myclient.createboard('design', 'art')

	#delete a board
#	print myclient.deleteboard('design')

	#get exsited boards
	print myclient.getboards()

	#search for pins
#	print myclient.searchpins('football', 20)

	#get all pins in the category
#	print myclient.getallpins('design', 1, 2)

	#like a pin
#	print myclient.like('4011087138419093')

	#unlike it
#	print myclient.unlike('4011087138419093')

	#repin a pin
#	print myclient.repin('4011155857117241', '4011087138419093', 'sweet')

	#pin a pin
#	print myclient.pin('4011155857117241', 'test', 'https://www.google.com/logos/classicplus.png', 'www.google.com', 'hooray')

	#delete a pin
#	print myclient.deletepin('4011087138919086')

	#read info from a pin
#	print myclient.readpin('4011087138419093')

#that's it
#have fun!