function(group) {
	var loader = new THREE.ColladaLoader();
	loader.options.convertUpAxis = true;
	loader.load("models/model.dae", function( collada ) {
		dae = collada.scene;
		dae.scale.set(35,35,35);
		dae.updateMatrix();
		group.add( dae );
		return group;
	});
}