base_length = 61.55;
base_width = 41;


module dual_motor_mould() {
    difference() {
    	union() {
			cube([61.55,41,4]);
			motor_block(0);
			translate([41.55,0,0]) motor_block(1);
		};
		translate([-4, 0, 2.7]) motor_base();
		translate([45.5, 0, 2.7]) motor_base();
    }
	
	
}

module motor_block(isLeft) {
        
        if(isLeft) {
            translate([0, 0,  0]) motor_wall();
        } else {
            translate([16, 0, 0]) motor_wall();
        }

   		difference() {
        	cube([20 ,41, 15]);
		}
        
}

module motor_wall() {
		difference() {
			cube([4, 41, 28]);
			translate([0, 16, 20]) cube([15, 8, 12]);
		}
}

module motor_base() {
	union() {
		translate([10,20.5,19]) rotate ([0,90,0]) cylinder (h = 20, r=15.5, center = true);
		translate([0, 20.5-8, 0]) cube([20, 16, 6]);	
	}	
}

module screw_holes() {
	translate([30,3,21]) rotate([0, 90, 0]) cylinder(h = 40, r=2, center = true, $fn=100);
	translate([30,38,21]) rotate([0, 90, 0]) cylinder(h = 40, r=2, center = true, $fn=100);
}

module solenoid_hole() {
	translate([base_length/2, base_width/2, 2]) cylinder(h = 6, r = 2, center = true, $fn=100);	
}

difference() {
	dual_motor_mould();
	union() {
		screw_holes();
		solenoid_hole();
	}	
}

