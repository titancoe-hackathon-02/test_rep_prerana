require('dotenv').config();
const express = require('express');
const authRoutes = require('./routes/auth');
const auth = require('./middleware/auth');

const app = express();
app.use(express.json());

app.use('/api/auth', authRoutes);

app.get('/api/protected', auth, (req, res) => {
  res.json({ message: 'Protected data', user: req.user });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
