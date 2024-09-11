import * as THREE from 'three';

async function fetchAsteroidData() {
    const response = await fetch('/orbit');
    const data = await response.json();
    return data.near_earth_objects;
}

async function createOrbit(asteroid) {
    const geometry = new THREE.CircleGeometry(1, 64);
    const material = new THREE.LineBasicMaterial({ color: 0xff0000 });
    const orbit = new THREE.LineLoop(geometry, material);

    const semiMajorAxis = parseFloat(asteroid.orbital_data.semi_major_axis);
    const eccentricity = parseFloat(asteroid.orbital_data.eccentricity);

    orbit.scale.set(semiMajorAxis, semiMajorAxis * Math.sqrt(1 - Math.pow(eccentricity, 2)), 1);
    orbit.rotation.x = Math.PI / 2; // Rotate to lie flat
    return orbit;
}

async function initOrbitVisualization() {
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000000);

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 10;

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('visualization').appendChild(renderer.domElement);

    const light = new THREE.PointLight(0xffffff);
    light.position.set(10, 10, 10);
    scene.add(light);

    const asteroids = await fetchAsteroidData();
    for (const date in asteroids) {
        for (const asteroid in asteroids[date]) {
            const orbit = createOrbit(asteroid);
            scene.add(orbit);
        }
    }

    function animate() {
        requestAnimationFrame(animate);
        renderer.render(scene, camera);
    }
    animate();
}

document.addEventListener('DOMContentLoaded', initOrbitVisualization);
