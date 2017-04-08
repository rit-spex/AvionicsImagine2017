function(group) {
	var loader = new THREE.OBJLoader();
	loader.load("models/model.obj", function( obj ) {
		obj.scale.set(35,35,35);
		group.add( obj );
		return group;
	});
}