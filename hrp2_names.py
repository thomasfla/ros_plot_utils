#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  scrolling_topic.py
#  
#  Copyright 2017 Thomas Flayols <tflayols@arequipa>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
NBj = 30
NameToId = { "rhy" : 0,
            "rhr" : 1,
            "rhp" : 2,
            "rk"  : 3,
            "rap" : 4,
            "rar" : 5,
            "lhy" : 6,
            "lhr" : 7,
            "lhp" : 8,
            "lk"  : 9,
            "lap" : 10,
            "lar" : 11,
            "ty"  : 12,
            "tp"  : 13,
            "hy"  : 14,
            "hp"  : 15,
            "rsp" : 16,
            "rsr" : 17,
            "rsy" : 18,
            "re"  : 19,
            "rwy" : 20,
            "rwp" : 21,
            "rh"  : 22,
            "lsp" : 23,
            "lsr" : 24,
            "lsy" : 25,
            "le"  : 26,
            "lwy" : 27,
            "lwp" : 28,
            "lh"  : 29 }
IdToName = {0:"rhy",
            1:"rhr"  ,
            2:"rhp"  ,
            3:"rk"   ,
            4:"rap"  ,
            5:"rar"  ,
            6:"lhy"  ,
            7:"lhr"  ,
            8:"lhp"  ,
            9:"lk"   ,
            10:"lap" ,
            11:"lar" ,
            12:"ty"  ,
            13:"tp"  ,
            14:"hy"  ,
            15:"hp"  ,
            16:"rsp" ,
            17:"rsr" ,
            18:"rsy" ,
            19:"re"  ,
            20:"rwy" ,
            21:"rwp" ,
            22:"rh"  ,
            23:"lsp" ,
            24:"lsr" ,
            25:"lsy" ,
            26:"le"  ,
            27:"lwy" ,
            28:"lwp" ,
            29:"lh"    }
        
IdTolongName = {0: "Right Hip Yaw",
                1: "Right Hip Roll"  ,
                2: "Right Hip Pitch"  ,
                3: "Right Knee"   ,
                4: "Right Ankle Pitch"  ,
                5: "Right Ankle Roll"  ,
                6: "Left Hip Yaw"  ,
                7: "Left Hip Roll"  ,
                8: "Left Hip Pitch"  ,
                9: "Left Knee"   ,
                10:"Left Ankle Pitch" ,
                11:"Left Ankle Roll" ,
                12:"Torso Yaw"  ,
                13:"Torso Pitch"  ,
                14:"Head Yaw"  ,
                15:"Head Pitch"  ,
                16:"Right Shoulder Pitch" ,
                17:"Right Shoulder Roll" ,
                18:"Right Shoulder Yaw" ,
                19:"Right Elbow"  ,
                20:"Right Wrist Yaw" ,
                21:"Right Wrist Pitch" ,
                22:"Right Hand"  ,
                23:"Left Shoulder Pitch" ,
                24:"Left Shoulder Roll" ,
                25:"Left Shoulder Yaw" ,
                26:"Left Elbow"  ,
                27:"Left Wrist Yaw" ,
                28:"Left Wrist Picth" ,
                29:"Left Hand"    } 
            
        


