window.onload = function() {
	// SocketIO stuff

	DATA= {x:0.0, y:0.0, z:0.0};
	var socket = io();

	socket.on('toClient', function(data) {
		console.log(data);
		DATA.x = data.x;
		DATA.y = data.y;
		DATA.z = data.z;
		console.log(DATA);
	});


	//ThreeJS stuff
	renderer = null;
	var scene, camera, group;


	var windowHalfX = window.innerWidth / 2;
	var windowHalfY = window.innerHeight / 2;

	var container = document.createElement( 'div' );
	document.body.appendChild( container );

	var info = document.createElement( 'div' );
	info.style.position = 'absolute';
	info.style.top = '10px';
	info.style.width = '100%';
	info.style.textAlign = 'center';
	info.style.color = 'white';
	info.innerHTML = 'CubeSat Visualization';
	container.appendChild( info );

	init3d();
	// initBackground();
	container.appendChild( renderer.domElement );

	window.addEventListener( 'resize', onWindowResize, false );

	animate();
}

/// Events from extrude shapes example

function onWindowResize() {

	windowHalfX = window.innerWidth / 2;
	windowHalfY = window.innerHeight / 2;

	camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();

	renderer.setSize( window.innerWidth, window.innerHeight );
}

function animate() {

	/// compatibility : http://caniuse.com/requestanimationframe
	requestAnimationFrame( animate );

	render();
}

function render() {
	group1.rotation.x = DATA.x;
	group1.rotation.y = DATA.y;
	group1.rotation.z = DATA.z;
	renderer.render( scene, camera );
}

var init3d = function(){

	/// Global : renderer
	renderer = new THREE.WebGLRenderer( { alpha:true, antialias: true } );
	renderer.setClearColor( 0x000000, 0);
	renderer.setPixelRatio( window.devicePixelRatio );
	renderer.setSize( window.innerWidth, window.innerHeight );

	/// Global : scene
	scene = new THREE.Scene();

	/// Global : camera
	camera = new THREE.PerspectiveCamera( 80, window.innerWidth / window.innerHeight, 0.01, 5000 );
	camera.position.set( 0, 0, 200 );

	/// Global : group
	group1 = new THREE.Group();
	//scene.add( group1 );
	console.log(scene);

	var loader = new THREE.ColladaLoader();
	loader.options.convertUpAxis = true;
	loader.load("models/cubesat.dae", function( collada ) {
		dae = collada.scene;
		dae.traverse( function ( child ) {
			if ( child instanceof THREE.Mesh ) {
				child.material.color.setHex('0xff7b00');
			}
		});
		dae.scale.set(1000,1000,1000);
		dae.updateMatrix();
		group1.add( dae );
		scene.add( group1 );
	});

	/// direct light
	var light = new THREE.DirectionalLight( 0x404040 );
	light.position.set( 0.75, 0.75, 1.0 ).normalize();
	scene.add( light );

	/// ambient light
	var ambientLight = new THREE.AmbientLight(0x404040);
	scene.add( ambientLight );

};
