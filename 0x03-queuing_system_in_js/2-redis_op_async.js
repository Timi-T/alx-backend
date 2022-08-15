// Connect to a Redis server

import { createClient } from 'redis';

const util = require('util');

const client = createClient().connect();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

const readCache = util.promisify(client.get);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, val) => console.log(val));
}

async function displaySchoolValue(schoolName) {
  const readCache = util.promisify(client.get);
  //const res = await readCache.apply(schoolName).catch((msg) => console.log(msg));
  console.log(readCache())
  //await readCache(schoolName)
    //.then(() => console.log("ope"))
  //client.get(schoolName, (err, val) => console.log(val));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
