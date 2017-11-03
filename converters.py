# -*- coding: utf-8 -*-

import sys

turkish_chars = ['ı','ğ','ü','ç','ö','ş','Ü','Ğ','Ç','Ö','İ','Ş']
replacements  = ['i','g','u','c','o','s','U','G','C','O','I','S']

def toLatin(filename):
    #replaces the turkish characters
    input_file = open(filename,'r')

    content = input_file.read()

    for c_index in range(len(turkish_chars)):
        content = content.replace(turkish_chars[c_index],replacements[c_index])
    

    output_file_name = "latin_"+ filename

    output_file = open(output_file_name,'w')
    output_file.write(content)