USAGE :
    
    ./vacuum <name_file>
    
GOAL :
    
Obtain the final position of the automatic vacuum after multiple actions

TYPE OF ACTIONS :

D : rotate 90° on right

G : rotate 90° on left

A : move forward

FILE TEMPLATE :

<board's_width_max>  <board's_height_max>

<origin_x> <origin_y>  <origin_direction>

<actions>

EXAMPLE :

    ./vacuum examples_txt/file.txt
    5 6 N
