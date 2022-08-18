// HSet in redis

import { createClient } from 'redis';

const redis = require('redis');

const util = require('util');

(async () => {
const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

client.on('connect', () => console.log('Redis client connected to the server'));

async function hashSet(hash, key, value) {
  const setSch = util.promisify(client.hset).bind(client);
  const res = await setSch(hash, key, value);
}

function hashGet(hash) {
    client.hgetall('HolbertonSchools', (err, val) => console.log(val));
}

//client.hset('HolbertonSchools', 'Portland', 50, (val) => console.log(val));
await hashSet('HolbertonSchools', 'Portland', 50)
  .then((res) => redis.print(res));
await hashSet('HolbertonSchools', 'Seattle', 80)
  .then((res) => redis.print(res));
await hashSet('HolbertonSchools', 'New York', 20)
  .then((res) => redis.print(res));
await hashSet('HolbertonSchools', 'Bogota', 20)
  .then((res) => redis.print(res));
await hashSet('HolbertonSchools', 'Cali', 40)
  .then((res) => redis.print(res));
await hashSet('HolbertonSchools', 'Paris', 2)
  .then((res) => redis.print(res));
hashGet('HolbertonSchools');
//client.hgetall('HolbertonSchools', (val) => console.log(val));
})();
