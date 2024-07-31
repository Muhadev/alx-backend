import redis from 'redis';

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

// Create the hash with various fields
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display the hash
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.error(`Error retrieving hash: ${err.message}`);
    return;
  }
  console.log(result);
});

// Close the client connection
client.quit();
