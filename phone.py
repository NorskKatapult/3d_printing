from solid import *
from solid.utils import * 

def iphone_holder():
    # Dimensions
    width = 80  # Holder width
    depth = 100  # Holder depth
    height = 20  # Holder height
    phone_thickness = 7.4  # iPhone 12 thickness
    phone_height = 146.7  # iPhone 12 height

    # Base
    base = cube([width, depth, height])

    # Phone support
    support_height = height + 20  # Height of the support
    support = translate([width/2 - 5, depth, 0])(cube([10, 20, support_height]))

    # Create the holder
    holder = base + support

    # Create a cutout for the phone
    cutout = translate([10, 0, height])(cube([width - 20, 10, phone_height + phone_thickness]))
    
    # Final model
    model = holder - cutout

    return model

if __name__ == '__main__':
    scad_render_to_file(iphone_holder(), 'iphone_holder.scad')
