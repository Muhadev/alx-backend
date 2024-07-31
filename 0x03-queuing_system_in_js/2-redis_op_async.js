import redis from 'redis';
import { promisify } from 'util';

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

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

// Function to set a new school value
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the school value using async/await
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error fetching the value: ${err.message}`);
  }
}

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
