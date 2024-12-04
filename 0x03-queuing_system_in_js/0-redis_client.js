import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// On successful connection
client.on('connect', function() {
  console.log('Redis client connected to the server');
});

// On error
client.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

