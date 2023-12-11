#!/usr/bin/node

const argv = process.argv;

if (isNaN(parseInt(argv[2]))) {
				console.log('Missing size');
} else {
				for (let i = 0; i < argv[2]; i++) {
								console.log('#'.repeat(argv[2]));
				}
}
