# csvre
csv rearranger
tyler weston 2023

python csvre.py input_filename output_filename input_pattern output_pattern (-r)

-r is an optional flag that ignores the first line of the input file, if it is a header
-r must appear as the last argument if present

input_pattern can be a letter, or to ignore a column use an underscore
output_pattern can either be a letter that matches with an input column to rearrange or a static string

note that each key used in input_pattern must be present in output_pattern

to generate the output from the input:
python csvre.py test.csv out.csv a,b,_,_,e,_,g,h g,h,"string",e,b,"string2",a -r
