# Study-Card-Generator

This Python script can be used to generate a PDF grid in order to be used as a template for printing study cards. It uses the *Reportlab* module, so make sure you have it installed when launching.

Attributes such as colour, page size, horizontal- and vertical cells, a string at the bottom etc. can be adjusted at the beginning of the file.
Furthermore, there is a "generateTemplates" variable, that allows the user to generate all colours at the same time should this be useful. A blank backside will always be generated with the same layout, such that the front and backside can be combined in a pdf editor of your choice if you want to save coloured ink.
