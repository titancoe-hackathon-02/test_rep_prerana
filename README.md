# test_rep_prerana
this is for learning

## Express JWT Auth (added)

Simple demo added to show a JWT-based authentication endpoint.

- Start server:

```bash
npm install
npm start
```

- Endpoints:

	- `POST /api/auth/login` — body JSON: `{ "email": "test@example.com", "password": "password" }` returns `{ "token": "..." }`
	- `GET /api/protected` — requires header `Authorization: Bearer <token>` returns protected JSON when token is valid.

Default demo user: `test@example.com` / `password`.
