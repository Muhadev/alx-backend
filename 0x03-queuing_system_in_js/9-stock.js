import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// Data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

// Utility function to get item by id
const getItemById = (id) => {
  return listProducts.find(product => product.itemId === parseInt(id));
};

// Redis client
const client = createClient();
client.on('error', (err) => console.error('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// Promisified Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to reserve stock by id
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Function to get current reserved stock by id
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock !== null ? parseInt(stock) : null;
};

// Routes
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(req.params.itemId) ?? item.initialAvailableQuantity;
  res.json({
    ...item,
    currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);
  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentStock = await getCurrentReservedStockById(req.params.itemId) ?? item.initialAvailableQuantity;

  if (currentStock < 1) {
    return res.json({ status: 'Not enough stock available', itemId: item.itemId });
  }

  await reserveStockById(req.params.itemId, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId: item.itemId });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
