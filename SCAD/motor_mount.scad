base_length = 61.55;
base_width = 43;
half_base_width = base_width/2;

module dual_motor_mould() {
    difference() {
    	union() {
			cube([61.55,base_width,4]);
			motor_block(0);
			translate([41.55,0,0]) motor_block(1);
		};
		translate([-3, 0, 2.7]) motor_base();
		translate([44.5, 0, 2.7]) motor_base();
    }
}

module motor_block(isLeft) {   
        if(isLeft) {
            translate([-1.2, 0,  0]) motor_wall();
        } else {
            translate([17.2, 0, 0]) motor_wall();
        }

   		difference() {
        	cube([20 ,base_width, 15]);
		}   
}

module motor_wall() {
		difference() {
			cube([4, base_width, 28]);
			translate([0, 16, 20]) cube([15, 11, 12]);
		}
}

module motor_base() {
	union() {
		translate([10,half_base_width,19]) rotate ([0,90,0]) cylinder (h = 20, r=15.5, center = true);
		translate([0, half_base_width-8, 0]) cube([20, 16, 6]);	
	}	
}

module screw_holes() {
	translate([30,4,22.5]) rotate([0, 90, 0]) cylinder(h = 40, r=2, center = true, $fn=100);
	translate([30,38.5,22.5]) rotate([0, 90, 0]) cylinder(h = 40, r=2, center = true, $fn=100);
}

module solenoid_hole() {
	translate([base_length/2, base_width/2, 2]) cylinder(h = 6, r = 1.5, center = true, $fn=100);	
}

difference() {
	dual_motor_mould();
	union() {
		screw_holes();
		solenoid_hole();
	}	
}