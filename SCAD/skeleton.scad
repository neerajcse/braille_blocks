width_of_edge=3;
height_of_edges=40;
module edge() {
    cube([width_of_edge, width_of_edge, height_of_edges]);
}
      
cube([61.54*2,
      41.29,
      width_of_edge]);

      
translate([61.54*2 - width_of_edge,0,0]) edge();
translate([61.54*2 - 2,41.29-2,0]) edge();
translate([0,41.29-2,0]) edge();
edge();

/**
translate([0,0,20]) cube([2,41.29,2]);
translate([0,0,20]) cube([61.54*2,2,2]);
translate([61.54*2-2,0,20]) cube([2,41.29,2]);
translate([0,41.29-2,20]) cube([61.54*2,2,2]);**/