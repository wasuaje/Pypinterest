
# -*- coding: utf-8 -*-
#! /usr/bin/env python
from pyterest import *
 
p = Pinterest()
logged = p.login('hidu72@gmail.com','violeta23')
print logged
if logged:
    print 'logged in.'
    boards = p.getBoards()
    print boards