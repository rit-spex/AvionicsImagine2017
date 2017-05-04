function(group) {
	var loader = new THREE.ObjectLoader();
	loader.load("models/model.json", function( object ) {
		object.scale.set(35,35,35);
		group.add( object );
		scene.add( group );
	});
	return group;
}


